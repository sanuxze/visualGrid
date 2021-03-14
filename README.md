# visualGrid

## This code makes a visual grid of the win lines given in visualInterface.py

![Sample.xlsx](https://github.com/smandal047/visualGrid/blob/master/images/xl_win_lines.png)

Originally made to automate the API creation of the Slot Machine Games.

![Win Lines](https://www.vegasslotsonline.com/assets/images/index_clip_image002.jpg)

This visuallize the winline lines from the paramters stated below:

Note: the info dict takes the number of reels, view size, number of win lines and the order of symbols of slot

```
info = {
    'num_reels': 5,
    'view_size': 3,
    'win_lines': 25,
    'symbol_pos': [[0, 1, 2, 3, 4],
                   [5, 6, 7, 8, 9],
                   [10, 11, 12, 13, 14]]
}
```

while win lines describe the payline configuration

```
win_lines = [
    [1, 1, 1, 1, 1],  # 1 payline
    [0, 0, 0, 0, 0],  # 2 payline
    [2, 2, 2, 2, 2],  # 3 and so on....
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
```
Enjoy!!!, if you got what you are searching for or keep looking.
