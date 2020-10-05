#coding utf-8

print(" I am a modudle_test.py and my name is: " + __name__)

def function1():
    print("Hi I am inside function1.")

print("Calling function....")

if __name__ == '__main__':
    print("calling function1 - only if I am __main__ ...")
    function1()