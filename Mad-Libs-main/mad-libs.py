def mad_libs():
    print("Welcome to Mad Libs!")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"Today I went to the {place} and saw a very {adjective} {noun}. It {verb} all day long!"

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
