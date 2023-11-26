a=10
b=20
try:
    c=b/a
except:
    print("cannot divide by zero")
else:
    print(c)
finally:
    print("exception handling")
