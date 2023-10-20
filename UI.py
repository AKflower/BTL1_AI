
import tkinter as tk
from DFS import NQueens_DFS
from BFS import NQueens_BFS
from heuristic import NQueens_Heuristic
import time

class NQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('N-Queens Solver')

        self.board_size_label = tk.Label(root, text="Enter the board size (n):")
        self.board_size_label.grid(row=1, column=0, columnspan=2)

        self.board_size_entry = tk.Entry(root)
        self.board_size_entry.grid(row=1, column=2)

        self.solve_button = tk.Button(root, text="DFS Solve", width = 12, height = 1, command=self.dfs_solve)
        self.solve_button.grid(row=0, column=3)

        self.solve_button = tk.Button(root, text="BFS Solve", width = 12, height = 1,command=self.bfs_solve)
        self.solve_button.grid(row=1, column=3)

        self.solve_button = tk.Button(root, text="Heuristic Solve",  width = 12, height = 1, command=self.heuristic_solve)
        self.solve_button.grid(row=2, column=3)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=3, column=0, columnspan=2)

        self.solution_text = tk.Text(root, height=20, width=40)
        self.solution_text.grid(row=3, column=2, columnspan=2)

        self.n = None
        self.board = None


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

    def bfs_solve(self):
        try:
            self.n = int(self.board_size_entry.get())
            self.board = [[0] * self.n for _ in range(self.n)]
            self.canvas.delete("all")  # Clear the canvas
            self.solution_text.delete(1.0, tk.END)  # Clear the solution text
            self.bfs_display_all_solutions()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for 'n'.")
    def bfs_display_all_solutions(self):
        n_queens = NQueens_BFS(self.n)
        solutions = n_queens.BFS()
        if solutions == []:
            # No solutions found
            self.solution_text.insert(tk.END, "No solutions found.")

        # Display board N <= 10
        if self.n <= 10:
            for solution in solutions:
                self.print_solution(solution)
                self.draw_board(solution)
                self.root.update()
                self.root.after(1000)

            self.solution_text.insert(tk.END, f"Total solutions: {len(solutions)}")

        # Display number of solutions
        
        if self.n > 10:
            self.solution_text.insert(tk.END, f"Total solutions: {len(solutions)}")
            # self.solution_text.insert(tk.END, "\n\n")
            # self.solution_text.insert(tk.END, "\n".join(["".join(["Q" if (i, j) in solutions[0] else "." for j in range(self.n)]) for i in range(self.n)]) + "\n\n")



    def dfs_solve(self):
        try:
            self.n = int(self.board_size_entry.get())
            self.board = [[0] * self.n for _ in range(self.n)]
            self.canvas.delete("all")  # Clear the canvas
            self.solution_text.delete(1.0, tk.END)  # Clear the solution text
            self.dfs_display_all_solutions()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for 'n'.")

    def dfs_display_all_solutions(self):
        n_queens = NQueens_DFS(self.n)
        solutions = n_queens.DFS()
        if solutions == []:
            # No solutions found
            self.solution_text.insert(tk.END, "No solutions found.")

        # Display board N <= 10
        if self.n <= 10:
            for solution in solutions:
                self.print_solution(solution)
                self.draw_board(solution)
                self.root.update()
                self.root.after(1000)

            self.solution_text.insert(tk.END, f"Total solutions: {len(solutions)}")

        # Display number of solutions
        
        if self.n > 10:
            self.solution_text.insert(tk.END, f"Total solutions: {len(solutions)}")
            # self.solution_text.insert(tk.END, "\n\n")
            # self.solution_text.insert(tk.END, "\n".join(["".join(["Q" if (i, j) in solutions[0] else "." for j in range(self.n)]) for i in range(self.n)]) + "\n\n")

    
    def heuristic_solve(self):
        try:
            self.n = int(self.board_size_entry.get())
            self.board = [[0] * self.n for _ in range(self.n)]
            self.canvas.delete("all")  # Clear the canvas
            self.solution_text.delete(1.0, tk.END)  # Clear the solution text
            self.heuristic_display_solutions()
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid integer for 'n'.")

    def heuristic_display_solutions(self):
        n_queens = NQueens_Heuristic(self.n)
        start_time = time.time()
        solutions = n_queens.queen_fast_search()
        end_time = time.time()
        self.solution_text.insert(tk.END, f"Time taken: {end_time - start_time} seconds\n")
        if solutions == []:
            # No solutions found
            self.solution_text.insert(tk.END, "No solutions found.")

        # Display board N <= 20
        if self.n <= 20:
            self.print_solution(n_queens.queenPosSol)
            self.draw_board(n_queens.queenPosSol)
            self.root.update()
            self.root.after(1000)

            

        # Display number of solutions
        
        if self.n > 20 and self.n <= 50:
            self.print_solution(n_queens.queenPosSol)

        if self.n > 50:
            #show solution
            self.solution_text.insert(tk.END, n_queens.queenPosSol)


if __name__ == "__main__":
    root = tk.Tk()
    gui = NQueensGUI(root)
    root.mainloop()