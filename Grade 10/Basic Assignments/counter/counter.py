counter = 0

def counting():
    global counter

    if counter != 5:
        counter += 1

    else:
        counter = 0

while True:
    prompt = input("{0}\nPress Enter or 'q' to quit.\n".format(counter))
    if prompt == "":
        counting()
    elif prompt == "q":
        break
    else:
        print("\nInvalid Key\n")
