import pygame
from colors import Colors

# creates the grid where the cells are
class Grid:
	def __init__(self):
		# number of rows and columns in the grid
		self.num_rows = 20
		self.num_cols = 10
		# size of each cell in pixels
		self.cell_size = 30
		# 2D array to represent the grid, initialized with zeros
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		# colors for each type of cell
		self.colors = Colors.get_cell_colors()

	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ")
			print()
# Checks if a given position is inside the grid, creating a boundary
	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False
# checks if a cell at a given position is empty
	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

# checks to see if the row is full by checking each cell to see if everything is full
	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True

# clears the row by turning off the cells in that row
	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

# method to move a row down by a specific number of rows
	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0
# method to clear all full rows and move the rows above down
	def clear_full_rows(self):
		completed = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed
# Resets the grid by setting all cells to zero
	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0
# method to draw the grid on the screen
	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)