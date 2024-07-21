# Print grid
def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Check validity
def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Solve puzzle
def solve_sudoku(grid):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return True
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

# Find empty cell
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

# Input grid
sudoku = []
print("Please use 0 in place of blank spaces")
for i in range(9):
    row = input(f"Enter the elements of row {i + 1} without any spaces: ")
    row = [int(char) for char in row]
    sudoku.append(row)

# Solve and print
if solve_sudoku(sudoku):
    print("Sudoku puzzle solved successfully!")
    print_grid(sudoku)
else:
    print("No solution exists for the given Sudoku puzzle.")
    