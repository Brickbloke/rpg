print("hello monsters")
string = input("would you like to say something?")

print(string)
run = True
menu = True
play = False
rules = False

hp = 50
atk = 3

def save():
    list = [
        name
        str(hp)
        str(atk)
    ]
    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
while run:
    while menu:
        print("1, New Game")
        print("2, load game")
        print("3, rules")
        print("4, quit game")

    if rules:
        print("im the boss now these are the rules")
        rules = False
        choice = ""
        input(".... ")
    else: 
        choice = input("c..")
    if choice == "1"
        name = input("what will be your name?")
        menu = False
        play = True
    elif choice == "2":
        pass    