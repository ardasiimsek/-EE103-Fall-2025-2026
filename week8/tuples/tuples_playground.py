# Tuples: Indices and slicing
seq = (2, 'a', 4, (1, 2))

# Try these in the pdb prompt (or VSCode debug console with a breakpoint on print):
# len(seq)    -> 4
# seq[3]      -> (1, 2)
# seq[-1]     -> (1, 2)
# seq[3][0]   -> 1
# seq[4]      -> IndexError: tuple index out of range (only indices 0..3 exist)
# seq[1]      -> 'a'
# seq[-2:]    -> (4, (1, 2))
# seq[1:3]    -> ('a', 4)

print(seq)
import pdb; pdb.set_trace()
