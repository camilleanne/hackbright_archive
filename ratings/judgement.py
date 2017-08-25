from flask import Flask, render_template, redirect, request, session, url_for, flash
import datetime, random, math
import model
app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhsupersecretthing"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    search_term = request.args.get("search")
    search_results = model.session.query(model.Movies).filter(model.Movies.name.like("%"+search_term+"%"))
    return render_template('search.html', search_results = search_results, search_term = search_term)

@app.route("/", methods=["POST"])
def sign_in():
    email = request.form.get("email")
    password = request.form.get("password")
    user_id = model.authenticate(email, password)
    if user_id != None:
        flash("loggedin!")

        session['user_id'] = user_id
        print session.get('user_id')
        # return redirect(url_for("view_user_ratings", user_id = user_id))
    else:
        flash("Password or email incorrect. Try again.")
    return redirect(url_for("index"))

@app.route("/signup")
def sign_up():
    return render_template('signup.html')

@app.route("/signup", methods=["POST"])
def sign_up():
    email = request.form.get("email")
    password = hash(request.form.get("password"))
    age = request.form.get("age")
    zipcode = request.form.get("zipcode")

    new_user = model.User(email = email, password = password, age = age, zipcode = zipcode)
    user_id = model.add_user(new_user)
    session['user_id'] = user_id
    return redirect(url_for("view_user_ratings", user_id = user_id))

@app.route("/users")
def view_all_users(): #same as index, above
    user_list = model.session.query(model.User).limit(20).all()
    return render_template("user_list.html", users = user_list)

@app.route("/users/<user_id>")
def view_user_ratings(user_id):
    user_ratings = model.session.query(model.Ratings).filter_by(user_id = user_id).all()
    return render_template("user_ratings.html", ratings = user_ratings)

@app.route("/movies")
def view_all_movies():
    random_start = random.randint(0, 1500)
    random_end = random_start + 100
    movie_list = model.session.query(model.Movies).filter(model.Movies.id > random_start, model.Movies.id < random_end).all()
    return render_template("movies.html", movies = movie_list)

@app.route("/movies/<movie_id>")
def view_movie(movie_id): # change to display movie title, not ID
    movie_details = model.session.query(model.Ratings).filter_by(movie_id=movie_id).all()
    movie = model.session.query(model.Movies).filter_by(id = movie_id).one()
    user_id = session.get('user_id')
    #get the object for the Judmental Eye
    the_eye = model.session.query(model.User).filter_by(id=946).one()
    rating = None
    difference = None
    effective_prediction = None
    eye_rating = None
    beratement = None
    
    if user_id:
        #if the user is logged in, then get their rating for this movie
        rating = model.session.query(model.Ratings).filter_by(movie_id = movie_id, user_id = user_id).all()
        if not rating:
            #if there isn't a rating already, get the user object,
            #then generate the rating prediction
            user = model.session.query(model.User).filter_by(id = user_id).one()
            prediction = model.rating_prediction(user, movie)
            effective_prediction = prediction

            #get the rating object for the Judmental Eye for that movie
            eye_rating = model.session.query(model.Ratings).filter_by(user_id = the_eye.id, movie_id = movie.id).first()
        
        #if there is a rating for the User, assign effective_prediction to it
        else:
            effective_prediction = rating[0].rating
            
        #if there is no rating for the Eye for that movie, predict one
        if not eye_rating:
            eye_rating = model.rating_prediction(the_eye, movie)
        else:
        #if there is a rating for the judgemental eye, set the eye_rating to the rating from that object
            eye_rating = eye_rating.rating

        difference = abs(eye_rating - effective_prediction)

        effective_prediction = math.floor(effective_prediction)

        messages = [ "I suppose you don't have such bad taste after all.",
                 "I regret every decision that I've ever made that has brought me to listen to your opinion.",
                 "Words fail me, as your taste in movies has clearly failed you.",
                 "That movie is great. For a clown to watch. Idiot.",]

        beratement = messages[int(difference)]

    return render_template("movie_ratings.html", details = movie_details, rating = rating, effective_prediction = effective_prediction, difference = difference, beratement = beratement)

@app.route("/movies/<movie_id>", methods=["POST"])
def rate_movie(movie_id):
    print "rating movie"
    rating = request.form.get("ratingRadio")
    if rating:
        new_rating = model.Ratings(movie_id = movie_id, user_id = session.get("user_id"), timestamp = datetime.datetime.now(), rating = rating)
        model.add_rating(new_rating) #add + commit

        flash("Your rating has been recorded!")
    else:
        flash("Please choose a rating!")
    return redirect(url_for("view_movie", movie_id = movie_id))


@app.route("/clear")
def session_clear():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)