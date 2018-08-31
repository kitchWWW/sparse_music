import random
import math

noteNames = ['c', 'cis', 'd', 'ees', 'e', 'f','fis','g','aes','a','bes','b']

def stringForNote(note,octave):
	ret = noteNames[note%12]
	direction = (math.floor(note/12) + octave)
	if direction > 0:
		ret += '\''*direction
	elif direction < 0:
		ret += ','*(-1*direction)
	return ret


stepDirections = [[-1,2], # c -> b or d
	[], # c#
	[0, 4], # d -> c or e
	[], # ees
	[2, 5], # e
	[4,7], # f
	[4,7], # fis
	[5,9], # g
	[9], # aes
	[7,11], # a
	[9,12], # bes
	[12,9], # b
	[11,14], #c
	[],
	[12,16] #d
	] 

SPECIAL = [0]
NO_ACCENT = [1]
ONES_THAT_END = [2,3,4,5]
ONES_THAT_START = [6,7,8,9]
NORMAL = [10,11,12]
decorationText = [
	'{0}1 s4 \n', #special, for last measure
	's2 {0}4 s4 \n',#no accent note
	's2 s4 {0}4 \\( \n', #ones that end
	's2 {1}4 \\( {0}4 \n',
	's8 s2 {1}8 \\( {0}4 \n',
	's8 s2 {1}4 \\( {0}8 \n',
	'{1}4 {0}4\\) s2 \n', #ones that start
	'{0}4\\) s4 s2 \n',
	'{1}4 {0}8\\) s2 s8 \n',
	'{1}8 {0}4\\) s2 s8 \n',
	's4. {1}4 \\({0}4\\) s8 \n', #normal stuff
	's4. {1}4 \\({0}8\\) s4 \n',
	's4. {1}8 \\({0}4\\) s4 \n', 
]

# decorationText = [
# 	'{0}1 s4 \n', #special, for last measure
# 	's2 {0}4 s4 \n',#no accent note
# 	's2 s4 {0}4  \n', #ones that end
# 	's2 {1}4  {0}4 \n',
# 	's8 s2 {1}8  {0}4 \n',
# 	's8 s2 {1}4  {0}8 \n',
# 	'{1}4 {0}4 s2 \n', #ones that start
# 	'{0}4 s4 s2 \n',
# 	'{1}4 {0}8 s2 s8 \n',
# 	'{1}8 {0}4 s2 s8 \n',
# 	's4. {1}4 {0}4 s8 \n', #normal stuff
# 	's4. {1}4 {0}8 s4 \n',
# 	's4. {1}8 {0}4 s4 \n', 
# ]

print("*** SPECIAL")
for i in SPECIAL:
	print(decorationText[i])
print("*** NO_ACCENT")
for i in NO_ACCENT:
	print(decorationText[i])
print("*** ONES THAT END")
for i in ONES_THAT_END:
	print(decorationText[i])
print("*** ONES THAT START")
for i in ONES_THAT_START:
	print(decorationText[i])
print("*** NORMAL")
for i in NORMAL:
	print(decorationText[i])

decorationDirections = []
# notes = [[0,5,9],
# 	[2,5,7],
# 	[4,7,9],
# 	[5,0,9],
# 	[7,10,0],
# 	[9,4,2],
# 	[11,7,6],
# 	[12,0,0]
# 	]

# notes = [
# 	[0, 0, 0],
# 	[2, 9, 0],
# 	[4, 7, 0],
# 	[5, 9, 0],
# 	[7,11, 5],
# 	[9, 2, 5],
# 	[11, 2, 5],
# 	[12,12,12]
# ]

notes = [[0,12],[9,2,5],[7],[9],[10,11],[14,2,0,4],[9,7],[14,2,12],[11,10],[8],[0]]

print("-----")
goodToGo = False
while not goodToGo:
	numbNotes = 0
	parts = []
	instLyString = []
	orderOfDecor = []
	for i in range(len(notes)):
		notePlaying = random.choice(notes[i])
		decorationIndex = random.choice(range(len(decorationText)))
		# print(str(instIndex) +': '+ str(entryNumber)+' '+ str(notePlaying)+' '+str(decorationIndex))
		if(i==0):
			decorationIndex = random.choice(NORMAL)	
		if(i==3):
			decorationIndex = random.choice(ONES_THAT_END)
		if(i==4):
			decorationIndex = random.choice(ONES_THAT_START)
		if(i>0 and orderOfDecor[i-1] in ONES_THAT_END):
			decorationIndex = random.choice(ONES_THAT_START)
		if(i==len(notes)-1):
			decorationIndex=0
		lyNotePlaying = stringForNote(notePlaying, 1)
		decorativeNote = random.choice(stepDirections[notePlaying])
		lyAccentNote = stringForNote(decorativeNote,1)
		lyString = decorationText[decorationIndex].format(lyNotePlaying,lyAccentNote )
		instLyString.append(lyString)
		orderOfDecor.append(decorationIndex)
		if(decorationIndex<3 or decorationIndex==7):
			numbNotes+=1
		else:
			numbNotes+=2

	instLyString.insert(4,'  ~ a\'4  ')
	instLyString.insert(6,'  \\break ')
	parts.append(' '.join(instLyString))



	goodToGo = True
	numbBoundries=0		
	hasNoAccent = False
	for i in range(len(notes)-1):
		if(orderOfDecor[i] in NO_ACCENT):
			hasNoAccent = True
		if(orderOfDecor[i] in SPECIAL):
			goodToGo=False
		if(orderOfDecor[i] in ONES_THAT_END):
			if(orderOfDecor[i+1] not in ONES_THAT_START):
				goodToGo = False
			else:
				numbBoundries+=1
		if(orderOfDecor[i] in ONES_THAT_START):
			if(orderOfDecor[i-1] not in ONES_THAT_END):
				goodToGo = False
		if(orderOfDecor[i] in NO_ACCENT):
			if(orderOfDecor[i+1] in NO_ACCENT):
				goodToGo=False
	if(not hasNoAccent):
		goodToGo = False
	if(orderOfDecor[9] in NO_ACCENT):
		goodToGo=False
	if(numbBoundries != 2):
		goodToGo=False
	if(orderOfDecor[3] not in ONES_THAT_END):
		goodToGo=False
	if(orderOfDecor[0] not in NORMAL):
		goodToGo=False
	# if(numbNotes!=19):
	# 	goodToGo=False
	print(numbNotes)
#insert the paren



import time
millis = int(round(time.time() * 1000))
timestamp = ''

fd = open('template.ly')
out = open('out/output_'+timestamp+'.ly','w')
for l in fd:
	if '%part' in l:
		partNo = int(l[5:])
		out.write(parts[partNo])
	elif '%time' in l:
		out.write(timestamp)
	else:
		out.write(l)
fd.close()
out.close()



