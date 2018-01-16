def a_function():
	print("some thing!!!")

def empty_function():
	pass

def submit(a=1, b=2):
	return a-b

#To get infinite arguments, use *args 
#and for infinite keyword arguments, use **kwargs
def many(*args, **kwargs):
    print(args)
    print(kwargs)

#global
def function_a():
    global a
    a = 1
    b = 2
    return a+b

def function_b():
    c = 3
    return a+c


many(1, 2, 3, name="Mike", job="programmer")
print(submit())
print(submit(b=4, a=5))
print(function_a())
print(function_b())

