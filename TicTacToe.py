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
	while move not in range(1, 10) or is_sq_is_sq_occupied
		move = eval(input('Enter valid move: '))
		sq[move] = 'X'

print(record_moves())
5
create_board

def is_sq_occupied(num):
	if sq [num] == '': 
		return False
	else:
		return True
	return sq[num] |= ''
	


#Tasks
# Introduce
# catch moves
# write fn that tests if square is available
# Test if squares are left in appropriate squares
# Test for 3 of a kind
# write an outrow -  conclusion - Player x wins or it was a tie