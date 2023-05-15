secret_word = "ferrari"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You have run out of guesses.")
else:
    print("You have guessed correctly!")