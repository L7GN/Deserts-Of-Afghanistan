import os
import random
import time
import sys

os.system('pip install getch')
os.system('clear')


locations = [
    "Main stage", "Party room", "Backstage", "Restrooms", "Kitchen",
    "West hall", "W. hall corner", "Left hall", "E. hall corner", "Closet",
    "Office", "Pirates cove"
]

at_main_stage = ["Bonnie", "Chica", "Freddy"]
at_party_room = []
at_backstage = []
at_restrooms = []
at_kitchen = []
at_west_hall = []
at_whall_corner = []
at_east_hall = []
at_ehall_corner = []
at_closet = []
at_office = []
at_pirates_cove = ["Foxy"]
alive = True
playing = True
night = 1
clock = 12
power = 100
score = 0
seconds = 0
custom205 = False
door1 = False
door2 = False
timer1 = 0
timer2 = 0
check1 = 0
check2 = 0

phone_guy = {
    "message1": [
        "Hello and welcome to your new job as a night guard at Freddy Fazbear's pizza! ",
        "You are working at the office I was working in. ",
        "Im actually finishing up my last night right now.",
        "Anyway, I left these messages for you so I can tell you what happens during the night. ",
        "To prevent their servos from locking up, the animatronics are set to a \"free roaming\" mode at night.",
        "Unfortunately, if they see you they'll think that you are a metal endoskeleton without a suit.",
        "Now since thats not allowed here, they might try to...",
        "Forcefully stuff you inside a Freddy Fazbear suit.",
        "The springlocks would release and would shoot pieces of metal inside of you...",
        "The only parts of you that would see the light of day again would be...",
        "Your eyeballs and teeth as they pop out the front of the mask.",
        "Yeah they don't tell you this stuff when you sign up...",
        "Anyway, if you see an animatronic at the door, close it. It will eventually wander away.",
        "Using your cameras, door, or doorlight will decrease your power.",
        "And if you run out of power, there's nothing to stop the animatronics from getting to you.",
        "So anyway, don't get caught, and I'll leave you another message tomorrow",
        "Good luck. "
    ],
    "message2": ["Hey, congratulations on finishing your first night!", ""]
}


def clear():
	os.system('clear')


def jumpscare(an):
	global night, clear
	for i in range(10):
		clear()
		time.sleep(.07)
		print("""
		███████▀▀▀░░░░░░░▀▀▀███████
		██████▀░░░░░░░░░░░░░░░▀████
		█████│░░░░░░░░░░░░░░░░│████
		████└┐░░░░░░░░░░░░░░░┌┘░███
		███░░└┐░░░░░░░░░░░░░░┌┘░░██
		███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
		██▌░▄██████▄░░░▄██████▄░▐██
		███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███
		██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██
		██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███
		████▄─┘█████████████└─▄████
		█████░░▐███████████▌░░█████
		██████░░▀█████████▀░░▐█████
		███████░░░░▓▓▓▓▓░░░░▄██████
		████████▄░░░░░░░░░▄████████
		███████████▓▓▓▓▓███████████
		███████████▓▓▓▓▓███████████

████╗████████╗██╗███████╗ ███╗═══███╗████████╗
═██╔╝═══██╔══╝╚█║██╔════╝ ████╗═████║██╔═════╝
═██║════██║════╚╝███████╗ ██╔████╔██║█████╗
═██║════██║══════╚════██║ ██║╚██╔╝██║██╔══╝
████╗═══██║══════███████║ ██║═╚═╝═██║███████╗
		""")
		time.sleep(.07)
	try:
		print(f"You were jumpscared by {an.name}!")
	except:
		print(f"You were jumpscared by {an}!")

	input()
	print(f'You made it to night {night}.')
	import Winter


def running():
	guesses = 0
	global Foxy, jumpscare, power
	foxy = Foxy()
	while True:
		if guesses == 3:
			jumpscare("Foxy")
		print('FOXY IS COMING!')
		uh_oh = random.randint(1, 3)
		guess = input('Pick a number 1-3: ')
		if guess != str(uh_oh):
			guesses += 1
			print('Foxy is still running!')
		else:
			print('You stopped foxy!')
			foxy.caught()
			break


def loss():
	print('~~~~~~~~~')
	print('POWER: 0')
	print('~~~~~~~~~')
	r = random.randint(3, 6)
	time.sleep(r)
	jumpscare("Freddy")


class Chica:
	def __init__(self):
		self.path = [
		    "Main stage", "Party room", "Restroom", "Kitchen", "East hall",
		    "E. hall corner", "Office"
		]
		self.moved = 0
		self.current = self.path[self.moved]
		self.aggression = 0
		self.name = "Chica"

	def move(self):
		self.moved += 1
		self.current = self.path[self.moved]

	def caught(self):
		self.moved = 0
		self.current = self.path[0]

	def reset(self, aggression):
		self.moved = 0
		self.current = self.path[0]
		self.aggression = aggression


class Bonnie:
	def __init__(self):
		self.path = [
		    "Main stage", "Party room", "Backstage", "Closet", "West hall",
		    "W. hall corner", "Office"
		]
		self.moved = 0
		self.current = self.path[self.moved]
		self.aggression = 0
		self.name = "Bonnie"

	def move(self):
		self.moved += 1
		self.current = self.path[self.moved]

	def caught(self):
		self.moved = 0
		self.current = self.path[0]

	def reset(self, aggression):
		self.moved = 0
		self.current = self.path[0]
		self.aggression = aggression


class Freddy:
	def __init__(self):
		self.path = [
		    "Main stage", "Party room", "Restroom", "Kitchen", "West hall",
		    "W. hall corner", "Office"
		]
		self.moved = 0
		self.current = self.path[self.moved]
		self.aggression = 0
		self.name = "Freddy"

	def move(self):
		self.moved += 1
		self.current = self.path[self.moved]

	def caught(self):
		self.moved = 0
		self.current = self.path[0]

	def reset(self, aggression):
		self.moved = 0
		self.current = self.path[0]
		self.aggression = aggression


class Foxy:
	def __init__(self):
		self.path = ["Pirates cove", "West hall", "office"]
		self.moved = 0
		self.current = self.path[self.moved]
		self.aggression = 0
		self.name = "Foxy"

	def move(self):
		self.moved += 1
		self.current = self.path[self.moved]

	def caught(self):
		self.moved = 0
		self.current = self.path[0]

	def reset(self, aggression):
		self.moved = 0
		self.current = self.path[0]
		self.aggression = aggression


def camera():
	global at_main_stage, at_party_room, at_backstage, at_restrooms, at_kitchen, at_west_hall, at_whall_corner, at_closet, at_office, at_pirates_cove, chica, bonnie, freddy, foxy, running, power
	print(f'chica: {chica.current}')
	print(f'bonnie: {bonnie.current}')
	if foxy.current != "Pirates cove":
		running()
	else:
		print(f"foxy: Pirates cove")
	print(f'freddy: type f to find')
	power -= 5
	ree = input()
	print()
	if ree.lower() == 'f':
		print(f"Freddy is at the {freddy.current}")
		power -= 2
		input()


chica = Chica()
bonnie = Bonnie()
freddy = Freddy()
foxy = Foxy()
active = []
animatronics = [chica, bonnie, freddy, foxy]

while playing:
	if night == 7:
		clear()
		print('GREAT!')
		print('Now get out.')
		time.sleep(2)
		print('You\'re fired.')
		print('Reasons: ')
		print('Odor, tampering with the animatronics.')
		input()
		sys.exit()
	if night == 1:
		active = [chica, bonnie]
		chica.reset(4)
		bonnie.reset(4)
		freddy.reset(0)
		foxy.reset(0)
	elif night == 2:
		active = [chica, bonnie, foxy]
		chica.reset(6)
		bonnie.reset(7)
		freddy.reset(0)
		foxy.reset(1)
	elif night == 3:
		active = [chica, bonnie, foxy, freddy]
		chica.reset(8)
		bonnie.reset(10)
		freddy.reset(3)
		foxy.reset(1)
	elif night == 4:
		active = [chica, bonnie, foxy, freddy]
		chica.reset(10)
		bonnie.reset(10)
		freddy.reset(8)
		foxy.reset(2)
	elif night == 5:
		active = [chica, bonnie, foxy, freddy]
		chica.reset(12)
		bonnie.reset(12)
		freddy.reset(10)
		foxy.reset(3)
	elif night == 6:
		active = [chica, bonnie, foxy, freddy]
		chica.reset(12)
		bonnie.reset(14)
		freddy.reset(14)
		foxy.reset(4)
	print(f'NIGHT {night}')
	input()
	print('(type "mute" to mute)')
	print()
	call = f"message{night}"
	for i in range(len(phone_guy[call])):
		print(phone_guy[call][i])
		xor = input()
		if xor.lower() == 'mute':
			break
	clear()
	while True:
		if clock == 6:
			night += 1
			print('~~~~~~~')
			print('6:00 am')
			print('~~~~~~~')
			time.sleep(3)
			clock = 12
			door1 = False
			door2 = False
			power = 100
			break
		if door1:
			power -= 5
		if door2:
			power -= 5
		for x in animatronics:
			if x.current == "Main stage":
				at_main_stage.append(x.name)
			else:
				try:
					at_party_room.remove(x.name)
				except:
					pass
			if x.current == "Party room":
				at_party_room.append(x.name)
			else:
				try:
					at_party_room.remove(x.name)
				except:
					pass
			if x.current == "Backstage":
				at_backstage.append(x.name)
			else:
				try:
					at_backstage.remove(x.name)
				except:
					pass
			if x.current == "Restrooms":
				at_restrooms.append(x.name)
			else:
				try:
					at_restrooms.remove(x.name)
				except:
					pass
			if x.current == "Kitchen":
				at_kitchen.append(x.name)
			else:
				try:
					at_kitchen.remove(x.name)
				except:
					pass
			if x.current == "West hall":
				at_west_hall.append(x.name)
			else:
				try:
					at_west_hall.remove(x.name)
				except:
					pass
			if x.current == "W. hall corner":
				at_whall_corner.append(x.name)
			else:
				try:
					at_whall_corner.remove(x.name)
				except:
					pass
			if x.current == "East hall":
				at_east_hall.append(x.name)
			else:
				try:
					at_east_hall.remove(x.name)
				except:
					pass
			if x.current == "E. hall corner":
				at_ehall_corner.append(x.name)
			else:
				try:
					at_ehall_corner.remove(x.name)
				except:
					pass
			if x.current == "Closet":
				at_closet.append(x.name)
			else:
				try:
					at_closet.remove(x.name)
				except:
					pass
			if x.current == "Pirates cove":
				at_pirates_cove.append(x.name)
			else:
				try:
					at_pirates_cove.remove(x.name)
				except:
					pass
		if at_office != []:
			for i in at_office:
				jumpscare(i)
		for anim in active:
			agr = int(anim.aggression)
			mv = random.randint(1, 30)
			#print(f'1-{agr} and its {mv}') #DEBUGGER
			if mv in range(1, agr):
				anim.move()
				#print(f'{anim.name} moved to {anim.current}') #DEBUGGER
		if power <= 0:
			loss()
		#for i in animatronics: #DEBUGGER
		#print(f"{i}: {i.current}") #DEBUGGER
		print()
		dis = True
		while dis:
			print(f'{clock}:00 am')
			print(f'Power: {power}')
			print('L: check left door\nR: check right door\nC: cameras')
			print('space: continue')
			if door1:
				print('(left door closed)')
			if door2:
				print('(right door closed)')
			option = input()
			print()
			option = option.lower()
			if option == 'c':
				camera()
				clear()
			elif option == 'l':
				if at_whall_corner != []:
					for i in at_whall_corner:
						print(f"{i} Is there!")
				else:
					print('Nothing here...')
				print('c to close door, o to open')
				ha = input()
				if ha.lower() == 'c' and not door1:
					door1 = True
				elif ha.lower() == 'o' and door1:
					door1 = False
				power -= 1
			elif option == 'r':
				if at_ehall_corner != []:
					for i in at_ehall_corner:
						print(f"{i} Is there!")
				else:
					print('Nothing here...')
				print('c to close door, o to open')
				ha = input()
				if ha.lower() == 'c' and not door2:
					door2 = True
				elif ha.lower() == 'o' and door2:
					door2 = False
				power -= 1
			elif option in ['', ' ']:
				dis = False
			print()

		print()
		seconds += 1
		if seconds == 10:
			clock += 1
			seconds = 0

		if at_whall_corner != []:
			for i in animatronics:
				if i.current == "W. hall corner" and not door1:
					jumpscare(i)
				elif i.current == "W. hall corner" and door1:
					i.caught()
		if at_ehall_corner != []:
			for i in animatronics:
				if i.current == "E. hall corner" and not door2:
					jumpscare(i)
				elif i.current == "E. hall corner" and door1:
					i.caught

		if clock == 13:
			clock = 1

		clear()
		#power -= 1
