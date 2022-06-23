from enum import Enum
import numpy as np

class GridDirection(Enum):
    up_down="up_or_down"
    left_right="left_or_right"
    diagonal="diagonal"

def get_adjacents_row_col(row,col,direction=GridDirection.left_right):
    if direction is GridDirection.left_right:
        return [[row,col-1],[row,col],[row,col+1]]
    if direction is GridDirection.up_down:
        return [[row-1,col],[row,col],[row+1,col]]
    if direction is GridDirection.diagonal:
        return [[row-1,col-1],[row,col],[row+1,col+1]]
    raise ValueError("Unsupported direction")

def is_in_grid(row,col, rows, cols):
    return row>=0 and row < rows and col >= 0 and col<cols

def row_col_list_is_in_grid(row_col_list,rows,cols):
    for idx in range(0, len(row_col_list)):
        is_in = is_in_grid(row_col_list[idx][0], row_col_list[idx][1], rows, cols)
        if is_in == False:
            return False
    return True

def count_adjacent(grid, direction):
    rows,cols=np.shape(grid)
    count=0
    for row in range(0,rows):
        for col in range(0,cols):
            adjacent_indices_list=get_adjacents_row_col(row,col,direction)
            is_in=row_col_list_is_in_grid(adjacent_indices_list, rows, cols)
            if is_in==True:
                count=count+1
    return count

def compute_adjacent_max_product(grid, direction):
    rows, cols = np.shape(grid)
    max_product=None # In order to handle possibly negative numbers, max_product is not initialized here
    for row in range(0,rows):
        for col in range(0,cols):
            adjacent_indices_list = get_adjacents_row_col(row, col, direction)
            is_in = row_col_list_is_in_grid(adjacent_indices_list, rows, cols)
            if is_in == True:
                product=1
                for idx in range(0, len(adjacent_indices_list)):
                    i=adjacent_indices_list[idx][0]
                    j=adjacent_indices_list[idx][1]
                    product=product*grid[i,j]
                if max_product is None:
                    max_product=product
                else:
                    if product > max_product:
                        max_product=product
    return max_product
