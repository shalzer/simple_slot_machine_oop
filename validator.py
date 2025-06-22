MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

class Validator:
    @staticmethod
    def validate_lines(lines):
        if not (1 <= lines <= MAX_LINES):
            raise ValueError("🎯 Lines must be between 1 and 3.")

    @staticmethod
    def validate_bet(bet):
        if not (MIN_BET <= bet <= MAX_BET):
            raise ValueError(f"💲 Bet must be between ${MIN_BET} and ${MAX_BET}.")