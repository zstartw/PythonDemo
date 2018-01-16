if 1 > 0:
	print("success!!!")
else:
	print("this was false!")


#Boolean Operations
x = 10
y = 20

if x < 10 or y > 15:
    print("This statement was True!")

my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
	print("'x' is not in the list")

# checking for nothing
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if empty_string == "":
	print("this is an empty string!")

if not nothing:
    print("Then it's nothing!")

#Special Characters
print("I have a \n new line in the middle")
print("I have a \ttabbed!!")