# Define a class, which have a class parameter and have a same instance
# parameter.
#
# Hints:
# Define an instance parameter, need add it in __init__ method.You can init an
# object with construct parameter or set the value later


class MyClass:
    name = "MyClass"

    def __init__(self, name=None):
        self.name = name


object_one = MyClass()
object_two = MyClass("object_two")

print("%s has name %s" % (MyClass.name, object_one.name))
print("%s has name %s" % (MyClass.name, object_two.name))

# given solution
"""class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))
"""
