try:

    a=int(input("Enter First Number : "))

    b=int(input("Enter Second Number: "))


    print("+ For Addition\n- For Subtraction\n* For Multiplication\n\ For Division")


    o=input("Enter Your Choice: ")

    match o:
        case "+":
            print(f"Addition is: {a+b}")
        case "-":
            print(f"Subtraction is: {a-b}")
        case "+":
            print(f"Multiplication is: {a*b}")
        case "+":
            print(f"Division is: {a/b}")
        case _:
            print("Invalid Choice Choose Only: +, -, *, /")
except Exception as e:
    print("Enter a Valid Value Of A and B")
