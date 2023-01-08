score = 0
print('Guess the animal!')


def checkAnswer(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct!')
            score = score+1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Nope! Guess Again ')
            attempt = attempt+1
    if attempt == 3:
        print('The correct answer is '+answer)


score = 0


guess1 = input('What animal is known as the king of the jungle?')
checkAnswer(guess1, ' lion')
guess2 = input('What bird symbolizes freedom?')
checkAnswer(guess2, ' eagle')
guess3 = input('What animal lurks in the sea in the town of Amity Island?')
checkAnswer(guess3, ' shark')
guess4 = input('What is the largest animal?')
checkAnswer(guess4, ' whale')
guess5 = input('What animal goes MEEP MEEP?')
checkAnswer(guess5, ' roadrunner')
guess6 = input('What animal has layers like onions?')
checkAnswer(guess6, ' ogre')
print('Your score is'+' '+str(score))
