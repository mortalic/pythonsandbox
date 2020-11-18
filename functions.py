def my_function():
    print("hello from my function")

def my_function_with_args(username, greeting):
    print("Hello, %s , from my function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("John", "a great year")

x = sum_two_numbers(1,2)

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "more readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()