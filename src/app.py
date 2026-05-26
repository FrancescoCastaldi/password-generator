import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_password, ALGORITHMS
from utils import copy_to_clipboard


class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🔐 Password Generator")
        self.resizable(False, False)
        self.configure(padx=24, pady=20, bg="#1e1e2e")
        self._build_ui()

    def _build_ui(self):
        label_font = ("Helvetica", 11)
        title_font = ("Helvetica", 16, "bold")
        bg = "#1e1e2e"
        fg = "#cdd6f4"
        accent = "#89b4fa"
        btn_bg = "#313244"

        tk.Label(self, text="Password Generator", font=title_font, bg=bg, fg=accent).grid(
            row=0, column=0, columnspan=2, pady=(0, 16)
        )

        tk.Label(self, text="Algorithm:", font=label_font, bg=bg, fg=fg).grid(
            row=1, column=0, sticky="w", pady=4
        )
        self.algorithm_var = tk.StringVar(value=ALGORITHMS[0])
        algo_menu = ttk.Combobox(
            self,
            textvariable=self.algorithm_var,
            values=ALGORITHMS,
            state="readonly",
            width=26,
        )
        algo_menu.grid(row=1, column=1, sticky="w", pady=4)

        tk.Label(self, text="Length (chars):", font=label_font, bg=bg, fg=fg).grid(
            row=2, column=0, sticky="w", pady=4
        )
        self.length_var = tk.IntVar(value=32)
        length_spin = tk.Spinbox(
            self,
            from_=8,
            to=128,
            textvariable=self.length_var,
            width=6,
            bg=btn_bg,
            fg=fg,
            insertbackground=fg,
        )
        length_spin.grid(row=2, column=1, sticky="w", pady=4)

        tk.Button(
            self,
            text="Generate",
            command=self._generate,
            bg=accent,
            fg="#1e1e2e",
            font=("Helvetica", 11, "bold"),
            relief="flat",
            padx=12,
            pady=6,
            cursor="hand2",
        ).grid(row=3, column=0, columnspan=2, pady=(14, 6))

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            self,
            textvariable=self.password_var,
            font=("Courier", 11),
            width=38,
            state="readonly",
            readonlybackground=btn_bg,
            fg=fg,
            insertbackground=fg,
            relief="flat",
        )
        self.password_entry.grid(row=4, column=0, columnspan=2, pady=6)

        tk.Button(
            self,
            text="Copy to Clipboard",
            command=self._copy,
            bg=btn_bg,
            fg=fg,
            font=label_font,
            relief="flat",
            padx=10,
            pady=4,
            cursor="hand2",
        ).grid(row=5, column=0, columnspan=2, pady=(4, 0))

    def _generate(self):
        pwd = generate_password(
            algorithm=self.algorithm_var.get(),
            length=self.length_var.get(),
        )
        self.password_var.set(pwd)

    def _copy(self):
        pwd = self.password_var.get()
        if not pwd:
            messagebox.showwarning("No Password", "Generate a password first.")
            return
        copy_to_clipboard(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
