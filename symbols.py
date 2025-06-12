class SymbolSet:
    def __init__(self):
        self.symbol_counts = {
            "💀": 2,
            "🔥": 4,
            "💎": 6,
            "💰": 8
        }
        self.symbol_values = {
            "💀": 5,
            "🔥": 4,
            "💎": 3,
            "💰": 2
        }

    def get_symbol_pool(self):
        pool = []
        for symbol, count in self.symbol_counts.items():
            pool.extend([symbol] * count)
        return pool

    def get_value(self, symbol):
        return self.symbol_values.get(symbol, 0)