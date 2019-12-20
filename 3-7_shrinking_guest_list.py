guests = ['Robert', 'André', 'Joseph', 'Renée']

message = "Hi, " + guests[0] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[1] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[2] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[3] + ", I'd like to invite you to dinner"
print(message)

print(guests)
print("\nI found a bigger dinner table, so we'll have three more guests.")

guests.insert(0, "Hector")

guests.insert(2, "Jeanne")

guests.append("Léopold")

print(guests)
message = "Hi, " + guests[0] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[1] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[2] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[3] + ", I'd like to invite you to dinner"
print(message)

message = "Hi, " + guests[4] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[5] + ", I'd like to invite you to dinner"
print(message)
message = "Hi, " + guests[6] + ", I'd like to invite you to dinner"
print(message)

print("Sorry, my table won't arrive in time, so i'll have to cancel some invitations and invite only two persons.")

cancelled_guest=guests.pop()
print("Sorry, " + cancelled_guest + ", I can't invite you any more")

cancelled_guest=guests.pop()
print("Sorry, " + cancelled_guest + ", I can't invite you any more")

cancelled_guest=guests.pop()
print("Sorry, " + cancelled_guest + ", I can't invite you any more")

cancelled_guest=guests.pop()
print("Sorry, " + cancelled_guest + ", I can't invite you any more")

cancelled_guest=guests.pop()
print("Sorry, " + cancelled_guest + ", I can't invite you any more")

print(guests)

print("Hey, " + guests[0] + ", you're still invited.")
print("Hey, " + guests[1] + ", you're still invited.")

del guests[0]
del guests[0]

print(guests)
