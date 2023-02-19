def find_word(board, word):
    ls1 = []
    ls2 = []

    for letter in word:
        for row in board:
            for elem in row: 
                if letter == elem:
                    ls1.append((letter, board.index(row), row.index(elem)))
                
                    print(ls1)
                
testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]
print(find_word(testBoard, "CEREAL"))



