l = list((234,23,4,23,"FASDFH", 234.34))

try:
    print(l[2])
    print(x)
    print(l[234])
except IndexError:
    print("IndexError")
except Exception as e:
    print("Error: ", e)
else:
    print("Good, No error found!")
finally:
    print("Executed!")
