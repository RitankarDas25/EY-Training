try:
    value = int(input("Enter a number: "))
    print(10/value)
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("finally")