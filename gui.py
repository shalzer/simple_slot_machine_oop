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