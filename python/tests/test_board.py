import unittest
import sys
sys.path.append('../models')
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
