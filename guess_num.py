import random

def guess_a_number(num):
    rand_num = random.randint(1,num)
    guess = 0

    while rand_num!=guess:
        guess = input(f"Guess a number between 1 and {num}: ")
        guess = int(guess)
        if guess==rand_num:
            print("Yeyy you've guessed it")
            break
        print("Nope, not yet")

guess_a_number(5)

def computer_guess(num):
    low = 1
    high= num
    feedback = ''

    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback= input(f"Is {guess} too high(H) or too low(L), or correct(C): ".lower())
        if feedback == "h":
            high = guess - 1
        elif feedback=='l':
            low = guess + 1
    print(f"Yayy the computer has guessed the number {guess} correctly")

computer_guess(20)