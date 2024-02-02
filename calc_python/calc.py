#This is a simple study of using modules in different scripts.

#First script is a calculator:

#Adding:
def adding(a, b):
    return float(a) + float(b)

#Subtracting:
def subtracting(a, b):
    return float(a) - float(b)

#Dividing:
def dividing(a, b):
    if b==0:
        return 0
    return float(a) / float(b)

#Multiplying:
def multiplying(a, b):
          return float(a) * float(b)

# Calculating the percentage of a number relative to another:
def percentage(part,whole):
    if whole == 0:
        return 0
    return (part / whole) * 100