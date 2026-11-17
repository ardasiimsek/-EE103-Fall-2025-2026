L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
print(f"L4 = {L4}")

L3.append(L4)
print(f"L3 = {L3}")

L = L1.append(L3)
print(f"L  = {L}")
print(f"L1 = {L1}")

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
notes.sort()
print(notes)
notes.clear()
print(notes)
