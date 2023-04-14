guests = ["evie", "seth", "nate"]
message = f"Hey {guests[0].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[1].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[2].title()}, Would you like to go to dinner?"
print(message)
message = f"Im sorry that you cant make it {guests[1].title()}."
print(message)
guests[1] = "emily"
message = f"Hey {guests[0].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[1].title()}, Would you like to go to dinner?"
print(message)
message = f"Hey {guests[2].title()}, Would you like to go to dinner?"
print(message)
