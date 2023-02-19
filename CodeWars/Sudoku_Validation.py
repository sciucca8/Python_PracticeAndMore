def validate_sudoku(board):
    for x in zip(*board):
        print(x)
    for row in board:
        for num in row:
            if row.count(num) > 1 or num == 0:
                return False

    for i in range(len(board)):
        for riga in board:
            if board[board.index(riga)][i] in [x[i] for x in board[board.index(riga)+1:]]:
                return False

    range1 = 3
    range2 = 3
    ls = []
    for x in range(9):
        print(range1, range2)
        for r in range(range1 - 3, range1):
            for c in range(range2 - 3, range2):
                ls.append(board[r][c])
                print(ls)
                if len(ls) == 9:
                    for x in ls:
                        if x in ls[ls.index(x) + 1:]:
                            return False
                    ls.clear()
        
        print(range1, range2)
        if r == range1 - 1 and c == range2 - 1:
            if range1 == 9 and range2 == 9:
                return True
            elif range2 < 9:
                range2 += 3
            elif range2 == 9:
                range1 += 3
                range2 = 3
            
print(validate_sudoku([[5,3,4,6,7,8,9,1,2],
				       [6,7,2,1,9,5,3,4,8],
				       [1,9,8,3,4,2,5,6,7],
                       [8,5,9,7,6,1,4,2,3],
                       [4,2,6,8,5,3,7,9,1],
                       [7,1,3,9,2,4,8,5,6],
                       [9,6,1,5,3,7,2,8,4],
                       [2,8,7,4,1,9,6,3,5],
                       [3,4,5,2,8,6,1,7,9]]))



myset = list(range(1, 10))      
board =                [[5,3,4,6,7,8,9,1,2],
				       [6,7,2,1,9,5,4,4,8],
				       [1,9,8,3,4,2,5,6,7],
                       [8,5,9,7,6,1,4,2,3],
                       [4,2,6,8,5,3,7,9,1],
                       [7,1,3,2,2,4,8,5,6],
                       [6,6,1,5,3,7,2,8,4],
                       [2,8,7,4,1,9,6,3,5],
                       [3,1,5,2,8,6,1,6,9]]

print(myset, type(myset))
for x in zip(*board):
    print(list(x), set(x))
