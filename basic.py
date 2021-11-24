"""
This chapter 1 from Python Crash course book
"""

#Try it yourself 1

message = "Good morning!"
print(message)

message = "Good night!"
print(message)

name = " ini lovelace "
print(name.title())

name = "Eternal Love"
print(name.upper())
print(name.lower())

first_name = "vivi"
last_name = "Rosita"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

print("Blockchain")
print("\tBlockChain")

print("Languages : \nPython\nJava\nJavaScript")
my_language = "Indonesian "
my_language.rstrip()
print(my_language.rstrip())

sentence = "Python's strengths is its diverse community"
print(sentence)

#Try it yourself 2
name = "Vivi"
message1 = f"Hello {name}, would you like to learn some Python today?"
print(message1)

name1 = "vivi rosita romadhoni"
name2 = name1.lower()
name3 = name1.upper()
name4 = name1.title()

print(name1)
print(name2)
print(name3)
print(name4)

famous_person = "Bretman"
quote = f"{famous_person} once said, 'if there is no turtle, there is no turtle'"
print(quote)

name_asho = '\tAshoka Avalokita \nSri Narendra '
name1_asho = name_asho.lstrip()
print(name1_asho)
name2_asho = name_asho.rstrip()
print(name2_asho)

a = 3
b = 5.0
y = a + b
print (y)

#Try it yourslef3
print( 4+4)

#Try it yourself 4 comment


#Introducing Lists 3
secret_number = ['lea', 'denise', 'zuu', 'dita', 'jinni', 'soodam', 'minji']
print(secret_number[1].title())
print(secret_number[4])
print(secret_number[-4])
print(f"The main dancer of secret number is {secret_number[-4].title()}")

#Try it yourself 1
itzy = ['ryujin', 'chaeyoung', 'yeji', 'lia', 'yuna']
greeting0 = f"hello, I am {itzy[0].title()}"
greeting1 = f"hello, I am {itzy[1].title()}"
greeting2 = f"hello, I am {itzy[2].title()}"
greeting3 = f"hello, I am {itzy[3].title()}"
greeting4 = f"hello, I am {itzy[4].title()}"
print(greeting0)
print(greeting1)
print(greeting2)
print(greeting3)
print(greeting4)

cars = ['jazz', 'picanto', 'xenia', 'lamborghini', 'tesla']
cars.append('innova')
print(cars)
cars.insert(2, 'swift')
print(cars)
del cars[0]
print(cars)

popped_cars =cars.pop()
print(popped_cars)
cars.remove("xenia")
print(cars)

#Try it yourself 2


