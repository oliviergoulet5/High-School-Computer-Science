#functions2



def prompting(question):
    prompt = None
    while prompt != "yes" and prompt != 'no':
        prompt = input(question)
        print(" testing prompt var: " + prompt)


prompting("Do you like python? ")

    

