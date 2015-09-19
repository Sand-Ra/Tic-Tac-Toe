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
create_board(sq)
	
def record_moves():
	move = ''
	while move not in range(1, 10):
		move = eval(input('Enter valid move: '))
		sq[move] = 'X'

print(record_moves())

create_board



#Tasks
# Introduce
# catch moves
# write fn that tests if square is available
# Test if squares are left in appropriate squares
# Test for 3 of a kind
# write an outrow -  conclusion - Player x wins or it was a tie