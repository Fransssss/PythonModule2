def hello():
    name = ""
    name = input("\nwhat is your name: ")
    if len(name) > 0:
        if name[0].islower():
            name = name.capitalize()
        print("\n[ Hello {}, it is a pleasure to meet you! ]".format(name))

    elif len(name) == 0:
        print("\n[ Hey stranger, It is good to meet you! ]")