#name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

name_args(first_name="Alex",last_name="Aguirre",title="Full Stack Developer")

#all_true - Returns True if all the elements in an iterable are true. 
#Hint: there is an existing built-in function that could be very helpful here
def all_true(*args):
        if len(args)>=1:
            result=all(args)
            if result==True:
                print("All iterables are True")
                return result
            else:
                print("At least one iterables is False")
                return result
        else:
            print("Iterable is Empty, please pass an iterable with one or more values")

all_true(1==1,True,3<5)

#one_true - Returns True if one of the elements in an iterable is true. 
#Hint: there is an existing built-in function that could be very helpful here.<br><br>
def one_true(*args):
    if len(args)>=1:
    
        if any(args)==True:
            print("At lease one value in the arguments is true")
        else:
            print("There are no True arguments")
    else:
        print("Please provide at least one boolean value or experession")
one_true(1>2, 3==3)

#recursive_factorial - Uses recursion to find the factorial of an integer
def recursive_factorial(x):
    if x<1:
        print("Please enter a positive integer")
    elif x==1:
        return x
    else:
        return x*recursive_factorial(x-1)
print(recursive_factorial(3))


#recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
#Input: AABBCCDD
#Output: ABCD

def recursive_deduplicate(my_string):
    if not my_string:
        print("Must pass a string value")
    elif len(my_string)==1:
        return my_string
    else:
        if my_string[0]!=my_string[1]:
            return my_string[0]+recursive_deduplicate(my_string[1:])
        return recursive_deduplicate(my_string[1:])      

print(recursive_deduplicate("AABBCCDD"))

#recursive_reverse - Uses recursion to reverse a string
def recursive_reverse(norm_string):
    if not norm_string:
        return ("You must enter a valid string")
    elif len(norm_string) ==1:
        return norm_string
    else:
        return recursive_reverse(norm_string[1:])+norm_string[0]
       
print(recursive_reverse("Hello Alex Super software developer"))