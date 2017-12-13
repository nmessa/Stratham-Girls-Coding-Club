##Tuple Demo
##Author: nmessa
##Date: 12.13.2017

#Create an empty list to hold the Pythagorean triples
triples = []

for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if a**2 + b**2 == c**2:
                triples.append((a,b,c))

#Print the triples
for t in triples:
    print(t)
    


