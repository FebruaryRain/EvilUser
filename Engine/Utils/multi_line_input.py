def multi_line_input(prompt=""):
    end = False
    returnString = ""
    while not end:
        try:
            returnString += input(prompt) + "\n"
        except EOFError:
            end = True
            print()
    return returnString.strip()