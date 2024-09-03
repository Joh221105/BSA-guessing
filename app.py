def binary_search_guess(low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    return mid

def number_guessing_game():
    low, high = 1, 100
    guess = binary_search_guess(low, high)
    
    while guess is not None:
        print(f"Is your number {guess}?")
        response = input("Enter 'h' if it's higher, 'l' if it's lower, 'c' if correct: ").strip().lower()
        
        if response == 'c':
            print(f"Yay! The number was {guess}.")
            break
        elif response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            print("Invalid response. Please enter 'h', 'l', or 'c'.")
        
        guess = binary_search_guess(low, high)
        if guess is None:
            print("It seems the number is out of the range.")
            break

number_guessing_game()


