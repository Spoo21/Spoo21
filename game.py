print('''________________
                   |               |                        |
    
............|..............""""_;;,................|
-----------------|------
Y*$@_(_(@$($*Y@**@$Y@UY@Y*Y@Y**@*&@*$
     (*@@^&&)&@&Y@*
     *&&#&(@())
                     :"::"""":":"""::""
>>>>>>>>                 <<<<<<<<<<<
>>>>>>                     >>>>>>>>>>
                       >>>>>>>>>
            {{{{{{{{}}}}}}}}
+++++++++++++++++
              ---------+++----_________[[[[[]]]]]
?????????????????/|||||
__________//_______________////________
+++++++=======__________________0
''')

print("Welcome to the game puzzle challenge!")

treasure = input("welcome to wekon island. Your mission is to find the hidden trasure. Choose way left or right?: ").lower()
if treasure == "left":
    boat = input("You have come across the lake.Do you want to swim or wait for the boat to reach the other side?: ").lower()
    if boat == "swim":
        print("Game Over. You were eaten by shark!")
    elif boat == "wait":
        door = input("Which door do you want to choose? green, blue or yellow?: ").lower()
        if door == "green":
            print("Game Over. You entered a house full of hyenas!")
        elif door == "yellow":
            print("Game Over. You entered a room that had a sewage hole!")
        elif door == "blue":
            print("Congratulations you found the treasure. You Win!")
else:
    print("Game Over!")

    