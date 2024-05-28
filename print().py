from unittest import result


operator = __import__("Enter an operator(+ - * /): ")
num1 = float(__import__  ("Enter the 1st number: "))
num2 = float(__import__  ("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    print(f"{operator} is not a valid oparation")