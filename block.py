from colors import Colors
import pygame
from position import Position
# defines a class named block
class Block:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 30
		self.row_offset = 0
		self.column_offset = 0
		self.rotation_state = 0
		# pulls from the dictionary of colors for each block id
		self.colors = Colors.get_cell_colors()

# method to move the block by a specified number of rows and columns
	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns
# method to get the positions of all cells in the current rotation state
	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			# adjusts the position of all cells in the current rotation state
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles
# method to rotate the blcok to the next rotation state
	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0
# method to undo the last rotation and go back to the previous rotation state
	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1
# Draws the block on the pygame screen
	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)