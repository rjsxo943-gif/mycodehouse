import tkinter as tk
from tkinter import colorchooser


class PaintApp:
    def __init__(self, master):
        self.master = master
        self.color = "black"
        self.width = 2
        self.eraser = False
        self.last_x = None
        self.last_y = None

        toolbar = tk.Frame(master)
        toolbar.pack(side="top", fill="x", padx=6, pady=6)

        tk.Button(toolbar, text="색상", command=self.choose_color).pack(side="left")
        tk.Button(toolbar, text="지우개", command=self.toggle_eraser).pack(side="left", padx=5)
        tk.Button(toolbar, text="지우기", command=self.clear_canvas).pack(side="left", padx=5)

        tk.Label(toolbar, text="굵기").pack(side="left", padx=(10, 0))

        self.width_var = tk.IntVar(value=self.width)

        tk.Scale(
            toolbar,
            from_=1,
            to_=20,
            orient="horizontal",
            variable=self.width_var,
            command=lambda value: self.set_width(int(value))
        ).pack(side="left", padx=5)

        self.canvas = tk.Canvas(master, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y

        r = self.width / 2
        self.canvas.create_oval(
            event.x - r, event.y - r,
            event.x + r, event.y + r,
            outline=self.current_color(),
            fill=self.current_color(),
            width=0
        )

    def draw(self, event):
        if self.last_x is None:
            return

        self.canvas.create_line(
            self.last_x, self.last_y,
            event.x, event.y,
            fill=self.current_color(),
            width=self.width,
            capstyle="round",
            smooth=True
        )

        self.last_x = event.x
        self.last_y = event.y

    def stop_draw(self, event):
        self.last_x = None
        self.last_y = None

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.eraser = False

    def toggle_eraser(self):
        self.eraser = not self.eraser

    def clear_canvas(self):
        self.canvas.delete("all")

    def set_width(self, value):
        self.width = int(value)

    def current_color(self):
        return "white" if self.eraser else self.color


if __name__ == "__main__":
    root = tk.Tk()
    root.title("그림판")
    root.geometry("900x650")

    app = PaintApp(root)

    root.mainloop()