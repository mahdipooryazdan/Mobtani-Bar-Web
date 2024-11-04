import random

# Tamarin List
# -------------1-------------
studentList = ["Mohammad","Mahdi" , "Ali" ]

def addStudent():
    while (True) :
        studentName = input("Enter Name Of Student Enter 0 to Finish: ")
        if studentName == "0":
            print(studentList)
            break
        else:
            studentList.append(studentName)

# -------------2-------------
def randomNumber():
    randomListNumber = []
    inputNum = input("Enter Your Number 0:10 : ")
    flag=False
    for x in range(5):
        randomInt = random.randint(0,10)
        randomListNumber.append(randomInt)
    for x in randomListNumber :
        print(x)
        if x == int(inputNum):
            flag = True
    print(flag)

# -------------3-------------
def reverseArray():
    inputArray = []
    while(True):
        inputValue = input("Enter List Value(Enter 0 to Finish): ")
        if inputValue == "0":
            reverseList = inputArray[::-1]
            print("Original: ",inputArray)
            print("Reversed: ", reverseList)
            break
        else:
            inputArray.append(inputValue)
# -------------4-------------
def deleteStudent():
    studentList = ["Mohammad","Javad","Mahdi","Ali","Reza","Seyed" ]
    inputStudentName = input("Enter Student Name: ")
    for x in studentList:
        if x == inputStudentName:
            studentList.remove(x)
            print(studentList)
# -------------5-------------
def mergeList():
    lst1 = []
    lst2 = []
    while (True) :
        lst1Value = input("Enter Value Of List 1 Enter 0 to Finish: ")
        if lst1Value == "0":
            while (True) :
                lst2Value = input("Enter Value Of List 2 Enter 0 to Finish: ")
                if lst2Value == "0":
                    print("List 1 Items: ",lst1)
                    print("List 2 items: ",lst2)
                    lst3 = lst1+lst2
                    print("Merge List: ",lst3)
                    break
                else:
                    lst2.append(lst2Value)
            break
        else:
            lst1.append(lst1Value)
# Tamarin Topple
# -------------1-------------
def favoriteColor():
    colors = ()
    lstColor =[]
    while True :
        inputColor = input("Enter Favorite Color(Enter 0 To Cancel): ")
        if inputColor == "0":
            colors = tuple(lstColor)
            print(colors)
            for x in colors:
                print(x)
            break
        else:
            lstColor.append(inputColor)
# -------------2-------------
def countInTopple() :
    num = (1,2,3,4,5,6,5,7,8,9,10)
    numInput = input("Enter number 1:10 to Check Count: ")
    print(num.count(int(numInput)))
# -------------3-------------
def monthCheck() :
    month = ("Farvardin" , "Ordibehesht", "Tir","Khordad","Mordad","Shahrivar","Mehr","Aban","Azae","Dey","Bahman","Esfand")
    monthInput = input("Enter Month: ")
    for x in month:
        if x == monthInput:
            print("Mah Mored Nazar Peyda Shod")
            break
# -------------4-------------
def averageScore() :
    student_scores = (("mahdi", 16),("Ali", 16),("Mohammad", 16))
    for student in studentList :
        print(student)
# -------------5-------------





# Tamarin If
# -------------1-------------
def evenOrOdd():
    num=input("Enter Your Number: ")
    num=int(num)
    if(num%2==0):
      print ("Your number is Even")
    else:
       print("your number is Odd")
# -------------2-------------
def checkTemp():
   temperature=input("Enter Temperature Your Room: ")
   temperature=int(temperature)
   if(temperature >15):
     print("Your room is Hot")
   else:
      print("Your Room is Cold")
# -------------3-------------
def login():
   userName=input("Enter your User Name : ")
   passWord=input("Enter Your Password: ")
   if(userName=="User"and passWord=="1234"):
      print("You'r Login")
   else:
      print("Enter Current User & Password")
# -------------4-------------
def ageVerify():
   citizen=input("Are You Citizen Of IRAN \"YES\" OR \"NO\":")
   age=input("How Old Are You : ")
   age=int(age)
   if(citizen=="yes" and age>=18):
      print("You Can Vote")
   elif(citizen=="yes" and age<18):
      print ("Your Age is less")
   else:
      print ("Your Not Citizen Of IRAN")
# -------------5-------------
def offer():
   user=input("Are You User :")
   money=input("How Many Use Money $: ")
   money=int(money)
   if(user=="yes" and money>=100):
      print("You Can User This Offer")
   else:
      print("You Cant Use This Offer")

# Tamarin Loop
# -------------1-------------
def printNum():
    for x in range(1,101):
        print(x)
# -------------2-------------
def sumNumber() :
    sum=0
    for x in range (1,51):
        sum+=x
    print(sum)
# -------------3-------------
def mpTable() :
    num = input("Enter Number To Show MP Table: ")
    for x in range(1,11):
        print(x , " * " ,num," = ", x*num )
# -------------4-------------
def factorial():
    num = input("Enter Number To Show Factoriel: ")
    fac = 1
    num1 = int(num)+1
    for x in range(1,num1):
        fac = fac * x
    print(fac)
# -------------5-------------
def sumEven():
    sum = 0
    for x in range(1,100):
        if x % 2 == 0:
            sum = sum + x
    print (sum)
while (True) :
    print("[1] List\n[2] Topple\n[3] If\n[4] For")
    inputNumT = input()
    if inputNumT == "1":
        while (True):
            print("[1] Add Student\n[2] Random Number\n[3] Reverse List\n[4] Remove Student \n[5] Merge List\n[0] Main Menu")
            inputNum = input()
            if (inputNum == "1"):
                addStudent()
            elif (inputNum == "2"):
                randomNumber()
            elif (inputNum == "3"):
                login()
            elif (inputNum == "4"):
                deleteStudent()
            elif (inputNum == "5"):
                mergeList()
            elif (inputNum == "0"):
                break
    if inputNumT == "2":
        while (True):
            print("[1] Favorite Color\n[2] Count in Topple\n[3] Check Month\n[4] Average Score")
            inputNum = input()
            if (inputNum == "1"):
                favoriteColor()
            elif (inputNum == "2"):
                countInTopple()
            elif (inputNum == "3"):
                monthCheck()
            elif (inputNum == "4"):
                averageScore()
            elif (inputNum == "0"):
                break

    if inputNumT == "3":
        while (True):
            print("[1] Even or Odd\n[2] Check Temp\n[3] Month Check\n[4] age Verify for Vote\n[5] Use Offer")
            inputNum = input()
            if (inputNum == "1"):
                evenOrOdd()
            elif (inputNum == "2"):
                checkTemp()
            elif (inputNum == "3"):
                monthCheck()
            elif (inputNum == "4"):
                ageVerify()
            elif(inputNum == "5"):
                offer()
            elif (inputNum == "0"):
                break
    if inputNumT == "4":
        while (True):
            print("[1] Print Number 1:100\n[2] Sum Number 1:50\n[3] MP Table\n[4] Factorial \n[5] Sum Even 1:100")
            inputNum = input()
            if (inputNum == "1"):
                printNum()
            elif (inputNum == "2"):
                sumNumber()
            elif (inputNum == "3"):
                mpTable()
            elif (inputNum == "4"):
                factorial()
            elif(inputNum == "5"):
                sumEven()
            elif (inputNum == "0"):
                break





