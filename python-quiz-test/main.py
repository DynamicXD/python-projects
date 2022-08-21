def oddeven(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a Number: "))
print("The Number is ", oddeven(num))
