a = input("Enter the number:")
print(f"multypication table of {a} is")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a*i)}")
except ValueError:
    print("error 404 not found")


print("End of program")