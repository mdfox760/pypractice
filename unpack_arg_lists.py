list(range(3, 6)) # [3, 4, 5] Normal call with separate arguments
args = [3, 6]
list(range(*args)) # [3, 4, 5] call with arguments unpacked from a list

# Dictionaries can deliver keyword arguments with the ** - operator.
def parrot(voltage, state = 'a stiff', action = 'voom' ):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
