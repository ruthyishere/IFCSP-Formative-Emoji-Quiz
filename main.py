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
        "celebrities": list(celebrity_dict.items()),
        "world cities": list(world_city_dict.items()),
        "movies": list(movies_dict.items()),
        "tv shows": list(tv_show_dict.items()),
        "brands": list(brands_dict.items()),
        "disney": list(disney_dict.items())
        }   
    
    score = 0
    
    print("🌟🌟🌟Welcome to The Emoji Quiz!🌟🌟🌟")
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

          If you fail to get the correct answer after three tries, you get 0 points for that round!

          The game will randomly select how many questions will be in your quiz, and if you reach the end of those questions you will receive your final score!

          Good luck!

          """)
    time.sleep(1)

    topics_selected = make_selection(choices)

    print()
    print("You have chosen: ")
    for topic in topics_selected:
        print(topic.capitalize())
    print()

    print("Making your quiz...")
    filtered_choice_to_question_dict = {}
    for topic in topics_selected:
        filtered_choice_to_question_dict[topic] = choice_to_question_dict_map[topic]
    question_set = curate_question_set(random.randint(5, 10), filtered_choice_to_question_dict)
    time.sleep(1)
    print()

    print("TIME TO QUIZ!!")
    print("When you input your answer, make sure your spelling and any other characters are correct and in the right places as best as you can make them.")
    time.sleep(3)
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()

    for topic in question_set:
        print(f"You are in the world of {topic}!")
        for emoji, answer in question_set[topic]:
            #user_ans = input(f"What do you think {emoji} means? --> ").title()
            points = 3
            while points > 0:
                user_ans = input(f"What do you think {emoji} means? --> ").lower()
                if user_ans == answer.lower():
                    score += points
                    print(f"Congrats! You answered correctly! You get an additional {points} points")
                    break
                else:
                    print(f"Sorry, {user_ans} is incorrect. Check your answer carefully and try again.")
                    points -=1
            if points == 0:
                print(f"Unlucky! The correct answer was {answer}. Better luck in the next question!")
        print()

    print("Congrats on making it to the end! You have a grand total of.... drumroll...")
    time.sleep(3)
    print(f"{score} points!!! Well done! Play again next time for a new ____ of The Emoji Quiz (not movie )")
    print("Credits: The Cosmopolitan --> https://www.cosmopolitan.com/uk/entertainment/quizzes-games/a38311108/emoji-quiz-questions/")

    

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