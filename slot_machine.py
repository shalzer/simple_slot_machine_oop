import random
from symbols import SymbolSet

class SlotMachine:
    def __init__(self):
        self.symbols = SymbolSet()
        self.rows = 3
        self.cols = 3

    def get_spin_result(self):
        all_symbols = self.symbols.get_symbol_pool()
        columns = []

        for _ in range(self.cols):
            current_symbols = all_symbols[:]
            column = []

            for _ in range(self.rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)
        return columns