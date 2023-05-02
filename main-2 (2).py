# Olivia Franczyk
# I am writing a program based on my lifting schedule and implementing
# my weight and different days of muscle groups

print("Hey Olivia!", end=" ")
print("Time to go lift!")


def intro():
    while True:
        # standard iterative structures
        try:
            weight = float(input("About how much do you weigh today?"))
            weight = weight // 1
            # use of //
            # did this to get a whole number rather than a possible decimal
            if (weight > 160) or (weight == 160):
                # use of boolean operators
                weight = weight
                cardio(weight)
                break
            elif (weight <= 111):
                print("I am sorry!", "You seem pretty under-weight!", "Lets focus on more protein intake!", sep=' ')
                print("Press 2 for the next question")
                break
            else:
                print("Great!lets move on", '.' * 3)
                # use of *
                moveOn(weight)
                break
        except:
            print("Oops!Invalid Entry!Please try again!")


def moveOn(weight):
    while True:
        try:
            print("Time to pick today's workout <3")
            print("Please select one of the options below:")
            print("Type a 1 for Legs:")
            print("Type a 2 for Back:")
            print("Type a 3 for Biceps:")
            print("Type a 4 for Chest:")
            print("Type a 5 for Triceps & Shoulders")
            print("Type a 6 for a Cardio Session")
            print("Type a 7 for a Core Session")
            decidedGroup = int(input())
            if (decidedGroup == 1):
                legs()
                break
            elif (decidedGroup == 2):
                back()
                break
            elif (decidedGroup == 3):
                biceps()
                break
            elif (decidedGroup == 4):
                chest()
                break
            elif (decidedGroup == 5):
                trishould()
                break
            elif (decidedGroup == 6):
                cardio()
                break
            elif (decidedGroup == 7):
                core()
                break
            else:
                print("Invalid Entry! Don't try to get out of this workout! Try again!")
                continue
        except:
            print("Invalid Entry! Don't try to get out of this workout! Try again!")


def legs():
    print("You have selected a Leg workout!")
    while True:
        try:
            print("Please select a 1 for Strength or a 2 for Tone")
            strengthOrTone = int(input())
            if (strengthOrTone != 1) and (strengthOrTone != 2):
                print("Try again")
                continue
            elif (strengthOrTone == 1):
                print("You have selected Strength!")
                print("Get excited to build some muscle!")
                strengthLegs()
                break
            else:
                toneLegs()
                break
        except:
            print("Invalid Entry please try again")


def strengthLegs():
    print("Today is going to consist of mostly compound lifts!")
    while True:
        try:
            squatweight = float(input("How much weight are you willing to Squat?"))
            if (squatweight < 155) and (squatweight >= 0):
                # use of relational operators
                strengthlegslist = open('strengthlegs.txt')
                for index in range (1,8):
                    sl= strengthlegslist.readline()
                    print(str(index) + ". ", sl)

                break
            # use of if,elif,else
            elif (squatweight >= 155):
                strengthenlegslist=open('strengthenlegs.txt')
                for index in range (1,8):
                    sll=strengthenlegslist.readline()
                    print(str(index) + ". ", sll)

                break
            else:
                print("Invalid Entry please try again!")
                continue
        except:
            print("Invalid Entry please try again!")


def toneLegs():
    print("You have selected Toning of Legs")
    toninglegslist = open('toninglegs.txt')
    for index in range(1, 6):
        tl = toninglegslist.readline()
        print(str(index) + ". ", tl)

def back():
    print("Time for a Back workout!")
    backlist = open('back.txt')
    for index in range(1, 8):
        b = backlist.readline()
        if len(b) >= 10:
            print(b.rstrip())


def biceps():
    print("Time for a Bicep workout!")
    biceplist=open('bicep.txt')
    for index in range(1,6):
        bi=biceplist.readline()
        print(str(index) + ". ", bi)

def chest():
    print("Time for a Chest workout!")
    chestlist=open('chest.txt')
    for index in range(1,4):
        c=chestlist.readline()
        print(str(index) + ". ", c)

def trishould():
    print("Time for a Tricep & Shoulder workout!")
    trishouldlist=open('trishould.txt')
    for index in range(1,5):
        t=trishouldlist.readline()
        print(str(index) + ". ", t)

def core():
    print("Time for a Core workout!")
    corelist=open('core.txt')
    for index in range(1,5):
        co=corelist.readline()
        print(str(index) + ". ", co)

def cardio():
    print("Time for a Cardio workout!")
    cardiolist=open('cardio.txt')
    for index in range(1,4):
        ca=cardiolist.readline()
        print(str(index) + ". ", ca)

def done():
    print("Program is complete")

def again():
    while True:
        answer = int(input("Would you like to do another workout or series of lifts? Type 1 for yes and 2 for no"))
        try:
            if (answer != 1) and (answer != 2):
                # use of relational operators
                # use of boolean operators
                print("Please try again!")

            elif (answer == 1):
                print("yes")
                intro()
                break
            else:
                print("No")
                break
        except:
            print("invalid try again")


def cleanup():
    print("Thank you for having a great workout today!")
    print("Below is a few things I could not include from the rubric")
    a = 5
    b = -5
    print("a >> 1=", a >> 1)
    print("b >> 1=", b >> 1)
    a = 2
    b = -5
    print("a << 1=", a << 1)
    print("b << 1=", b << 1)


def main():
    intro()
    again()
    cleanup()
    done()

if __name__=='__main__':
    main()
