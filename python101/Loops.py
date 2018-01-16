
# python 2.x called xrange
# python 3.x changed range
range(4, 10, 2)
# list(range[5, 10, 2])

for number in range(5):
	print(number)

for x in range(1,10):
	print("xrang:%s" % x)

dict = {"one":1, "two":2, "three":3}
for key in dict.values():
	print(key)
for key in dict.keys():
	print(key)

i = 0
while i < 10:
	print(i)
	i = i + 1