import a3

print(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO'))
print(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'BOX'))
print(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TEN'))

print(a3.make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0))
print(a3.make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))

# lst = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

# print(len(lst))

# print(lst)
# print(lst[0][0])
# print(lst[0][1])
# print(lst[0][2])
# print(lst[0][3])

# lst = ['A', 'N', 'T', 'T']
# print(lst[0])

# for i in range(len(lst)):
#   print(lst[i])

lst = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

print(range(len(lst)))
#    print(lst[i][1])

#print(lst[0][1] + lst[1][1])
# prin(lst[i][column_index])

print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1))
print(a3.make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2))

print(a3.board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB'))

print(a3.board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO'))

print(a3. board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT'))
