import unittest

class TestTicTacToe(unittest.TestCase):
    def test_check_winner(self):
        board = [
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertTrue(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))

        board = [
            ["X", "O", "X"],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertTrue(check_winner(board, "X"))
        self.assertFalse(check_winner(board, "O"))

        board = [
            ["X", "O", "O"],
            ["X", "O", " "],
            ["O", " ", "X"]
        ]
        self.assertTrue(check_winner(board, "O"))
        self.assertFalse(check_winner(board, "X"))

    def test_get_valid_input(self):
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.assertEqual(get_valid_input("Enter a number: "), 1)
        with unittest.mock.patch('builtins.input', return_value='3'):
            self.assertEqual(get_valid_input("Enter a number: "), None)

if __name__ == "__main__":
    unittest.main()
