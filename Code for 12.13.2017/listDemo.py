##List Demo
##Author: nmessa
##Date: 12.13.2017

#Create an empty list
friends = []

#Add 5 friends to the list
for i in range(5):
    name = input('Enter your friends name: ')
    friends.append(name)

#Print the list of friends
print(friends)

#print your friends
for friend in friends:
    print(friend)

#sort your friends
friends.sort()
print(friends)



