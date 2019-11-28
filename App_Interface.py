import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    platform_os = ""

    def __init__(self):
        super().__init__()

        platform_os = self.identify_os()

    def initialize_root_window(self):
        root = tk.Tk()
        root.title("TKPing " + version)
        root.geometry("567x435")
        root.resizable(False, False)

