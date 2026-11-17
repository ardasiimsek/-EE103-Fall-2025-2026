# Lists: Indices and slicing
seq = [2, 'a', 4, [1, 2]]

# Try these in the pdb prompt (or VSCode debug console with a breakpoint on print):
# len(seq)    -> 4
# seq[3]      -> [1, 2]
# seq[-1]     -> [1, 2]
# seq[3][0]   -> 1
# seq[4]      -> IndexError: list index out of range
# seq[1]      -> 'a'
# seq[-2:]    -> [4, [1, 2]]
# seq[1:3]    -> ['a', 4]
# Same as the tuple version, but slices give back lists instead of tuples.

print(seq)
import pdb; pdb.set_trace()
