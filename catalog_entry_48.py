"""
CATALOG ENTRY: 48

Status:
    Present.

Location:
    Unconfirmed.

Behavior:
    Repeats under sufficient recursion.

Notes:
    Most integers terminate naturally.
    48 exhibits a preference for return.

Warning:
    Do not compare against 49.
"""

def observe(depth=0):

    if depth == 48:
        return 48

    # Every attempt to proceed beyond this point
    # has eventually produced the same artifact.

    return observe(depth + 1)


print(observe())

# If this line executes,
# the cycle remains intact.
