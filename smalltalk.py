def smalltlk():
    wthr = ""
    wthr = input("\nWhat is the weather like in your city: ")

    sport = ""
    sport = input("What is your favorite sport to watch: ")

    food = ""
    food = input("How about food, what is you favorite food: ")

    if len(wthr) == 0:
        print("\n[ Whatever the weather like, I am sure you are used to it!")
    elif len(wthr) > 0:
        print("\n[ Oh so the weather in your city is {}, I did not know that!".format(wthr))

    if len(sport) == 0:
        print("Most people have a certain sport they like to watch, I am sure you do too!")
    elif len(sport) > 0:
        print("Oh I see, so the sport you like to watch is {}! my uncle Ben and aunty Marrie like it too!".format(sport))

    if len(food) == 0:
        print("I'm sure you have a good taste in food! ]")
    elif len(food) > 0:
        print("So you do like {}? no way, my sister and my father like it too! "
              "They go out every weekend together to get some {} ]".format(food,food))

