# AI - CS 5400 - Sec 1A
# Puzzle Assignmet 1 - Missionaries and Cannibals 
#
# Trevor Ross
# 01/22/2016
import random

class River(object):
	"""docstring for Puzzle"""
	def __init__(self):
		# each state takes the format [ml, cl, mr, cr] where:
			# ml = number of missionaries on the left bank
			# cl = number of cannibals on the left bank
			# mr = number of missionaries on the right bank
			# cr = number of cannibals on the right bank

		# Initial state is all misionaries and cannibals on the left side
		self.state = [3,3,0,0]
		# how many times the boat crosses the river
		self.moves = 0
		# a boat can either be on the left (l) side or the right (r) side
		self.boat = 'l'
		# keep track of all the states so the solution can be printed 
		self.past_states = [[0,0,0,0],[0,0,0,0]]
		# store all valid states in order to check if an action is valid
		self.valid_states = [[3,3,0,0], [3,2,0,1], [3,1,0,2], [3,0,0,3],
							[2,2,1,1], 
							[1,1,2,2],
							[0,0,3,3], [0,1,3,2], [0,2,3,1], [0,3,3,0]]
		# available actions to take, defaults to boat moving left to right
		self.avail_actions = {'m1c1':[-1,-1,1,1], # move one missionary and one cannibal
							  'm1c0':[-1,0,1,0], # move one missionary
							  'm2c0':[-2,0,2,0], # move two missionary
							  'm0c1':[0,-1,0,1], # move one cannibal
							  'm0c2':[0,-2,0,2]} # move two cannibal


	def ACTIONS(self, s):
		valid_actions = []

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

		# check if the moves are valid
		if m1c1 in self.valid_states and m1c1 != self.past_states[-1] and m1c1 != self.past_states[-2]:
			valid_actions.append('m1c1')
		if m1c0 in self.valid_states and m1c0 != self.past_states[-1] and m1c0 != self.past_states[-2]:
			valid_actions.append('m1c0')
		if m2c0 in self.valid_states and m2c0 != self.past_states[-1] and m2c0 != self.past_states[-2]:
			valid_actions.append('m2c0')
		if m0c1 in self.valid_states and m0c1 != self.past_states[-1] and m0c1 != self.past_states[-2]:
			valid_actions.append('m0c1')
		if m0c2 in self.valid_states and m0c2 != self.past_states[-1] and m0c2 != self.past_states[-2]:
			valid_actions.append('m0c2')

		return valid_actions


	def RESULT(self, s, a):
		action_array = self.avail_actions[a]
		new_state = s[:]

		# if the boat is moving from left to right
		if self.boat == 'l': 
			for i in xrange(4):
				new_state[i] = new_state[i] + action_array[i]

		# if the boat is moving from right to left
		elif self.boat == 'r': 
			for i in xrange(4):
				new_state[i] = new_state[i] - action_array[i]
		else:
			print 'ERROR: BOAT IN INVAlID POSSITION: %s' % self.boat

		return new_state


	def Visualize(self, s, a=[]):
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
			self.Visualize(self.RESULT(s,a))

	def SIMULATE(self):
		while not self.FINAL(self.state):
			# find the valid actions and pick a random one
			valid_actions = self.ACTIONS(self.state)
			if len(valid_actions)==0:
				# break if there are no valid options
				break
			random.shuffle(valid_actions)
			next_action = valid_actions[0]
			# save the current state to the list of states
			self.past_states.append(self.state + [self.boat])
			# take the choosen action
			self.state = self.RESULT(self.state, next_action)
			self.MOVE_BOAT()

		# print the resulting solution set
		for s in self.past_states:
			self.Visualize(s)
		self.Visualize(self.state)

		if self.FINAL(self.state):
			print "YOU WIN!"
		else:
			print "NO VALID ACTIONS FOUND"


	def MOVE_BOAT(self):
		if self.boat == 'l': self.boat='r'
		elif self.boat == 'r': self.boat='l'


	def FINAL(self,s):
		if s == [0,0,3,3]:
			return True
		else:
			return False



################################################################################
### MAIN
################################################################################
r1 = River()
r1.SIMULATE()















		