translate = {'O':'0', 'D':'0', 'I': '1', 'L':'1', 'Z':'2', 'E':'3',
             'h':'4', 'S':'5', 'G':'6', 'T':'7', 'L':'7', 'B':'8', 'P':'9'}

def leetSpeak(phrase):
    leet = ""
    for ch in phrase:
        if ch in translate.keys():
            leet += translate[ch]
        else:
            leet += ch
    return leet
        

phrase = input('Enter a phrase: ')
phrase = phrase.upper()
elite = leetSpeak(phrase)
print(elite)
