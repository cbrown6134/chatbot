# PyChat 2K17

import random

def start():
    print("  _    _      _ _          _____ _             _______ _                                 ______    _ _                 ")
    print(" | |  | |    | | |        |_   _( )           |__   __| |                               |  ____|  | (_)                ")
    print(" | |__| | ___| | | ___      | | |/ _ __ ___      | |  | |__   ___  _ __ ___   __ _ ___  | |__   __| |_ ___  ___  _ __  ")
    print(" |  __  |/ _ \ | |/ _ \     | |   | '_ ` _ \     | |  | '_ \ / _ \| '_ ` _ \ / _` / __| |  __| / _` | / __|/ _ \| '_ \ ")
    print(" | |  | |  __/ | | (_) |   _| |_  | | | | | |    | |  | | | | (_) | | | | | | (_| \__ \ | |___| (_| | \__ \ (_) | | | |")
    print(" |_|  |_|\___|_|_|\___(_) |_____| |_| |_| |_|    |_|  |_| |_|\___/|_| |_| |_|\__,_|___/ |______\__,_|_|___/\___/|_| |_|")

def end():
    print("  _______    _ _      _                              _       _            ")
    print(" |__   __|  | | |    | |                            | |     | |           ")
    print("    | | __ _| | | __ | |_ ___    _   _  ___  _   _  | | __ _| |_ ___ _ __ ")
    print("    | |/ _` | | |/ / | __/ _ \  | | | |/ _ \| | | | | |/ _` | __/ _ \ '__|")
    print("    | | (_| | |   <  | || (_) | | |_| | (_) | |_| | | | (_| | ||  __/ |_  ")
    print("    |_|\__,_|_|_|\_\  \__\___/   \__, |\___/ \__,_| |_|\__,_|\__\___|_(_) ")
    print("                                  __/ |                                   ")
    print("                                 |___/                                    ")

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "You may be onto something",
                 "I don't agree with you",
                 "It's probably not your fault",
                 "Does it even matter?"]

    return random.choice(responses)

def get_question_response():
    responses = ["Huh?",
                 "I don't know?",
                 "I have no idea?",
                 "Do you really want me to answer that...",
                 "Ask a less stupid question please.",
                 "The simplest answer is most often correct.",
                 "Just remember to always try your best."]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    thank_words = ["thanks", "thank you"]
    nature_words = ["beach", "forest", "mountain", "jungle", "woods"]
    season_words = ["season", "seasons", "summer", "autumn", "winter", "spring"]
    weather_words = ["rain", "snow", "wind", "sunny", "cloudy", "windy", "sleet", "hail"]
    hi_words = ["hi", "hello", "hey", "howdy", "hiya", "whaddup"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif statement[-1] == "?":
        response = get_question_response()
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, thank_words):
        response = "Your welcome."
    elif has_keyword(statement, nature_words):
        response = "I love nature. The beach, the mountains, the woods, et cetera."
    elif has_keyword(statement, weather_words):
        response = "The weather has been wonky recently."
    elif has_keyword(statement, season_words):
        response = "My favorite season is autumn."
    elif has_keyword(statement, hi_words):
        response = "Hola"
    elif len(statement) == 0:
        response = "You have to say something"
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Say something to me!")

    while talking:
        statement = input(">> ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()

