print("Hello world!!")
print("\n")

""" Lists of a month """
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print("\n")

print(month[-1])
print("\n")

for x in month:
    print(x)

#strip
first_half = month[:6]
print(first_half) 

last_half = month[6:]
print(last_half)

random_month = month[2:4]
print(random_month)

# prints length
print(type(random_month))
print(len(random_month))

# print(type(month))