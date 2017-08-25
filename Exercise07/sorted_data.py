from sys import argv

script, filename = argv

f = open(filename)
text = f.readlines()

ratings = {}

def clean_text(text):
    i = 0
    for item in text:
	text_split = item.split(':')
	ratings[text_split[0]] = text_split[1].strip("\n")
 	 i += 1

    return ratings

def print_ratings(ratings):
    for key, value in sorted(ratings.iteritems()):
        print "Restaurant %s is rated at %s." % (key, value)

def main():
    print_ratings(clean_text(text))

main()
