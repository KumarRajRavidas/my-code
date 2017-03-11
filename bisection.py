print("Please think of a number between 0 and 100!")
guesno = input('what is your no :')
# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False
# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))



base=input("enter value of base :")   
height=input("enter value of height :")  
x = base**2 + height**2
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print abs(ans**2 - x)
    print x
    print ans
    #print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    #numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
#print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x)) 


'''ListOfNumbers = [ x for x in range(10) ]

ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]

list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
results = []
#this is equivelent to this
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )'''







           
    