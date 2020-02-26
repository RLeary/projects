# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use class, function and comprehension.


class DivisiblebySeven:
    def divisible_by_seven(self, n):
        for number in range(n + 1):
            if number % 7 == 0:
                yield number


divisible = DivisiblebySeven()
gen = divisible.divisible_by_seven(int(input("Enter a number: ")))

for number in gen:
    print(number)

# given solution
"""
class Divisible:
    
    def by_seven(self, n):
        for number in range(n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)
"""
