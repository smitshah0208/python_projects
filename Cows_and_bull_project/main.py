def check_length(code):
    if len(str(code)) != 4:
        print("Please enter a four digit code only.")
    else:
        return True


def check_uniqueness(code):
    unique_num = []
    for number in str(code):
        if number not in unique_num:
            unique_num.append(number)
    if len(unique_num) == 4:
        return True
    else:
        print("Please enter your your secret code in the correct format.")
        return False


def count_cow_bull(guessed, code):
    cow = 0
    bull = 0
    for number in str(guessed):
        if number in str(code):
            if str(guessed).index(number) == str(code).index(number):
                cow += 1

            elif str(guessed).index(number) != str(code).index(number):
                bull += 1
            else:
                continue
    return cow, bull


def start_game():
    attempts = 3
    while attempts != 0:
        print(f"You have {attempts} remaining.")
        guess = int(input("Enter your guess : "))
        if len(str(guess)) != 4:
            print("Please enter your guess again as it should contain four digits only.")
            guess = int(input("Enter your guess : "))
        elif guess == secret_code:
            print("You guessed correctly.")
            break
        else:
            cow, bull = count_cow_bull(guess, secret_code)
            print(f"Guess : {guess}")
            print(f"Response : {cow} cows, {bull} bulls\n")
        attempts -= 1
    print("Sorry you have no attempts remained. You lose the game!!!.")


secret_code = int(input("Enter your four digit secret code  : "))


while not (check_length(secret_code) and check_uniqueness(secret_code)):
    print("Please enter your code again.\n")
    secret_code = int(input("Enter your four digit secret code  : "))

start_game()


