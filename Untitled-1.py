def fun1():
    try:
        l = [1, 22, 72, 871, 17, 817]
        i = int(input("Enter the index"))
        print(l)
        print(i)
    except:
        print("something wrong")
    finally:
        print("iam always executed")
x = fun1
print(x)