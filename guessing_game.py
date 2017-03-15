def guessing_game():            
    """
    (none) -> (str)
    
    This is a game where the user is first prompted for their difficulty (easy, hard, or soulcrusher).
    Based upon the difficulty the program generates a random 2, 4, or 6 digit number. The user is then prompted for a guess.
    The program prints how many digits the user inputed that are both in the generated number and in the right place,
    as well as how many digits are in the generated number but in the wrong place.
    The game ends when the user guesses the number correctly.
    The program then returns how many guesses it took the user to guess the correct number.
    
    """
    import random
    
    difficulty = str(input("Enter your difficulty(easy(2-digit), hard(4-digit), soulcrusher(6-digit): "))
    difficulty = difficulty.lower()
    
    if difficulty == 'easy':
        ans = random.randint(10, 99)
        length = 2
    
    elif difficulty == 'hard':
        ans = random.randint(1000, 9999)
        length = 4
        
    elif difficulty == 'soulcrusher':
        ans = random.randint(100000, 999999)
        length = 6
    
    ans = str(ans)
    
    
    guess = str((input("enter your guess: ")))
    
    c = 0
    b = 0
    
    failsafe = 0
    
    guesses = 0
    
    while c != length:
        c = 0
        b = 0
        count = 0
        contains = []
        if guess == "exit":
            c = length
            failsafe += 1 
        else:
            for i in guess:
                if i == ans[count]:
                    c += 1
                    count += 1
                    contains.append(i)
                elif i in ans:
                    if i not in contains:
                        b += 1
                        count += 1
                        contains.append(i)
                else:
                    count += 1
                
        guesses += 1
        print ("Right number right spot: ")
        print (c)
        print ("Right number wrong spot: ")
        print (b)
        
        if c != length:
            guess = str(input("What is your new guess? "))
                    
    if failsafe == 1 :
        a = "You lose! You tried " + str(guesses) + " times"
        print (ans)
    else:
        a = "You win! You took " + str(guesses) + " guesses"
        
        
    return a

