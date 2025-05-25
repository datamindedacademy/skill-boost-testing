import random


class DeadException(Exception):
    """Exception raised when the player has used all guess attempts."""
    pass


class Galgje:
    def __init__(self):
        self.words = ["elephant", "dromedary", "camel", "squirrel"]
        self.word_to_guess = ""
        self.guess_attempt = 0
        self.guessed_letters = []

    @classmethod
    def start_game(cls) -> 'Galgje':
        game = cls()
        game.word_to_guess = random.choice(game.words)
        game.guessed_letters = [' ' for _ in range(len(game.word_to_guess))]
        return game

    def get_word_to_guess(self):
        return self.word_to_guess

    def get_amount_of_letters(self):
        return len(self.word_to_guess)

    def get_guess_attempt(self):
        return self.guess_attempt

    def guess_letter(self, letter):
        self.guess_attempt += 1
        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if letter == char:
                    self.guessed_letters[i] = letter

            self.check_guess_attempt()
            return True

        self.check_guess_attempt()
        return False

    def guess_word(self, s):
        self.guess_attempt += 1
        is_equal = s == self.word_to_guess
        if not is_equal:
            self.check_guess_attempt()
        return is_equal

    def check_guess_attempt(self):
        if self.guess_attempt >= 10:
            raise DeadException("You have guessed 10 times! You lost!")

    def get_guessed_letters(self):
        return self.guessed_letters


def main():
    print("Welcome to Galgje!")
    has_won = False
    game = Galgje.start_game()

    try:
        while not has_won:
            print(f"Attempt {game.get_guess_attempt() + 1}")
            print_guessed_letters(game.get_guessed_letters())
            print("What do you want to do?\nL) guess a letter\nW) guess the word")
            choice = input().lower()

            if choice.startswith('l'):
                print("What's your letter?")
                letter = input()[0]  # Take the first character
                game.guess_letter(letter)
            elif choice.startswith('w'):
                print("What's your word?")
                word = input()
                has_won = game.guess_word(word)

        print(f"Congratulations! You won after {game.get_guess_attempt()} attempts!")

    except DeadException as e:
        print(f"You have lost the game! The word was: {game.get_word_to_guess()}")


def print_guessed_letters(characters):
    for c in characters:
        if c == ' ':
            print("_ ", end="")
        else:
            print(f"{c} ", end="")
    print()


if __name__ == "__main__":
    main()
