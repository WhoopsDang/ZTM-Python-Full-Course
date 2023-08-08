import guessGame
import unittest


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = guessGame.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input2(self):
        answer = 5
        guess = 3
        result = guessGame.run_guess(guess, answer)
        self.assertFalse(result)

    def test_out_of_bounds(self):
        answer = 5
        guess = 12
        result = guessGame.run_guess(guess, answer)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
