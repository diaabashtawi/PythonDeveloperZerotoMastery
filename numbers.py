# python's 2 main types for Numbers is int and float (or integers and floating point number)
print(type(1))  # int
print(type(-10))  # int
print(type(0))  # int
print(type(0.0))  # float
print(type(2.2))  # float
print(type(4E2))  # float - 4*10 to the power of 2
print("------------------------------------------")
# Arithmetics
print(10 + 3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 ** 3)  # 100
print(10 / 3)  # 3.3333333
print(10 // 3)  # 3 --> floor division - no decimals and return an int
print(10 % 3)  # 1 --> modulo operator - return the reminder.
print("------------------------------------------")
# Basic Functions
print(pow(5, 2))  # 25 --> like doing 5**2
print(abs(-50))  # 50
print(round(5.46))  # 5
print(round(5.468, 2))  # 5.47 --> round to nth digit
print(bin(512))  # '0b1000000000' --> binary format
print(hex(512))  # '0x200' --> hexadecimal format
print("------------------------------------------")
# Converting Strong to number
age = input("How old are you")
age = int(age)
print(age)
pi = input("What is the value of pi?")
pi= float(pi)
print(pi)
