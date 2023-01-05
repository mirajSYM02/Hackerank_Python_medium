

def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(string)):
        if string[i] in 'AEIOU':   
        # If the character is a vowel, add the score to Kevin
            kevin_score += len(string) - i
        else:
        # If the character is a consonant, add the score to Stuart
            stuart_score += len(string) - i
    
    # Print the result
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
