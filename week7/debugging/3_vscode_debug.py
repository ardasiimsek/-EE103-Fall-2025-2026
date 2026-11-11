# Debugging - Part 3: graphical debugging in VS Code
#
# 1) Open this file in VS Code.
# 2) Hover left of the line "if num % 2 == 0:" and click to set a
#    breakpoint (solid red dot).
# 3) Press F5 (or Run and Debug -> Python File).
# 4) Watch input_n, count and num in the VARIABLES panel on the left.
# 5) Try the debug bar buttons:
#       Continue  (F5)            -> run to the next breakpoint
#       Step Over (F10)           -> run the current line
#       Step Into (F11)           -> go inside a function call
#       Step Out  (Shift+F11)     -> finish the current function
#       Restart   (Ctrl+Shift+F5)
#       Stop      (Shift+F5)
def count_evens(input_n):
    count = 0
    for num in range(input_n):
        if num % 2 == 0:          # <-- put the breakpoint here
            count += 1
    return count


print("Total evens:", count_evens(5))
