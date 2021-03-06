from openpyxl import Workbook
from visualGrid.visualGridv2 import VisualGridMaker

info = {
    'num_reels': 5,
    'view_size': 3,
    'win_lines': 25,
    'symbol_pos': [[0, 1, 2, 3, 4],
                   [5, 6, 7, 8, 9],
                   [10, 11, 12, 13, 14]]
}

win_lines = [
    [1, 1, 1, 1, 1],  # 1
    [0, 0, 0, 0, 0],  # 2
    [2, 2, 2, 2, 2],  # 3
    [0, 1, 2, 1, 0],  # 4
    [2, 1, 0, 1, 2],  # 5
    [1, 0, 1, 0, 1],  # 6
    [1, 2, 1, 2, 1],  # 7
    [0, 1, 0, 1, 0],  # 8
    [2, 1, 2, 1, 2],  # 9
    [1, 0, 0, 0, 1],  # 10
    [1, 2, 2, 2, 1],  # 11
    [2, 2, 1, 2, 2],  # 12
    [0, 0, 1, 0, 0],  # 13
    [2, 1, 1, 1, 2],  # 14
    [0, 1, 1, 1, 0],  # 15
    [0, 2, 0, 2, 0],  # 16
    [2, 0, 2, 0, 2],  # 17
    [1, 1, 0, 1, 1],  # 18
    [1, 1, 2, 1, 1],  # 19
    [2, 2, 0, 2, 2],  # 20
    [0, 0, 2, 0, 0],  # 21
    [0, 0, 1, 2, 2],  # 22
    [2, 2, 1, 0, 0],  # 23
    [1, 0, 2, 0, 1],  # 24
    [1, 2, 0, 2, 1],  # 25

]

if __name__ == "__main__":
    wb = Workbook()
    ws = wb.active

    worksheet = VisualGridMaker(info, ws, win_lines)
    worksheet.grid_maker()

    wb.save('sample.xlsx')
