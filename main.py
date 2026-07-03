# get quiz from --> https://www.cosmopolitan.com/uk/entertainment/quizzes-games/a38311108/emoji-quiz-questions/
# Max three goes! 
import random 
from emoji_dicts import celebrity_dict, world_city_dict, movies_dict, tv_show_dict, brands_dict, disney_dict
from quiz_functions import curate_question_set, make_selection
import time

def main():
    choices = {
        0: "random choice",
        1: "celebrities",
        2: "world cities",
        3: "movies",
        4: "tv shows",
        5: "brands",
        6: "disney"
    }

    choice_to_question_dict_map = {
        "celebrities": celebrity_dict,
        "world cities": world_city_dict,
        "movies": movies_dict,
        "tv shows": tv_show_dict,
        "brands": brands_dict,
        "disney": disney_dict
        }   
    
    print("🌟🌟🌟Welcome to the emoji quiz!🌟🌟🌟")
    print("""
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

          If you fail to get the correct answer after three tries, the game ends and you receive your final score!

          The game will randomly select how many questions will be in your quiz, and if you reach the end of those questions you will receive your final score!

          Good luck!

          """)
    time.sleep(3)
    

# print(celebrity_emojis)
# for key in celebrity_emojis:
#     print(key)

# print(random.choice(list(celebrity_emojis.items())))

# params = {"celebrity_emojis": list(celebrity_emojis.items())}

# question_set = curate_question_set(no_of_questions=5, **params)
# print(question_set)



# topics = make_selection(params)
# print(topics)

main()