char = input("enter your character")



match(char.lower()):
    case "a" | "i" | "o" | "u" | "e":
        print(char , "is a vowel")
    case _:
        print(char , "not a vowel")
    