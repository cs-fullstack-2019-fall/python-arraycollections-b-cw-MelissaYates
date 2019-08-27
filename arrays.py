# # python-arrayCollections_b-cw
#
# ### Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
#
#     b) Print the size of the array
#
# c) Delete the second element.
#
#     d) Print the 3rd element.
#
def problem1():
    variableBelow()

def variableBelow():
    arrayForProblem1 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem1[2])
    print(len(arrayForProblem1))
    del arrayForProblem1[1]
    print(arrayForProblem1)
    print(arrayForProblem1[2])

#     ### Problem 2:
#     ##### We will keep having this problem until EVERYONE gets it right without help
#     Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
#
def repeat():
     userInput = ''
     while userInput != 'q':
        userInput = input("Enter a string. Enter 'q' to quit ")
# ### Problem 3:
# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
# ```
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# ```
# a) Print the collection
#
# b) Print William's nickname
#
# ### Problem 4:
# Create an array of 5 numbers. <strong>Using a loop</strong>,
# print the elements in the array reverse order. <strong>Do not use a function</strong>
#
arrayOfNumbers = [1,2,3,4,5]
for x in arrayOfNumbers:
    reverseArray =arrayOfNumbers [::-1]
    print(reverseArray)
# ### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def numArray():
    arrayNums = [3, 5, 8, 9, 15]
    userInput = int(input("Enter a number"))
    for x in arrayNums:
        if userInput < x:
            print(x)
        elif userInput > x:
            print(x)
        elif userInput == x:
            print("Equal to number in array")


def main():
    problem1()
    repeat()
    numArray()

main()