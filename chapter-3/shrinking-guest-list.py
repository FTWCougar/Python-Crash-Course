guests = ["evie", "seth", "nate"]
message = f"Hey {guests[0].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[1].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[2].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey everyone I found a bigger table."
print(message)
guests.insert(0, "jordan")
guests.insert(2, "alfred")
guests.append("bryan")
message = f"Hey {guests[0].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[1].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[2].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[3].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[4].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[5].title()}, Would you like to go to dinner?"
print(message)
message = "Hey everyone the dinner table won't be avaiable in time i can only take two people"
print(message)
poppedGuest = guests.pop()
message = f"Hey sorry i cant invite you {poppedGuest.title()}."
print(message)
poppedGuest = guests.pop(3)
message = f"Hey sorry i cant invite you {poppedGuest.title()}."
print(message)
poppedGuest = guests.pop(2)
message = f"Hey sorry i cant invite you {poppedGuest.title()}."
print(message)
poppedGuest = guests.pop(0)
message = f"Hey sorry i cant invite you {poppedGuest.title()}."
print(message)
message = f"Hey {guests[0].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[1].title()}, Would you like to go to dinner?"
print(message)
del guests[0]
del guests[0]
print(guests)
