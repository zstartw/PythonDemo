
import sys

print(sys.version)

my_string = "welcome!!!"
my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
another_string = 'The bright red fox jumped the fence.'
a_long_string = ''' this is a 
mutil-line stirng. '''

my_string = "abc"
#wrong code
# my_string[0] = "d" 

#python 2.x unicode add
my_unicode_string = u"This is unicode"

#String methods
my_unicode_string.upper()
my_unicode_string.strip()
#get a list of all the string method
dir(my_unicode_string)
#api doc
help(my_unicode_string.capitalize)
# print(type(my_unicode_string))

#string formatting
my_string = "I like %s" % "python"
another_string = "I like %s and %s" % ("Python", "cookies")
my_string = "%i + %i = %i" % (1,2,3)
float_string = "%f" % (1.23)
print(float_string)


