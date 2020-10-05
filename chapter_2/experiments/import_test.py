#coding utf-8

print("I am import_test.py and my name is: " + __name__)

print("importing module_test..")
import module_test


print("calling function1 from within import_test")
module_test.function1()