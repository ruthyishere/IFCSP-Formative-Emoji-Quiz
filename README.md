# IFCSP-Formative-Emoji-Quiz

## Welcome to The Emoji Quiz!!

### User Documentation
✨🌌💫 Instructions 🤍☁️🌿
You will first get to choose which topics you'd like out of:
- Celebrities
- World cities
- Movies
- TV Shows
- Brands
- Disney Classics
You can select up to three topics topics or have the game randomly decide!
You will be presented with a series of emojis on that topic, and you will have to input what those emojis represent.

You will be given three guesses:
- Correct answer on 1st guess - 3 points
- Correct answer on 2nd guess - 2 points
- Correct answer on 3rd guess - 1 point

If you fail to get the correct answer after three tries, you get 0 points for that question!

The game will randomly select how many questions will be in your quiz, and if you reach the end of those questions you will receive your final score!

Good luck!


### Technical Documentation
You can run the main.py file either in the terminal, or by directly clicking on main.py and running that file directly. 
The code uses a modular design:
- `main.py`: runs the actual quiz program. Imports `emoji_dicts.py`, `quiz_functions.py` and the Python Standard Library modules `random` and `time`.
- `emoji_dicts.py`: stores the emojis and their corresponding answers.
- `quiz_functions.py`: stores the some of the functions used to select which topics and questions to use. Imports Python Standard Library module `random`.

At the end of `main`, you will wait five seconds before the program terminates to make sure that any program pop up doesn't immediately shut down right after displaying the score.



