print("----SCIENTIFIC CALCULATOR----")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Square root\n7.Exponential\n8.Sine\n9.Cosine\n10.Tangent\n11.Radian to Degree\n12.Degree to Radian\n13.Exit")
import math
ch="y"
while ch!="13":
    a = int(input("Choose your option:"))
    if a==1:
        print("Addition")
        a1=float(input("Enter your First Number:"))
        b1=float(input("Enter your Second Number:"))
        print("Answer=",a1+b1)
    if a==2:
        print("Subtraction:")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 - b1)
    if a == 3:
        print("Multplication")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 * b1)
    if a == 4:
        print("Division")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 / b1)
    if a == 5:
        print("modulus")
        a1 = float(input("Enter your First Number:"))
        b1 = float(input("Enter your Second Number:"))
        print("Answer=", a1 % b1)
    if a == 6:
        print("Square root")
        a1 = int(input("Enter your Number:"))
        print("Answer=", a1 ** 0.5)
    if a == 7:
        print("Exponential")
        a1 = int(input("Enter your First Number:"))
        b1 = int(input("Enter your Second Number:"))
        print("Answer=", a1 ** b1)

    if a == 8:
        print("sine")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.sin(a1))

    if a == 9:
        print("cosine")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.cos(a1))
    if a == 10:
        print("tangent")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.tan(a1))
    if a == 11:
        print("Radian to Degree")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.radians(a1))
    if a == 12:
        print("Degree to Radian")
        a1 = float(input("Enter your Number:"))
        print("Answer=",math.degrees(a1))












