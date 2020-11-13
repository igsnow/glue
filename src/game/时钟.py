"""
Python 时钟
"""
import time
import tkinter as tk


class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Python 时钟')
        self.time_text = ''
        self.lbl = tk.Label(self,
                            text=self.time_text,
                            font=("ds-digital", 80),
                            padx=10,
                            pady=10,
                            background="black",
                            foreground="cyan"
                            )

        self.lbl.pack()
        self.update_time()

    def update_time(self):
        self.time_text = time.strftime('%y-%m-%d\n%H:%M:%S %p')
        self.lbl.config(text=self.time_text)
        self.after(1000, self.update_time)


if __name__ == '__main__':
    app = Clock()
    app.mainloop()
