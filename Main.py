"""My Integration Project is a Math Quiz Game."""
__author__ = "Esperandieu Alfred"
# Esperandieu Alfred
# I will be creating a quiz game with math
# I received helped from Andrew Krup
# Andrew help explaining the try and except functions.
# a code that is not very obvious is the try and accept functions.
# codes that I used that isn't obvious is the "if function",sep,end functions.
# I use this video for ideas and implementing the codes
# https://www.youtube.com/watch?v=myJ36xIR7Yg
# https://www.w3schools.com
# Introducing my topics, examples, quiz and string literals.
""" Using the Main def function to introduce a list of def function and
    other function to pass."""


def main():
    """ This is my Primary function to define functions and passing
    arguments. Also, you can say is my dictionary for the def
    functions."""
    welcome()
    name = 10
    nom = 5
    sum_of_addition(name, nom)
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19,
                20, 21, 22, 23, 24, 25]
    print(num_list)
    sample_name(11, 15)
    age = 22
    calculating_age(age)
    # game = 10
    # price = 15
    game_price()


"""The purpose of this function is to introduce to the reader about my
    quiz game. Also, the examples that is included in the quiz game and 
    answering the questions. At the end, you get a grade to see if you 
    understand the math functions."""


def welcome():
    """Introducing to the reader how beneficial this quiz game is to
understanding basic operators and functions."""
    print("welcome \n to my awesome class")
    print("Using this game, you will gain better understanding of the"
          "operators.")
    print("Using parameter, not, or, and operators")
    print("I used string literals")
    print("Using different operators and loops")
    print("using def to call functions")
    # Using the while loop to create true with is equal to each other.

    print("imputing a simple while loop")
    while True:
        try:
            name = int(input("Please enter a code to begin the quiz: "))
            code = ""
            print("Great! let's begin")
            break
        except ValueError:
            print("Wrong Answer. Try Again. Use Numbers")
    print(code and name)
    # I used the "not" equal operator to determine whether x is equal to y.
    input("is the following equation below equal to each other? \n(X != Y)")
    nom1 = input("Is it True or False: ")
    v = 8
    c = 9
    print(v != c)
    print(nom1)


# Another example of using parameter, giving the argument a name and passing
# the argument.


""" I am using the def function with the parameter to pass the argument. 
Letting the user answer the questions either true or false."""


def sum_of_addition(name, nom):
    """Letting the user figure out whether the function print out a True or
    False function. By typing in either true or false and it will tell you
    the correct answer after pressing Enter."""
    print(name + nom)
    # using the "and" operator to test whether the statement is True or False
    # I received help from www.w3schools.com
    print("Determine whether the statement using And is correct? "
          "\n(r > 8 and r < 11)")
    print("Is it True or False: ")
    r = 10
    print(8 < r < 11)
    # I am using the "Or" operator to determine if the statement is True
    # or False.
    # I received help from www.w3schools.com with the following question.
    print("what is the output of the (Or) operator?")
    print("(t > 6 or t < 8)")
    input("Is it True or False: ")
    t = 9
    print(t > 6 or t < 8)
    # using a not operator to determine whether the statement is True or False
    # I receive help from www.w3schools.com.
    print("Is the Not operator use properly? ")
    t = 9
    input("not(t < 15 and t<20)")
    input("Is it True or False: ")
    print(not (t < 15 and t < 20))
    # It only print MLB out of the list.
    input("Next example using for loops.")
    print("['NBA','FIFA', 'MLB', 'NFL']")
    # The for in range will be printing numbers starting from 1 to 3.
    none = ['NBA', 'FIFA', 'MLB', 'NFL']
    input("what order will the sports will they be?: ")
    for name in none:
        print(name)
    if name == 'NFL':
        print("MlB")
    # prompting the user to find the range of numbers starting from 1
    # ending in 25.
    input("Adding for in range loop.")
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19,
                20, 21, 22, 23, 24, 25]
    print(num_list)
    for num in range(1, 5, 25):
        # with the for loop it will print out all the numbers in between
        print(num)


# using a while loop with inner and our loop.
""" For this function I am using a while loop to determine the inner and 
outer loop functions. Also, to prompt the user of correct answer."""


def sample_name(name1, name2):
    """With the def function I was able to prompt the user of the correct
       answer and prompt them to enter an answer."""
    # using the def function of parameter to find the sample name. Also,
    # prompting the user the correct answer.
    input("example of parameter")
    answer = name1 + name2
    print('nom1 is', name1)
    print(answer)
    # sampleName(11, 15)
    print("Great job, on getting the right answer!")
    # printing the lists of colors in 6 rows and column's.
    # prints all the colors in the lists
    colors = ['red', 'blue', 'orange', 'black', 'yellow', 'white', 'brown']
    for colors in colors:
        print(colors)
    # I used the string literal and multiply to find the total of shoes1.
    nike1 = 10
    nike2 = 11
    shoes1 = (nike1 * nike2)
    # using total of nike1 multiply by nike2
    print("total cost of shoes1: ", shoes1)


""" Using the def function to calculate a name and list other examples 
using strings."""


def calculating_age(age):
    """I was able to prompt the user of the age, creating new lines and
        includes "sep arguments"."""
    # age = 22
    # calculating_age(age)
    # I used the end arguments and creating new lines.
    print("An example of using end argument and with a string")
    print("Using the end argument")
    print("How old am I?", age)
    print("this quiz game is easy and understandable ", end=". ")
    print("\n")
    print("an example of using the while true, using 'try and except' before "
          "the actual quiz.")
    # calculating_age(age)
    # Using the while true statement to prompt the user to input an answer.
    # It will also print in Excellent if you do it right.
    num1 = 'Excellent!'
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("wrong answer. try again! type in a whole number. ")
    print(num1, num)


# I am using the while true statement to generate a whole number.
# Also while rejecting any letters and decimals.

# I used the sep argument to determine the final price which is $150.00 with
# 2 decimals places.
"""Using the def function to calculate the gaming price."""


def game_price():
    """With the def function I was able to format the answer from final
       price to two decimals."""
    input("An example of using the sep argument and formatting new lines. ")
    game = 10
    price = 15
    final = game * price
    print("final: $", format(final, "0.2f"), sep='')
    answer = ''
    score = 0
    # game_price(price)
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
        # using elif instead of typing "a" you can type in "Espe"to get
        # the answer.
        score += 1
        print("correct!")
        print("score: ", score)
        print("\n")
    else:
        # If everything fails it will prompt you the correct answer.
        print("Incorrect! The answer is Espe.")
        print("Score: ", score)
        print("\n")
    # Question 2
    # Using the variable with the operator to add 100 and 100 to get 200 for
    # the
    # answer
    print("Question 2.")
    answer2 = input("Solve The Addition?\n100 + 100 \na. 150 \nb. 201 \nc. "
                    "200"
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
        # If you type in the wrong answer is will prompt you the correct
        # answer.
        print("Incorrect! The answer is 200.")
        print("Score: ", score)
        print("\n")
    # question3
    # I use the variables to ask the question and then subtract 25 by 10
    # to get 15.
    print("Question 3.")
    answer3 = input("Solve the Subtraction?\n25 - 10 \na. 16 \nb. 15 \nc. 17 "
                    "\nAnswer: ")
    if answer3 == "b":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    elif answer3 == "15":
        score += 1
        print("Correct!")
        print("Score: ", score)
        print("\n")
    else:
        print("Incorrect! The answer is 15. ")
        print("Score: ", score)
        print("\n")
    # Question4
    # I use the variable to ask a question using the multiplication function
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
    # Question5
    # I use the division operator to solve for the answer
    # by doing seventy five divided by five to get fifteen.
    print("Question 5.")
    answer5 = input("Solve The Division?\n75 / 5 \na. 15 \nb. 16 \nc. 14 "
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
    # Question 6
    # I used the modules to find the reminder for twenty nine divided by 3
    # and get the remainder of 2.
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
    # Question 7
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
    # Question 8
    # I use the floor division to find the to find the largest integer between
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
    # Final Message
    if score <= 2:
        print("final score is:", score, "-Failed!")
    print("\n")
    if score == 5:
        print("final score is:", score, "-Good Job!.")
    else:
        print("final score is:", score, "-Great Job!")


main()
