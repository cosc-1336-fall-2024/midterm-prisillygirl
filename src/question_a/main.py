#add import

from question_a import get_sum_of_evens

def main():
    while True:
        user_input = input("Enter a number (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break
        try:
            num = int(user_input)
            if num < 0:
                print("Please enter a positive number.")
            else:
                total = get_sum_of_evens(num)
                print(f"The sum of even numbers up to {num} is: {total}")
        except ValueError:
            print("Invalid. Please enter a valid number.")

if __name__ == "__main__":
    main()