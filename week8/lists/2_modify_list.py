# Lists: Modify a list

# Part 1: Define and append
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2              # + makes a NEW list: ['re', 'mi']
print(f"L4 = {L4}")

L3.append(L4)             # the whole list is added as ONE element
print(f"L3 = {L3}")       # ['do', ['re', 'mi']]

L = L1.append(L3)         # append changes L1 in place and returns None
print(f"L  = {L}")        # None
print(f"L1 = {L1}")       # ['re', ['do', ['re', 'mi']]]

# Part 2: Step-by-step modifications
notes = ['do', 're', 'mi']
notes.extend(['fa', 'sol', 'la', 'si'])
print(notes)
notes.insert(6, 'ti')
print(notes)
notes[0] = 'DO'
print(notes)
notes[1:3] = ['RE', 'MI']
print(notes)
notes.remove('ti')
print(notes)
last_note = notes.pop()
print(notes, "last_note =", last_note)
notes.pop(2)
print(notes)
del notes[0]
print(notes)
notes.reverse()
print(notes)
notes.sort()              # uppercase comes before lowercase in ASCII
print(notes)
notes.clear()
print(notes)
