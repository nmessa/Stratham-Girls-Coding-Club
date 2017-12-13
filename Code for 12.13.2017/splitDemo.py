##Split Demonstration
##Author: nmessa
##Date: 12/12/2017

phrase = 'Now is the time for all good men to come to the aid of their country'
lincoln = '2/9/1809'
christmas = '12-25-2017'
myTime = '10:32:53'


phraseList = phrase.split()
lincolnList = lincoln.split('/')
christmasList = christmas.split('-')
myTimeList = myTime.split(':')
weird = phrase.split('t')

print(phraseList)
print(lincolnList)
print(christmasList)
print(myTimeList)
print(weird)

for word in phraseList:
    print(word, end = ' ')
