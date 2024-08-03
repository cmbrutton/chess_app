import tkinter as tk
from PIL import Image, ImageTk
import os

# Define the chessboard
chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

# Define the color for each piece
piece_colors = {
    'R': 'black', 'N': 'black', 'B': 'black', 'Q': 'black', 'K': 'black', 'P': 'black',
    'r': 'white', 'n': 'white', 'b': 'white', 'q': 'white', 'k': 'white', 'p': 'white'
}

# Load piece images
piece_images = {
    # 'R': ImageTk.PhotoImage(Image.open("black_rook.png")),
    # 'N': ImageTk.PhotoImage(Image.open("black_knight.png")),
    # 'B': ImageTk.PhotoImage(Image.open("black_bishop.png")),
    # 'Q': ImageTk.PhotoImage(Image.open("black_queen.png")),
    # 'K': ImageTk.PhotoImage(Image.open("black_king.png")),
    # 'P': ImageTk.PhotoImage(Image.open("black_pawn.png")),
    # 'r': ImageTk.PhotoImage(Image.open("white_rook.png")),
    # 'n': ImageTk.PhotoImage(Image.open("white_knight.png")),
    # 'b': ImageTk.PhotoImage(Image.open("white_bishop.png")),
    # 'q': ImageTk.PhotoImage(Image.open("white_queen.png")),
    # 'k': ImageTk.PhotoImage(Image.open("white_king.png")),
    # 'p': ImageTk.PhotoImage(Image.open("white_pawn.png"))
}

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.bind_events()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                color = 'white' if (row + col) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = chessboard[row][col]
                if piece != ' ':
                    image = piece_images[piece]
                    self.canvas.create_image(x1 + 25, y1 + 25, anchor=tk.NW, image=image)

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        col = int(event.x / 50)
        row = int(event.y / 50)
        print(f"Clicked at: ({row}, {col})")

if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()