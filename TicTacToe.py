def create_board(sq):
	print (sq[7] + '|' + sq[8] + '|' + sq[9])
	print ('_ _ _')
	print (sq[4] + '|' + sq[5] + '|' + sq[6])
	print ('_ _ _')
	print (sq[1] + '|' + sq[2] + '|' + sq[3])
	print ('\n\n\n')

sq = [" "] * 10
def print_intro():
	print('Welcome')
	print('Player one is \'X\'')
	print('It\s your move player 1')
	print('Type numbers 1-9 to occupy squares')
	print('\n\n\n')
	print (sq)
create_board(sq)
print(': ')

print_intro()

sq[5] = 'X'
sq[6] = 'O'
sq[1] = 'X'
create_board(sq)
	
def record_moves():
	move = 10
	while move not in range(1, 10) or is_sq_occupied(move):
		move = eval(input('Enter valid move: '))
		sq[move] = 'X'

print(record_moves())
5
create_board

def is_sq_occupied(num):
	# if sq [num] == '': 
	# 	return False
	# else:
	# 	return True
	return sq[num] != ' '

	def sq_is_full():
		for index in range (1, 10):
			print('idx:', index, 'sq[idx]:', sq[index])
			if sq[index] == '':
				return False
		return True
		print (sq_is_full())

	def three_in_a_row():
		return ((sq[7] == sq[8] == sq[9] and sq[7]!= ' ') or
				(sq[6] == sq[5] == sq[4] and sq[6]!= ' ') or
				(sq[3] == sq[2] == sq[1] and sq[3]!= ' ') or 
				(sq[7] == sq[4] == sq[1] and sq[3]!= ' ') or
				(sq[8] == sq[5] == sq[2] and sq[3]!= ' ') or
				(sq[9] == sq[6] == sq[3] and sq[3]!= ' ') or
				(sq[7] == sq[5] == sq[3] and sq[3]!= ' ') or
				(sq[9] == sq[5] == sq[1] and sq[3]!= ' '))
print(three_in_a_row)
	


#Tasks
# Introduce
# catch moves
# write fn that tests if square is available
# Test if squares are left in appropriate squares
# Test for 3 of a kind
# write an outrow -  conclusion - Player x wins or it was a tie