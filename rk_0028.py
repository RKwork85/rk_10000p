import string

rank = [6, 6, 2, 2, 8, 4, 5, 1]
letter = 'K'
for index, score_item in enumerate(rank, start=5):
    cell_position = letter + str(index)  
    print(cell_position)