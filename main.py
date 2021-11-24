"""
how to manipulate strings in Python

"""
my_string = "Sometimes life is unfair"
new_string = my_string.replace("unfair", "fair enough")

print(my_string.find("Sometimes", 1, 20))
print(new_string)
print(new_string.upper())
print(int("78"))
print(int(34.5))
print(ord('g'))
print(bool("hi"))

num_list = [4,5,7,8,9,1,2]

triple_list = map(lambda n: n * 3, num_list)

print(list(triple_list))

numblist = [4, 4,3,7,8,5,6]

less_than_7 = list(filter(lambda  n: n < 7, numblist))
print(less_than_7)