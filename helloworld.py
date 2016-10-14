'''The program asks for a string input, and welcomes the person, or welcomes the world if nothing was given.'''

def inputname():
    '''Keeps asking until a string is inputted'''
    while True:
        try:
            name=input("Please enter your name!")
            int(name)
            print("This is not a string! Please enter a string")
        except ValueError:
            return name
            


def greeting(name):
    '''Greets the person, depending on the name'''
    if not name:
        print("Hello World!")
    else:
        print("Hello " + str(name) + "!")

greeting(inputname())