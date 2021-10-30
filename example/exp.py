# from math import pi
# a = float(input("Nhập a"))
# s = (pi*a**2)/2
# print(f"Diện tích nửa hình tròn là {s:.4f}")

#######################

# from math import sqrt

# h = float(input("Nhập độ cao h: "))
# g = 9.8
# v = sqrt(2*g*h)
# print("Vận tốc khi chạm đất = ", v)

#######################

# loop = 1
# while (loop < 10):
#     noun = input("Choose a noun: ")
#     p_noun = input("Choose a plural noun: ")
#     noun2 = input("Choose a noun: ")
#     place = input("Name a place: ")
#     adjective = input("Choose an adjective (Describing word): ")
#     noun3 = input("Choose a noun: ")
#     print("------------------------------------------")
#     print("Be kind to your", noun, "- footed", p_noun)
#     print("For a duck may be somebody's", noun2, ",")
#     print("Be kind to your", p_noun, "in", place)
#     print("Where the weather is always", adjective, ".")
#     print()
#     print("You may think that is this the", noun3, ",")
#     print("Well it is.")
#     print("------------------------------------------")
#     loop = loop + 1

######################

def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]
while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Viet Nguyen")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, invilid character")
    else:
        break
