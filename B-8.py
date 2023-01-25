#if statements
#allow us to make decisions based on specific conditions and actions to take based on
#those set conditions

isMale = True

if isMale:
    print("You are a male")
else:
    print("You are not a male")

isTall = True
if isMale or isTall:
    print("You are a male or tall ot both")
else:
    print("You are neither male or tall")

if isMale and isTall:
    print("You are a tall male")
elif isMale and not(isTall): #not() function negates everything inside the parentheses
    print("You are a short male")
else:
    print("You are either not tall or not a male")

#using if statements and comparisons
def maxnum(num1,num2,num3):
    if num1 >= num2 and num1 >=3:
        print("Max is: " + str(num1))
    elif num2 >= num1 and num2 >= num3:
        print("Max is: " + str(num2))
    elif num3 >= num1 and num3 >= num2:
        print("Max is: " + str(num3))
    else:
        print("Neither is the max")

ch1,ch2,ch3 = input("Enter 3 num: ").split()
x = int(ch1)
y = int(ch2)
z = int(ch3)
maxnum(x,y,z)
