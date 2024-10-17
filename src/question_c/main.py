from question_c import get_random_number


def main():
 

    while True:
        number_to_guess = get_random_number()
        print("Guess a number between 1 and 5:")
        
       
        while True:
            try:
                user_guess = int(input("Your guess: "))
                if 1 <= user_guess <= 5:
                    if user_guess == number_to_guess:
                        print("Congratulations! That's right!")
                        break 
                    else:
                        print("Wrong number! Try again!")
                else:
                    print("Enter a number between 1 and 5.")
            except ValueError:
                print("Invalid. Enter a number.")

           
        continue_game = input("Do you want to play again? Enter yes or no: ")
        if continue_game != 'yes':
            print("Thanks for playing!")
            break  

if __name__ == "__main__":
    main()