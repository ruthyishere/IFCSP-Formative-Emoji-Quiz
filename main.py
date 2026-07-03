import random # Helps with randomly selecting the number of questions
from emoji_dicts import celebrity_dict, world_city_dict, movies_dict, tv_show_dict, brands_dict, disney_dict # importing the dictionaries that store the emojis and their corresponding answers
from quiz_functions import curate_question_set, make_selection # Helps with the selection and curation of the questions set 
import time # To space out all the print statement outputs 

def main():
    # Runs the main program for the quiz

    # Dicts to help manage choice of which topics, and final score variable initialisation
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
    
    # Start of the introduction to the quiz
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

    # Uses quiz_functions to guide the user into selecting their chosen quiz topics.
    topics_selected = make_selection(choices)

    print()
    print("You have chosen: ")
    for topic in topics_selected:
        print(topic.capitalize())
    print()

    # Curates the question set for the quiz
    print("Making your quiz...")
    filtered_choice_to_question_dict = {}
    for topic in topics_selected:
        filtered_choice_to_question_dict[topic] = choice_to_question_dict_map[topic]
    question_set = curate_question_set(random.randint(5, 10), filtered_choice_to_question_dict)
    time.sleep(1)
    print()

    print("TIME TO QUIZ!! 📝📝📝")
    print("When you input your answer, make sure your spelling and any other characters are correct and in the right places as best as you can make them.")
    time.sleep(3)
    print("Starting in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()

    # Ask questions to user, output is converted to lowercase and compared to lowercase answer. The more guesses they have, the less points they get.
    for topic in question_set:
        print(f"You are in the world of 🌟{topic}🌟!")
        for emoji, answer in question_set[topic]:
            points = 3
            while points > 0:
                user_ans = input(f"What do you think {emoji} means? --> ").lower()
                if user_ans == answer.lower():
                    score += points
                    print(f"Congrats! 🎉 You answered correctly! You get an additional {points} points")
                    break
                else:
                    print(f"Sorry, {user_ans} is incorrect. Check your answer carefully and try again.")
                    points -=1
            if points == 0:
                print(f"Unlucky! 😩 The correct answer was {answer}. Better luck in the next question!")
        print()

    print("Congrats on making it to the end! You have a grand total of.... drumroll...")
    time.sleep(3)
    print(f" 🎉 {score} points!!! Well done! 🥳 Play again next time!")
    time.sleep(1)
    print("Credits: The Cosmopolitan --> https://www.cosmopolitan.com/uk/entertainment/quizzes-games/a38311108/emoji-quiz-questions/")
    time.sleep(5)

main()