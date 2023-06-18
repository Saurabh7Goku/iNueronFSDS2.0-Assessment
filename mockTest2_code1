def mySqrt(x):
    # Edge Case if input is 0 or 1
    if x == 0 or x == 1:
        return x
    # Initial guess for the square root for the comparison.
    guess = x 

    while True:
        # Calculate the new guess using Newton's method
        new_guess = (guess + x // guess) // 2
        
        # If the new guess is not closer to the actual square root, break the loop
        if new_guess >= guess:  
            break
            
        guess = new_guess

    return guess
