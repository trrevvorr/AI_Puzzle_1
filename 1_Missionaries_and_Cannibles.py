# AI - CS 5400 - Sec 1A
# Puzzle Assignmet 1 - Missionaries and Cannibals 
#
# Trevor Ross
# 01/22/2016
import random

class MC_Puzle(object):
	"""docstring for Puzzle"""
	def __init__(self):
		# each state takes the format [ml, cl, mr, cr] or [ml, cl, mr, cr, b] where:
			# ml = number of missionaries on the left bank
			# cl = number of cannibals on the left bank
			# mr = number of missionaries on the right bank
			# cr = number of cannibals on the right bank
			# b = possition of boat (either l or r) [OPTIONAL]

		# Initial state is all misionaries and cannibals on the left side
		self.state = [3,3,0,0,'l']
		# how many times the boat crosses the river
		self.moves = 0
		# a boat can either be on the left (l) side or the right (r) side
		self.boat = 'l'
		# keep track of all the states so the solution can be printed 
		self.past_states = []
		# these are dead end states, BACKTRACK() function fills this array
		self.trash_states = []
		# store all valid states in order to check if an action is valid
		self.valid_states = [[3,3,0,0], [3,2,0,1], [3,1,0,2], [3,0,0,3],
							[2,2,1,1], 
							[1,1,2,2],
							[0,0,3,3], [0,1,3,2], [0,2,3,1], [0,3,3,0]]
		# available actions to take, defaults to boat moving left to right
		self.legal_actions = {'m1c1':[-1,-1,1,1], # move one missionary and one cannibal
							  'm1c0':[-1,0,1,0], # move one missionary
							  'm2c0':[-2,0,2,0], # move two missionary
							  'm0c1':[0,-1,0,1], # move one cannibal
							  'm0c2':[0,-2,0,2]} # move two cannibal


	# PURPOSE: Returns a list of all valid actions that can be performed at the 
	# given state. To be "valid", a state must be a 1) member of the valid_states 
	# set, 2) not be in the set of past_states, and 3) not be in the set of trash states
	# INPUT: state in the format: [ml,cl,mr,cr] or [ml,cl,mr,cr,b]
	# OUTPUT: list of actions in the form 'mxcy' where x,y = [0,2]
	def ACTIONS(self, s):
		valid_actions = []

		# find all possible resulting states
		# one missionary, one cannible 
		m1c1 = self.RESULT(s,'m1c1')
		# one missionary
		m1c0 = self.RESULT(s,'m1c0')
		# two missionary
		m2c0 = self.RESULT(s,'m2c0')
		# one cannible 
		m0c1 = self.RESULT(s,'m0c1')
		# two cannible 
		m0c2 = self.RESULT(s,'m0c2')

		# eliminate invalid resulting states
		if m1c1[:4] in self.valid_states and m1c1 not in (self.past_states + self.trash_states):
			valid_actions.append('m1c1')
		if m1c0[:4] in self.valid_states and m1c0 not in (self.past_states + self.trash_states):
			valid_actions.append('m1c0')
		if m2c0[:4] in self.valid_states and m2c0 not in (self.past_states + self.trash_states):
			valid_actions.append('m2c0')
		if m0c1[:4] in self.valid_states and m0c1 not in (self.past_states + self.trash_states):
			valid_actions.append('m0c1')
		if m0c2[:4] in self.valid_states and m0c2 not in (self.past_states + self.trash_states):
			valid_actions.append('m0c2')

		return valid_actions


	# PURPOSE: returns the resulting state given the a state and the action to 
	# be perfomed on it
	# INPUT: can be passed a state in the form: [ml,cl,mr,cr] or [ml,cl,mr,cr,b]
	# action must be passed in the form 'mxcy'
	# OUTPUT: returns a state in the form: [ml,cl,mr,cr,b]
	def RESULT(self, s, a):
		action_array = self.legal_actions[a]
		new_state = s[:]

		# Deal with possition of boat and format of passed state
		if len(s) == 5:
			boat_state = s[4]
		else:
			boat_state = self.boat
			new_state.append(boat_state)

		# Take action on passed state
		# if the boat is moving from LEFT TO RIGHT
		if boat_state == 'l': 
			for i in xrange(4):
				new_state[i] = new_state[i] + action_array[i]
			new_state[4] = 'r'
		# if the boat is moving from RIGHT TO LEFT
		elif boat_state == 'r': 
			for i in xrange(4):
				new_state[i] = new_state[i] - action_array[i]
			new_state[4] = 'l'
		else: print 'ERROR: BOAT IN INVALID POSSITION: %s' % self.boat

		return new_state


	# PURPOSE: prints out state it is passed in a visual format
	# passing an action is optional but doing so will print s as
	# well as the resulting state after the action is taken
	# FORMAT: m = missionarry, c = cannibal
	# \~~~|
	# /~~~|	<- river with boat on left bank
	def VISUALIZE(self, s, a=[]):
		tl,bl,tr,br = '|','|','|','|'
		# used to draw boat direction
		if len(s) == 5:
			if s[4] == 'l': 
				tl,bl = '\\','/'
				tr,br = '|','|'
			elif s[4] == 'r': 
				tl,bl = '|','|'
				tr,br = '/','\\'
		# print the state of the river
		print 'm'*s[0],' '*(3-s[0]),'%s~~~%s'%(tl,tr),' '*(3-s[2]),'m'*s[2]
		print 'c'*s[1],' '*(3-s[1]),'%s~~~%s'%(bl,br),' '*(3-s[3]),'c'*s[3]
		print '-'*15
		# print the river after the action if passed one
		if len(a):
			print "-- ACTION --"
			self.VISUALIZE(self.RESULT(s,a))


	# PURPOSE: prints out the solution set (actions) in easy-to-understand sentences
	# call once after the AI has finished finding the solution
	def VERBALIZE(self):
		turn_count = 1
		print "== ACTIONS =="

		# iterate through each state in past_states, deducing what action was taken
		for i in xrange(len(self.past_states)-1):
			old_state = self.past_states[i]
			new_state = self.past_states[i+1]
			# extract boat info
			if old_state[4] == 'l':
				boat_move = 'left to right'
			else:
				boat_move = 'right to left'
			# extract move info
			for action in self.legal_actions:
				if new_state == self.RESULT(old_state, action):
					break
			# print the sentence
			print 'Turn %d: The boat moved from %s carrying %s missionary(s) and %s cannibal(s)' % (turn_count, boat_move, action[1], action[3])
			turn_count += 1


	# PURPOSE: plays the puzzle game until it wins
	# INPUT: none, it will begin the puzzle at the initial state
	# OUTPUT: builds an array of "past_states" which are the states it visted
	# on the way to the solution.
	# Also builds trash_states array which are the dead-end states it encountered
	def SIMULATE(self):
		while not self.FINAL(self.state):
			# save the current state to the list of past states
			self.past_states.append(self.state)
			# find the valid actions for the current state
			valid_actions = self.ACTIONS(self.state)
			# backtrack if there are no valid actions (dead-end)
			if len(valid_actions)==0:
				self.BACKTRACK()
				continue
			# choose a random valid action
			random.shuffle(valid_actions)
			next_action = valid_actions[0]
			# take the choosen action
			self.state = self.RESULT(self.state, next_action)
			self.MOVE_BOAT()
		# append the final state
		self.past_states.append(self.state)

		# print the resulting solution set
		for s in self.past_states:
			self.VISUALIZE(s)
		self.VERBALIZE()

		print "YOU WIN!"


	def BACKTRACK(self):
		# remove the dead end state and add it to the trash states
		dead_end = self.past_states.pop(-1)
		self.trash_states.append(dead_end)
		# move back one state
		self.state = self.past_states.pop(-1)
		self.MOVE_BOAT()


	# PURPOSE: simply sqitches the boat's possition from r to l or l to r
	def MOVE_BOAT(self):
		if self.boat == 'l': self.boat='r'
		elif self.boat == 'r': self.boat='l'


	# PURPOSE: return true if final state has been reached, false otherwise
	# INPUT: accepts state s in either form: [ml,cl,mr,cr] or [ml,cl,mr,cr,b]
	def FINAL(self,s):
		if s[:4] == [0,0,3,3]:
			return True
		else:
			return False



################################################################################
### MAIN
################################################################################
random.seed()
puzzle = MC_Puzle()
puzzle.SIMULATE()
















		