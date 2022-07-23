def greet():
    gret = ""
    gret = input("\nHow are you? ")
    if len(gret) == 0:
        print("\n[ I hope everything is going okay! ]")
    else:
        print("\n[ Thank you for letting me know that you are feeling {} ]".format(gret))
