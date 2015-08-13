#Many simple games are so well understood that players can play perfectly, 
#always choosing the best move. At that point, the outcome often becomes predetermined. 
#The most familiar example may be tic-tac-toe. In this game, either player can force the game into a draw, 
#no matter what moves the other player makes. In other games, such as connect 4 and chopsticks, 
#one of the players actually has a way to win, no matter what the opponent does.
#Mathematically, we define a winning strategy as a plan a player can use that always ends in a win. 
#To write a winning strategy for one of these games, we cant just fixed list a sequence of moves. 
#The moves have to change depending on what the opponent plays. 
#So a winning strategy specifies a next move for every possible state of the tic-tac-toe board. 
#You can think of it as a function from the state of the game to a next move.
#Perhaps the easiest way to think about winning strategies is recursively. 
#Lets call a state of the game hot. if the current player to move has a winning strategy to finish the game 
#-this is the state that you want to be in. Otherwise, lets call it cold. 
#Clearly, if a player can win in one move, the state of the game is hot. 
#If the current player loses immediately for any available move, the state of the game is cold.
#If the game is not about to end, the best strategy is to play not to lose. 
#That is, the state of the game is hot if the current player has a move that puts the game in a cold state 
#for the next player. Otherwise the state of the game is cold - whatever move the current player makes, 
#the state of the game will be hot for the next player.
#
#For this problem, lets consider a two-player version of the decreasing number game. 
#The game begins with a number N - this is the state of the game. 
#Two players take turns decreasing the number. 
#Each player has two moves available: they can subtract 1 from the number, or divide it in half (not integer division - use floats for this!). 
#The player that decreases the number below 1 is the loser.

#Write a script to prompt the user for the starting state of the game, N, and compute whether that state is hot or cold.
#
#Hint: Write a recursive function, is_hot, to check whether a state of the game is hot. 
#For a base case, note that any game state less than 2 is cold - no matter which move a player makes, the number will drop below 1 and the player loses.
#
#Optional extra: Write a program that actually plays the decreasing number game against the user, and follows a winning strategy whenever one is available. In other words, when it is the computers turn to move, it selects a move that places the game in a cold state, if such a move is available.
#
#When you are done, test to see if the following game states are hot or cold:

def is_hot(n):
	if n<2:
		is_hot_state= 'False'
	else:
		n1=n/2
		n2=n-1
		print n1
		print n2
		is_hot(n1) 
		is_hot(n2)
		is_hot_state='True'
	return is_hot_state

n = float(input())
print is_hot(n)