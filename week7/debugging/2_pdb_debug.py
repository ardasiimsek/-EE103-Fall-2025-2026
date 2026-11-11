# Debugging - Part 2: interactive terminal debugging with pdb
# Run in a terminal:  python 2_pdb_debug.py
#
# Useful pdb commands at the (Pdb) prompt:
#   p num, p count   -> print the value of a variable
#   n  (next)        -> run the next line (does not enter function calls)
#   s  (step)        -> step into a function call
#   c  (continue)    -> run until the next breakpoint / set_trace()
#   b 20             -> set a breakpoint at line 20 (b alone lists breakpoints)
#   l  (list)        -> show the code around the current line
#   q  (quit)        -> stop debugging
#
# Note: variables named b, c, n clash with these shortcuts, so this script
# uses input_n / num / count. To print such a variable use "p n" or "!n".
def count_evens(input_n):
    count = 0
    for num in range(input_n):
        # Execution will pause every time the loop reaches this line!
        import pdb; pdb.set_trace()
        if num % 2 == 0:
            count += 1
    return count


print("Total evens:", count_evens(5))
