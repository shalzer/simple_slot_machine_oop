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

    def format_slots(self, columns):
        lines = []
        for row in range(self.rows):
            line = " | ".join(columns[col][row] for col in range(self.cols))
            lines.append(line)

        return "\n".join(lines)

    def calculate_winnings(self, columns, lines, bet):