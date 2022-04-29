import random, time
def getanswer (answerNumber):
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'    
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'    
    elif answerNumber == 5:
        return 'Ask again'    
    elif answerNumber == 6:
        return 'Concentrate... and try again'    
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'        
    elif answerNumber == 9:
        return 'Very doubtful.'    
r = random.randint(1, 9)   
print(r)     
time.sleep(.5)
print('Deciding...')
time.sleep(2)
fortune = getanswer(r)
print(fortune)