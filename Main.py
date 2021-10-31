#Esperandieu Alfred
#I will be creating a quiz game with math
#I received helped from Andrew Krup
#A code that I used that isn't obvious is the "if function",sep,end functions.
#I use this video for ideas and implimenting the codes
# https://www.youtube.com/watch?v=myJ36xIR7Yg
#https://www.w3schools.com

#Introducing my topics, examples, quiz and string literals.
def main():
    input("welcome to my awesome class")
    input("Using this game, you will gain better understanding of the"
          "operators.")
    input("Using parameter, not, or, and operators")
    input("I used string literals")
    input("Using different operators and loops")
    input("using def to call functions")
# Using if and else loops to give condition to the function.
    game = input("would you like to play a quiz game: ")
    if game == "yes":
        print("great!,lets begin")
    else:
        print("okay!")
# Using the while loop to create a code with a true or false statement.
    answer = True
# Given the condition is true, write the same code for both it will be True.
    while answer:
        code1 = input(" Type in a password to play: ")
        code2 = input("Type in another password to play: ")
    if code1 == code2:
        print("Correct code!")
        answer = False
        quit()
    else:
        print("Wrong code")
        quit()
#With false condition if codes entered incorrectly, it will output"Wrong code".
def determine_nom1(nom1):
# I used the not equal to operator to determine whether x is equal to y.
    input("is the following equation below equal to each other? \n(X != Y")
    input("Press Enter to answer ")
    nom1 = input("True or False: ")
    nom1 = True
    v = 8
    c = 9
    print(v != c)
    determine_nom1(nom1)
#Another example of using parameter, giving the argument a name and passing
# the argument.
import math
def sumofaddition(name,nom):
    name = 10
    nom = 5
    print(name+nom)
    sumofaddition(name,nom)
# using the and operator to test whether the statement is True or False
#I received help from www.w3schools.com
def functionoftestsr(r):
    input("Determine whether the statement using And is correct? "
            "\n(r > 8 and r < 11)")
    input("Press Enter to answer")
    input("True or False: ")
    r = 10
    print(r > 8 and r < 11)
# I am using the Or operator to determine if the statement is True or False.
#I received help from www.w3schools.com with the following question.
def funtionoftestt(t):
    print("what is the output of the (Or) operator?")
    input("(t > 6 or t < 8)")
    input("Press Enter to answer")
    input("True or False: ")
    t = 9
    print(t > 6 or t < 8)
    funtionoftestt(t)
#using a not operator to determine whether the statement is True or False
def solvingfortt(t):
#I receive help from www.w3schools.com.
    print("Is the Not operator use properly? ")
    t = 9
    input("not(t < 15 and t<20)")
    print("type in your response below")
    input("True or False: ")
    print(not(t < 15 and t<20))
    solvingfortt(t)
def listofsports(none):
#It only print MLB out of the list.
    input("Next example using for loops.")
    print("['NBA','FIFA', 'MLB', 'PGA']")
# The for in range will be printing numbers starting from 1 to 3.
    none = ['NBA','FIFA', 'MLB', 'PGA']
    input("what will be in range of the four sports?: ")
    for name in none:
        print(name)
    if name == 'MLB':
        print("MlB")
    listofsports(none)
def calculatingnum_list(num_list):
#prompting the user to find the range of numbers starting from 1 ending in 25.
    input("implemeting for in range loop.")
    num_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25]
    for num in range(1,25):
    #with the for loop it will print out all the numbers in between
        print(num)
    calculatingnum_list()
# using a while loop with inner and our loop.
def sampleName(name1, name2):
#using the def function of parameter to find the sample name. Also,
# prompting the user the correct answer.
    input("example of parameter")
    answer = name1 + name2
    print('nom1 is', name1)
    print(answer)
    sampleName(11,15)
    print("Great job, on getting the right answer!")
#printing the lists of colors in 6 rows and colums.
def listofcolors(colors):
#prints all the colors in the lists
    colors =['red','blue','orange','black','yellow','white','brown']
    for x in colors:
        print(colors)
    listofcolors("colors")
# I used the string literal and multiply to find the total of shoes1.
def costofshoes(shoes):
    nike1= 10
    nike2= 11
    shoes1=(nike1 * nike2)
#using total of nike1 multiply by nike2
    print("total cost of shoes1: ", shoes1)
    costofshoes(shoes)
def calculatingAge(age):
    age = 22
#I used the end arguement and creating new lines.
    input("An example of using end argument and \n with a string")
    print("Using the end argument")
    print("How old am I?", age)
    print("this quiz game is easy and understandable " , end = ". ")
    print("\n")
    print("lets begin with the examples first", end = ". ")
    print("\n")
    print("Using the sep argument")
    calculatingAge(age)
#I used the sep argument to determine the final price which is $150.00 with
# 2 decimals places.
def gameprice(price):
    input("An example of using the sep argument and formating new lines. ")
    game = 10
    price = 15
    final = game * price
    print("final: $", format(final, "0.2f"), sep ='')
    answer = ''
    score = 0
    gameprice(price)
# I use the variables to create a string to display the question
# what is your name and the answer is Espe.
    print("Question 1.")
    answer1 = input("What Is Your Name? \na. Espe \nb. Espi \nc.Espy "
                    "\nAnswer:  ")
    if answer1 == "a":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    elif answer1 == "Espe":
#using elif instead of typing "a" you can type in "Espe"to get the answer.
        score += 1
        print("correct!")
        print("score: ", score)
        print("\n")
    else:
#If everything fails it will prompt you the correct answer.
        print("Incorrect! The answer is Espe.")
        print("Score: ", score)
        print("\n")
# Question 2
# Using thevariable with the operator to add 100 and 100 to get 200 for the
# answer
    print("Question 2.")
    answer2 = input("Solve The Addition?\n100 + 100 \na. 150 \nb. 201 \nc. 200"
                "\nAnswer: ")
    if answer2 == "c":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
# using elif as another way of answering instead of using "c" do "200".
    elif answer2 == "200":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
#If you type in the wrong answer is will prompt you the correct answer.
        print("Incorrect! The answer is 200.")
        print("Score: ", score)
        print("\n")
#question3
#I use the variables to ask the question and then subtract 25 by 10 to get 15.
    print("Question 3.")
    answer3 = input("Solve the Subtraction?\n25 - 10 \na. 16 \nb. 15 \nc. 17 "
               "\nAnswer: ")
    if answer3 == "b" or answer == "15":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 15. ")
        print("Score: ", score)
        print("\n")
#Question4
#I use the variable to ask a question using the multiplication function
# and i did 6 times 5 to get thirty for the answer.
    print("Question 4.")
    answer4 = input("Solve The Multiplication?\n6 * 5 \na. 29 \nb. 31 \nc. 30"
                "\nAnswer: ")
    if answer4 == "c" or answer == "30":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 30. ")
        print("Score: ", score)
        print("\n")
#Question5
# I use the dividion operator to solve for the answer
# by doing seventy five divided by five to get fifteen.
    print("Question 5.")
    answer5=input("Solve The Division?\n75 / 5 \na. 15 \nb. 16 \nc. 14 "
                  "\nAnswer: ")
    if answer5 == "a" or answer == "15":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 15. ")
        print("Score: ", score)
        print("\n")
#Question 6
# I used the modules to find the reminder for twenty nine divided by 3
# and get the remeainder of 2.
    print("Question 6.")
    answer6 = input("Solve The Modules?\n29 % 3 \na. 1 \nb. 2 \nc. 3 "
                    "\nAnswer: ")
    if answer6 == "b" or answer == "2":
        score += 3
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 15. ")
        print("Score: ", score)
        print("\n")
#Question 7
# I use the exponentiation operator to find the two to the seven power
# and get an answer of hundred twenty eight.
    print("Question 7.")
    answer7 = input("Solve The Exponentiation?\n2 ** 7 \na. 125 \nb. 126 "
    "\nc. 128 "
    "\nAnswer: ")
    if answer7 == "c" or "128":
        score += 3
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 128. ")
        print("Score: ", score)
        print("\n")
#Question 8
# I use the floor dision to find the to find the largest integer between
# 85 and 5.
    print("Question 8.")
    answer8 = input("Solve The Floor Division?\n85 // 5 \na. 17 \nb. 18 "
    "\nc. 16 "
    "\nAnswer: ")
    if answer8 == "17" or "b":
        score += 3
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 17. ")
        print("Score: ", score)
        print("\n")
#Final Message
    if score <= 2:
        print("final score is:", score, "-failed!")
    print("\n")
    if score == 5:
        print("final score is:", score, "-good!.")
    else:
        print("final score is:", score, "-great!")

main()
