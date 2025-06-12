import tkinter as tk
from tkinter import ttk, messagebox
from slot_machine import SlotMachine
from wallet import Wallet
from validator import Validator

class SlotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Maangas Slot Machine")
        self.root.configure(bg="#1c1c1c")

        self.wallet = Wallet()
        self.machine = SlotMachine()
        self.setup_style()
        self.setup_ui()

 def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1c1c1c", foreground="#f1f1f1", font=("Consolas", 12))
        style.configure("TButton", background="#333", foreground="#00ffcc", font=("Consolas", 12, "bold"))
        style.map("TButton", background=[("active", "#00ffcc")], foreground=[("active", "#000")])
        style.configure("Header.TLabel", font=("Consolas", 16, "bold"), foreground="#00ffcc")

 def setup_ui(self):
        ttk.Label(self.root, text="🧨 Deposit Amount:", style="Header.TLabel").grid(row=0, column=0, sticky="w", padx=10)
        self.deposit_entry = ttk.Entry(self.root)
        self.deposit_entry.grid(row=0, column=1, padx=10)
        ttk.Button(self.root, text="💸 Deposit", command=self.deposit).grid(row=0, column=2, padx=10)

        ttk.Label(self.root, text="🎯 Lines (1-3):").grid(row=1, column=0, sticky="w", padx=10)
        self.lines_entry = ttk.Entry(self.root)
        self.lines_entry.grid(row=1, column=1, padx=10)

        ttk.Label(self.root, text="💲 Bet per Line:").grid(row=2, column=0, sticky="w", padx=10)
        self.bet_entry = ttk.Entry(self.root)
        self.bet_entry.grid(row=2, column=1, padx=10)

        ttk.Button(self.root, text="🎰 SPIN", command=self.spin).grid(row=3, column=1, pady=10)

        self.slot_output = tk.Label(self.root, text="", font=("Consolas", 20), bg="#1c1c1c", fg="#ffdd00", justify="center")
        self.slot_output.grid(row=4, column=0, columnspan=3, pady=10)

        self.result_label = tk.Label(self.root, text="", fg="#00ffcc", bg="#1c1c1c", font=("Consolas", 14))
        self.result_label.grid(row=5, column=0, columnspan=3)

        self.balance_label = tk.Label(self.root, text="💵 Balance: $0", fg="#ffffff", bg="#1c1c1c", font=("Consolas", 14, "bold"))
        self.balance_label.grid(row=6, column=0, columnspan=3, pady=5)