# starting guest list (3-4)
guests = ["Kofi", "Amina", "Chinedu"]

print("initial invitations:")
for person in guests:
    print(f"hey {person}, you're invited to dinner.")

# 3-5: one person can't make it
print(f"\n{guests[1]} can't make it to the dinner.")

# replace them
guests[1] = "Zanele"

print("\nnew invitations:")
for person in guests:
    print(f"hey {person}, you're invited to dinner.")

# 3-6: found a bigger table
print("\ngood news, i found a bigger dinner table!")

guests.insert(0, "Tunde")      # beginning
guests.insert(2, "Fatima")     # middle
guests.append("Kwame")         # end

print("\ninvitations with bigger table:")
for person in guests:
    print(f"hey {person}, you're invited to dinner.")

# 3-7: table won't arrive
print("\nbad news... i can only invite two people.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"sorry {removed}, i can't invite you anymore.")

print("\nstill invited:")
for person in guests:
    print(f"{person}, you're still invited.")

# empty the list
del guests[:]

print("\nfinal guest list:")
print(guests)
