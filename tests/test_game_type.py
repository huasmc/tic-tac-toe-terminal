import unittest
from models.abstracts.game_type import GameType

class TestGameType(unittest.TestCase):

    def test_cannot_instantiate(self):
        with self.assertRaises(TypeError):
            GameType()


if __name__ == '__main__':
    unittest.main()
