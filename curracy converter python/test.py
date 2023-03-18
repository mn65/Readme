# txt = "welcome to the jungle"
# txt = "hello, my name is Peter, I am 26 years old"

# x = txt.split()

# print(x)

currancyDict = {}

with open("currancy.txt") as f:
    content = f.readlines()

for line in content:
    pherse = line.split("\t")
    currancyDict[pherse[0]] = pherse[1]

print(pherse)
print(pherse[0])
print(pherse[1])
print(pherse[2])
print(currancyDict)