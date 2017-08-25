var Cat = function(name, furColor, tiredness, hunger, loneliness, happiness){
    this.name = name;
    this.furColor = furColor;
    this.tiredness = tiredness;
    this.hunger = hunger;
    this.loneliness = loneliness;
    this.happiness = happiness;
    this.feed = function(food) {
        hunger--;
        if (food == 'fish' || food == 'milk'){
            hunger--;
            console.log("Happy meow. I like "+food+". Hunger level: "+hunger);
            happiness++;
        }
        else{
            console.log("Ew gross meow. I don't like "+food+". Hunger level: "+hunger);
            happiness--;
        }

    };
    this.sleep = function(numMinutes){
        var previous_tiredness = tiredness;
        tiredness = tiredness - Math.floor(numMinutes/5);

        if (tiredness < previous_tiredness && tiredness >= 0){
            for (var i = 0; i < numMinutes; i++){
                console.log('z');
            }
            console.log("I was level "+previous_tiredness+" tired but now I'm at " + tiredness+"!");
            happiness = happiness + Math.floor(numMinutes/8);
        }
        else{
            console.log("I'm not that tired!");
            tiredness = previous_tiredness;
        }
    };
    this.pet = function(numPets) {
        var previous_loneliness = loneliness;
        if (loneliness <= 0){
            console.log("I don't want pets! Leave me alone!");
            happiness--;
            loneliness = 0;
        }
        else{
            for (var i = 0; i<numPets; i++) {
                console.log('Purr');
            }
            if (numPets < 5 && loneliness > 0){
                loneliness ++;
                console.log("That wasn't enough. I'm more lonely now than before.");
            }
            else{
                loneliness = loneliness - Math.floor(numPets/5);
                if (loneliness <= 0){
                    console.log("That was too many. I'm tired of you! Leave me alone!");
                    happiness--;
                    loneliness = 0;
                } else{
                    console.log("I miss you so much, I was level " + previous_loneliness+" lonely but now I'm only at " + loneliness+"!");
                    happiness = happiness + Math.floor(numPets/8);
                }
            }
        }
        
    };
    this.showCatStatus = function() {
        console.log(name+"'s status:");
        console.log("   Tiredness " + tiredness);
        console.log("   Hunger " + hunger);
        console.log("   Loneliness " + loneliness);
        console.log("   Happiness " + happiness);
    };
};

var mrSnuggles = new Cat ("Mr Snuggles", "calico", 8, 10, 6, 2);
mrSnuggles.feed("fish");
mrSnuggles.feed("chicken");
mrSnuggles.sleep(20);
mrSnuggles.pet(10);
mrSnuggles.showCatStatus();