def great():
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today")


great()


# function that allow input
def great_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


great_me = input("Enter your name: ")
great_with_name(great_me)


# function with more input
def great_with(name, location):  # AVOID POSITION ARGUMENTS
    print(f"Hello {name}")
    print(f"what is it like in {location}")


great_with("Washington", "Lsikipia")


# tO AVOID POSITION argument we use key argument
def my_function(a, b, c):
    print(f"{a} and {b} and {c}")


my_function(c=3, b=8, a=10)



#
