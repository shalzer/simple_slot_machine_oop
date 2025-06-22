import random
from symbols import SymbolSet

class SlotMachine:
    def __init__(self):
        self.symbols = SymbolSet()
        self.rows = 3
        self.cols = 3