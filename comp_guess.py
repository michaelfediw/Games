def comp_guess():
    '''
    (none) -> (tuple)
    
    This is a game where the program attempts to guess what number (positive integer) the user is thinking of.
    The user is prompted for a upper limit (ie: the number is below 100, 1000, 10000, 77798, etc).
    The program prints a guess to the screen, and the user is prompted to respond with whether or not their number is higher, lower, 
    or the same as the number the program guesses.
    The program will then print a new guess to the screen.
    The game ends when the user inputs 'correct' when prompted.
    The program then returns a tuple of the form (the answer, how many guesses it took the program to get it)
    
    '''
    
    size = int(input('The lowest possibility is 1, enter the highest possibility: '))
    
    if size % 2 != 0:
        size += 1     
    
    poss = list(range(1,size+1)) 
        
    resp = 'start'
    count = 0
    
    while resp != 'correct':
        count += 1
        a = len(poss)
        if a % 2 != 0:
            a = a + 1
        gue = int(a / 2)
        guess = poss[gue-1]
        
        print (guess)
        
        ans = str(input('Higher, Lower, or Correct: '))
        ans = ans.lower()
        
        if ans == 'higher':
            poss_copy = poss[gue:]
        elif ans == 'lower':
            poss_copy = poss[:gue]
        else:
            poss_copy = poss
        
        poss = poss_copy   
    
        resp = ans
        
    return guess, count
