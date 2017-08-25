var word = ['F', 'O', 'X', 'X'];
var guessed_letters = ['_', '_', '_', '_'];
var remaining_letter_count = word.length;
var reward = 0;

function guessLetter(letter){
    letter = letter.toUpperCase();
    var found=0;
    for (var i = 0; i < word.length; i++) {
        if (letter == word[i]) {
            guessed_letters[i] = letter;
            console.log("Congratulations! You've found a new letter.");
            remaining_letter_count--;
            found = 1;
        }
    }
    if (found === 0) {
        console.log(letter+": Wrong guess.  Keep trying.");
    }
    if (remaining_letter_count !== 0) {
        console.log(guessed_letters + ": There are "+remaining_letter_count+" letters remaining. Keep trying");
    } else {
        console.log(guessed_letters + ": Congratulations! You've won the game!!!");
    }

}

function guessLetterFortune(letter){
    letter = letter.toUpperCase();
    var found=0;
    var letterReward = Math.floor(Math.random() * 100);
    for (var i = 0; i < word.length; i++) {
        if (letter == word[i]) {
            guessed_letters[i] = letter;
            remaining_letter_count--;
            found += 1;
            reward = reward + letterReward;
        }
    }
    if (found === 0) {
        reward = reward - letterReward;
        if (reward < 0){
            reward = 0;
        }
        console.log(letter+": Wrong guess.  Keep trying. Your total winnings are now: "+reward);
    } else {
        console.log("Congratulations! You've found a new letter! Your total winnings are "+reward+"!");
    }
    if (remaining_letter_count !== 0) {
        console.log(guessed_letters + ": There are "+remaining_letter_count+" letters remaining. Keep trying");
    } else {
        console.log(guessed_letters + ": Congratulations! You've won the game and you won " + reward + "!!!");
    }

}