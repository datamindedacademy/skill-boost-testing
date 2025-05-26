import pytest

from skill_boost_testing.galgje.galgje import Galgje, DeadException


class TestGalgjeGame:

    @pytest.fixture
    def game(self):
        """Create a new game instance before each test."""
        return Galgje.start_game()

    def test_verify_word_is_chosen_when_starting_game(self, game):
        """Test that a word is selected when starting a game."""
        assert game.get_word_to_guess() is not None
        assert len(game.get_word_to_guess()) > 0

    def test_amount_of_attempts_is_increased_when_guessing(self, game):
        """Test that guess attempts are counted correctly."""
        game.guess_letter('a')
        game.guess_letter('b')
        game.guess_word("test")

        assert game.get_guess_attempt() == 3

    def test_game_is_lost_when_guessing_10_times_wrong_letter(self, game):
        """Test that the game ends after 10 wrong letter guesses."""
        for i in range(9):
            game.guess_letter('A')

        with pytest.raises(DeadException):
            game.guess_letter('A')

    def test_game_is_lost_when_guessing_10_times_wrong_word(self, game):
        """Test that the game ends after 10 wrong word guesses."""
        for i in range(9):
            game.guess_word("test")

        with pytest.raises(DeadException):
            game.guess_word("test")

    def test_game_is_won_when_guessing_correct_on_10th_attempt(self, game):
        """Test that the game can be won on the last attempt."""
        for i in range(9):
            game.guess_letter('l')

        assert game.guess_word(game.get_word_to_guess())

    def test_guessed_letters_are_placed_in_correct_position(self, game):
        """Test that correctly guessed letters appear in the right positions."""
        existing_char_to_guess = game.get_word_to_guess()[2]  # position 3
        non_existing_char = '@'
        assert game.get_guessed_letters()[2] == ' '

        game.guess_letter(existing_char_to_guess)
        game.guess_letter(non_existing_char)

        assert game.get_guessed_letters()[2] == existing_char_to_guess

    def test_guessing_same_letters_twice_does_not_influence_word_length_or_position(self, game):
        """Test that guessing the same letter multiple times works correctly."""
        existing_char_to_guess = game.get_word_to_guess()[2]  # position 3

        game.guess_letter(existing_char_to_guess)
        guessed_letters_array_size = len(game.get_guessed_letters())
        game.guess_letter(existing_char_to_guess)

        assert game.get_guessed_letters()[2] == existing_char_to_guess
        assert len(game.get_guessed_letters()) == guessed_letters_array_size
