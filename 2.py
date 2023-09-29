vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

lines_count = int(input("How many lines will there be? "))
poem = []

for n in range(lines_count):
    poem.append(input())


vowels_counter = 0
consonants_counter = 0

for line in poem:
    vowels_counter += sum(1 for char in line.upper() if char in vowels)
    consonants_counter += sum(1 for char in line.upper() if char in consonants)


print("\nNumber of vowels: " + str(vowels_counter))
print("\nNumber of consonants: " + str(consonants_counter))
