# strings in python are stored as sequences of letters in memory

print(type("Deya Bakheet"))
print('I\'m thirsty')
print("I'm thirsty")
print("\n")  # new line
print("\t")  # adds a tab
print("------------------------------------------")
# 'Hay you!' [4]=y
name = "Deya Bakheet"
print(name[3])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::1])
print(name[::-1])
print(name[0:10:2])  # : is called slicing and has the format [ start : end : step ]
print("------------------------------------------")
print('*' * 10)  # *********
print("------------------------------------------")
# Basic Functions
print(len("Bakheet"))
print("------------------------------------------")
# Basic Methods
print(" I am alone ".strip())
print("On an Jordan".strip('d'))
print("but life is good!".split())
print("Diaa Bakheet".replace("Diaa", "Deya"))
print("Need to make fire".startswith("Need"))
print("upper case".upper())
print("LOWER CASE".lower())
print("deya bakheet".capitalize())
print("Welcome Deya Bakheet".count("t"))
print("Deya Aldeen Nayif Bakheet".find("i"))
print("Deya Aldeen Nayif Bakheet".find("z"))
print("Deya Aldeen Nayif Bakheet".index("t"))
print("------------------------------------------")
# String Formatting
name1 = "Deya"
name2 = "Bakheet"

print(f"Welcome there {name1} and {name2}")
print("Hello there {} and {}".format(name1, name2))
long_string = '''
WOW
O O
---
'''
print(long_string)

name = 'Deya Bakheet'
age = '31'

print(f'Welcome {name}. You are {age} years old')


print("------------------------------------------")
# Palindrome check
word = "reviver"
p = bool(word.find(word[::-1]) + 1)
print(p)
