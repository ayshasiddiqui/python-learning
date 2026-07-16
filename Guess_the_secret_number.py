secret_number = 7
attempt = 0

while attempt < 3:

    guess = int(input("Enter a number: "))
    #print("attempt=",attempt)

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
        print("attempt=",attempt)
    

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Too Low!")

        attempt = attempt + 1
        #print("attempt=",attempt)
if attempt == 3:
    print("Game Over!")
    #print("attempt=",attempt)
