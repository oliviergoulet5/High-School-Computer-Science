if dog_moves[0] in wantToForget.lower():
            print("You've unlearned {0} and replaced it with {1}.".format(dog_moves[0]))
        elif dog_moves[1] in wantToForget.lower():
            print("Want to forget Move 2")
        elif dog_moves[2] in wantToForget.lower():
            print("Want to forget Move 3")
        else:
            print("Get out of my store, nerd!")
