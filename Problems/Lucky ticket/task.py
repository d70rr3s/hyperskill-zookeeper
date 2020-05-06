# Save the input in this variable
ticket = input()

# Add up the digits for each half
parts = list(ticket)
half1 = int(parts[0]) + int(parts[1]) + int(parts[2])
length = len(parts)
half2 = int(parts[length - 3]) + int(parts[length - 2]) + int(parts[length - 1])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
