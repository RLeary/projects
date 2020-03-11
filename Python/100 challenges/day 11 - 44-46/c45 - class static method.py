# Define a class named American which has a static method called
# printNationality.
#
# Hints:
# Use @staticmethod decorator to define class static method.There are also two
# more methods.To know more, go to this link-https://realpython.com/instance-class-and-static-methods-demystified/


class American:
    @staticmethod
    def printNationality():
        print("american")


american = American()
american.printNationality()

American.printNationality()


# Given solution
"""
class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()
"""
