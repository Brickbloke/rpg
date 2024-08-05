import os

print("hello monsters")
string = input("would you like to say something?")

print(string)
run = True
menu = True
play = False
rules = False

hp = 50
atk = 3
def clear():          #clears os keeps terminal clean
    os.system("cls") 
def draw():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def save():            #saves the game
    list = [
        name,
        str(hp),
        str(atk)
    ]
    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close
    
while run:
    while menu:
        clear()
        print("1, New Game")
        print("2, load game")
        print("3, rules")
        print("4, quit game")
    
        if rules:
            print("im the boss now these are the rules")
            rules = False
            choice = ""
            input(".... ")
            menu = False
            play = True
        else: 
            choice = input("c..")
        if choice == "1":
            clear()
            name = input("what will be your name?")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt" , "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            hp = load_list[1][:-1]
            atk = load_list[2][:-1]
            # so ur here again. / ("0") / |___| 
            print("*goes into rage mode breaks pc*")
            print("ok then.... " + name + " lets continue.")
            input(".... ")
            menu = False
            play = True
            
        
        elif choice == "3":
            rules = True 
        elif choice == "4":
            quit()
        
    while play:
        save()         #autosaves the game
        
        clear()
        draw()
        print("0 - save and quit")
        draw()
        
        dest = input("-> ")
        
        if dest == "0":
            play = False
            menu = True
            save()
