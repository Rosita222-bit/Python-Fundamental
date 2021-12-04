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
dinner_guests =['Lisa', 'jennie', 'Jisoo', 'Rose']
welcome = 'Welcome to our dinner party!'
print(f"{welcome} {dinner_guests[0].title()}")
print(f"{welcome} {dinner_guests[1].title()}")
print(f"{welcome} {dinner_guests[2].title()}")
print(f"{welcome} {dinner_guests[3].title()}")



cancel_guest = 'Rose'
dinner_guests.remove(cancel_guest)
print(dinner_guests)

dinner_guests.append('Seulgi')
print(dinner_guests)
dinner_guests.insert(1, 'Irene')
print(dinner_guests)

dinner_guests.insert(0, 'Joy')
print(dinner_guests)
dinner_guests.insert(-1,'yujin')
print(dinner_guests)
new_dinner_guests = dinner_guests.pop()
print(new_dinner_guests)
print(dinner_guests)

#Shrinking guest list
print(f"Sorry, we can only invite {dinner_guests[0].title()} and {dinner_guests[1].title()}")
dinner_guests.pop(0)
dinner_guests.pop(1)
print(f"Waiting lists : {dinner_guests}")

#Sorting a list with sort() method
menus = ['toppoki', 'seblak', 'cimol', 'samgyeopsal', 'ayam betutu']
menus.sort()
print(f'the menu : {menus}')
menus.sort(reverse=True)
print(menus)

#sorted() function
print(f"SORTED() FUNCTION")
print(f"Here is the original list:{menus}")
print("\nHere is the sorted list:")
print(sorted(menus))
print("\nHere is the original list again:")
print( menus)
print(len(menus))

#Try it yourself 3
dream_place = ['london', 'seoul', 'tokyo', 'sydney', 'new zealand']
print(dream_place)
dream_place.sort(reverse=True)
print(dream_place)
print(sorted(dream_place))
print(dream_place)
print(len(dream_place))

#Avoiding Index Errors
print(f'Last place :{dream_place[-1]}')

#working with list chapter 4
print("\n-------------Working with Lists-----------------")
marketPlaces = ['tokopedia', 'shopee', 'bibli', 'lazada', 'jdid']
for m in marketPlaces :
    print(m)

for m in marketPlaces :
    print(f'{m.title()}, is a great marketplace in Indonesia!')
    print(f' I would love to shop in {m.title()}\n')

nama_ayam = ['geprek', 'taliwang', 'betutu', 'kecap', 'asam manis']

for ayam in nama_ayam :
    print(f" I love {ayam}\n")
print(f"I really love ayam!")

for value in range ( 5) :
    print(value)

#using range() to make a list of Numbers
numbers = list(range(1,5))
print(numbers)

even_numbers = list(range(2, 20, 5))
print(even_numbers)

triples =[]
for value in range(1, 40):
    triple = value ** 3
    triples.append(triple)

print(triples)

digits = [11,4,5,6,8,5,4,3,2,4]
print(min(digits))

doubled = [val ** 4 for val in range(1,11) ]
print(doubled)

#try it yourself

#for angka in range(1,21):
#    print(angka)
juta = list(range(1,1000000))
print(min(juta))
print(max(juta))
print(sum(juta))

#num = list(range(1,20,2))
#for numb1 in num :
 #   print(numb1)

num3 =[]
for angka3 in range(3,30) :
    numb3 = angka3 * angka3
    num3.append(numb3)

print(num3)

print("------------working with part if a list--------")
players = ['rina', 'yuri', 'mashiro', 'yena', 'eunbi']
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-2:])

#loopinng through a slice
singers = ['denise', 'minji', 'dita', 'soodam', 'jinni']

print("here are the last three singers on my team :")
for singer in singers[-3:]:
    print(singer.title())


#copying a list

food = ['cake', 'salada', 'chicken', 'snack']
copy_food = food[:]

print(food, copy_food)

#Try it yourself
buffet_menu = ('fried rice', 'sate', 'sushi', 'cake')

for menu in buffet_menu :
    print(menu)

buffet_menu = ('nasi kucing', 'bakso', 'sate', 'sushi')
for menu in  buffet_menu :
    print(menu)


























