#int() converts string to int

luckyNumber=input("What is your lucky number?")
magicNumber=luckyNumber+5

#this line prints luckyNumber concatenated with 5
#as input() takes input as string only

print(magicNumber) #error

#solution
magicNumber=int(luckyNumber)+5
print(magicNumber)
