import random


def format_dict(dict):
    # number --> topic name
    return "\t\n".join(f"{key} --> {value}" for key,value in dict.items())

def make_selection(dict_choice):
    # number --> topic name
    while True:
        ## add in try, except
        no_of_topics_selection = int(input("""
                            How many topics would you like? You can choose up to three or let the game randomly decide.
                            Enter 1 - 3 for the number of topics or 4 to let the game decide -->
                              """))
        if  1 <= no_of_topics_selection <= 4:
            if no_of_topics_selection == 4:
                no_of_topics_selection = random.randint(1, 3)
            break
        else:
            print("Incorrect input. Please try again.")
    print(f"You will be quizzed on {no_of_topics_selection} topics!")

    topics_selected = []
    _dict_choice = dict_choice.copy()
    while no_of_topics_selection > 0:
        select_topics = int(input(f"""
                                Which topic would you like to select from? You have the following options to choose from.
                                Input the corresponding value for the topic as seen below.
                                {format_dict(_dict_choice)}
                                
                                Your selection --> 
                                """))

        if select_topics < 0 or select_topics >= len(_dict_choice):
            print(f"Please enter a valid input between 0 and {len(_dict_choice)}")
        elif select_topics not in _dict_choice:
            print("Your choice is no longer available. Try again.")
        else:
            if select_topics == 0:
                choice = random.choice(list(_dict_choice.keys())[1:])
            else:
                choice = select_topics
            topics_selected.append(_dict_choice[choice])
            no_of_topics_selection -= 1
            print(f"{_dict_choice[choice]} selected!")
            _dict_choice.pop(choice)

    return topics_selected


def curate_question_set(no_of_questions, quiz_dicts): 
    #kwargs is a key, value dict; value is list of key, value pairs
    question_set = {}
    for topic in quiz_dicts.keys():
        question_set[topic] = []
    while no_of_questions > 0:
        random_topic = random.choice(list(quiz_dicts.keys()))
        random_topic_question_ans = random.choice(quiz_dicts[random_topic])
        question_set[random_topic].append(random_topic_question_ans)
        no_of_questions -= 1
        quiz_dicts[random_topic].remove(random_topic_question_ans)
    return question_set



