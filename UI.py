# Can present DFS solution abut N < 14

import tkinter as tk
from DFS import NQueens

class NQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('N-Queens Solver')

        self.board_size_label = tk.Label(root, text="Enter the board size (n):")
        self.board_size_label.grid(row=0, column=0, columnspan=2)

        self.board_size_entry = tk.Entry(root)
        self.board_size_entry.grid(row=0, column=2)

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=0, column=3)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.solution_text = tk.Text(root, height=20, width=40)
        self.solution_text.grid(row=1, column=2, columnspan=2)

        self.n = None
        self.board = None

    def solve(self):
        try:
            self.n = int(self.board_size_entry.get())
            self.board = [[0] * self.n for _ in range(self.n)]
            self.canvas.delete("all")  # Clear the canvas
            self.solution_text.delete(1.0, tk.END)  # Clear the solution text
            self.display_all_solutions()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for 'n'.")

    def display_all_solutions(self):
        n_queens = NQueens(self.n)
        solutions = n_queens.DFS()
        if solutions == []:
            # No solutions found
            self.solution_text.insert(tk.END, "No solutions found.")

        for solution in solutions:
            self.print_solution(solution)
            self.draw_board(solution)
            self.root.update()
            self.root.after(1000)

    def draw_board(self, queens):
        self.canvas.delete("all")
        self.queen_image = tk.PhotoImage(file="assets/queen.png")
        #scale the image to smaller size
        self.queen_image = self.queen_image.subsample(self.n, self.n)

        for row in range(self.n):
            for col in range(self.n):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(
                    col * 400 / self.n,
                    row * 400 / self.n,
                    (col + 1) * 400 / self.n,
                    (row + 1) * 400 / self.n,
                    fill=color,
                )
                if (row, col) in queens:
                    self.canvas.create_image(
                        col * 400 / self.n + 400 / self.n / 2,
                        row * 400 / self.n + 400 / self.n / 2,
                        image=self.queen_image,
                    )
        self.canvas.update()


    def print_solution(self, queens):
        self.solution_text.insert(tk.END, "\n".join(["".join(["Q" if (i, j) in queens else "." for j in range(self.n)]) for i in range(self.n)]) + "\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = NQueensGUI(root)
    root.mainloop()