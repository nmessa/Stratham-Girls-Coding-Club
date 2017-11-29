#Storyteller

#This program will write a biography about you

#Enter your name from the keyboard and store it in a variable 'name'
name = input("Enter your name: ")

#Enter the town where you were born and store it in a variable 'town'
town = input("Enter the town you were born in: ")

#Enter your the sport you like to play and store it in a variable 'sport'
sport = input("What is your favorite sport: ")

#Enter your favorite subject in school and store it in a variable 'subject'
subject = input("What is your favorite subject? ")

#Enter your favorite movie and store it in a variable 'movie'
movie = input("What is your favorite movie? ")

#Enter the names of 3 friends and store each one in the variables
#that are their names
friend1, friend2, friend3 = input("Enter the names of 3 friends: ").split()

#Optional: enter other information that you think would make your store better

#Write your story
print("My name is", name, ". I was born in", town,". In high school I was",
      "really good at", sport, "but unfortunately I could not hit a curve ball.",
      "I therefore had to result to my love of", subject, ". I used my prowess in",
      subject, "to make", friend1, "send", friend3, "to the moon.", "This made",
      friend2, "jealous so he would not buy me a ticket to go see", movie)

