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