import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
discord = "discord.gift/"
while 1:
    code_length = int(input("Type 16. "))
    code_count = int(input("How many codes would you like? "))
    for x in range(0,code_count):
        code = ""
        for x in range(0,code_length):
            code_char = random.choice(chars)
            code      = code + code_char
        print("Here is your code: ", discord + code)