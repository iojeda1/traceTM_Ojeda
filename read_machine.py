from collections import deque 

# machine for aa+ 
def aa():
    name = "aa+"
    states = ["q0", "q1", "qaccept", "qreject"]
    sigma = ["a", "_"]
    gamma = ["a", "_"]
    start = "q0"
    accept = "qaccept"
    reject = "qreject"
    transitions = {
        ("q0", "a"): [("q1", "a", "R")], 
        ("q0", "_"): [("qreject", "_", "R")], 
        ("q1", "a"): [("q1", "a", "R")], 
        ("q1", "_"): [("qaccept", "_", "R")], 
    }
    return name, states, sigma, gamma, start, accept, reject, transitions

# a+ machine for testing 
def a(): 
    name = "a+"
    states = ["q0", "q1", "q2", "qaccept", "qreject"]
    sigma = ["a", "_"]
    gamma = ["a", "_"]
    start = "q0"
    accept = "qaccept"
    reject = "qreject"
    transitions = {
        # if you are in state q1 and the head reads a, go to q1 or to q2
        ("q0", "a"): [("q1", "a", "R"), ("q2", "a", "R")], 
        ("q0", "_"): [("qreject", "_", "R")],
        # accept if blank is found 
        ("q1", "a"): [("q1", "a", "R")],
        ("q1", "_"): [("q2", "_", "L")], 
        # reject if after blank another symbol is found 
        ("q2", "_"): [("qaccept", "_", "L")],
        ("q2", "a"): [("qaccept", "a", "L")],
    }

    return name, states, sigma, gamma, start, accept, reject, transitions

def trace(machine, string, max_depth=100, max_transitions=200, debug=False): 
    name, states, sigma, gamma, start, accept, reject, transitions = machine()
    print("Machine: " + name)
    print("Initial string: " + string)
    # make a queue for bfs exploration 
    queue = deque([(string, start, 0, 0)]) 
    transitions_total = 0
    while queue:
        # get parent configuration from the queue 
        tape, state, head, depth = queue.popleft()
        transitions_total += 1
        if debug:
            print('\n')
            print(f"Step: {transitions_total}")
            print(f"State: {state}")
            print(f"Head: {head}")
            print(f"Tape: {tape}")
            print(f"Depth: {depth}")
        if transitions_total > max_transitions:
            print(f"\nExecution stopped after reaching {max_transitions} max transitions.")
            return 
        if depth >= max_depth: 
            print(f"\nExecution stopped after reaching {max_depth} max depth.")
            return 
        if state == accept: 
            print(f"\nThe string was accepted in {depth} transitions.")
            print(f"The depth is: {depth}")
            print(f"Total transitions: {transitions_total-1}")
            left = tape[:head]
            if head + 1 < len(tape):
                right = tape[head+1:]
            else: 
                right = "_"
            if head < len(tape):
                curr_c = tape[head]
            else:
                curr_c = "_"
            print(f"Step {depth}: Left: {left} | State: {state} | Head: {curr_c} | Right: {right}")
            return 
        if state == reject: 
            print(f"\nThe string was rejected in {depth} transitions.")
            print(f"The depth is: {depth}")
            print(f"Total transitions: {transitions_total-1}")
            left = tape[:head]
            if head + 1 < len(tape):
                right = tape[head+1:]
            else: 
                right = "_"
            if head < len(tape):
                curr_c = tape[head]
            else:
                curr_c = "_"
            print(f"Step {depth}: Left: {left} | State: {state} | Head: {curr_c} | Right: {right}")
            return 
            
        if head < len(tape): # current head character 
            curr = tape[head]
        else: 
            curr = '_'
        # generate tree branches 
        if (state, curr) in transitions:
            for next, s, dir in transitions[(state, curr)]:
                print(f"Transition: ({state}, {curr}) -> ({next}, {s}, {dir})")
                tape2 = list(tape)
                if head < len(tape2):
                    tape2[head] = s
                else:
                    tape2.append(s)
                # update head 
                if dir == 'R':
                    head2 = head + 1
                else:
                    head2 = head - 1
                head2 = max(0, head2)
                queue.append((''.join(tape2), next, head2, depth+1))
    print(f"Execution stopped without accept or reject after {transitions_total}.\n") 

# handle multiple strings 


# test cases 
print("Test case 1: Input = aaa\n")
trace(aa, "aaa", debug=True)

print ("\n")

print("Test case 2: Input = aaaa\n")
trace(aa, "aaaa", debug=True)

print ("\n")

print("Test case 3: Input = ""\n")
trace(aa, "", debug=True)

print ("\n")

print("Test case 4: Input = b\n")
trace(aa, "b", debug=True)


print("Test case 5: Input = aaaaa\n")
trace(a, "aaaaa", max_depth=15, max_transitions=15, debug=True)
'''

# Test cases
print("Test case 1: Input = aaa\n")
trace(a, "aaa", max_depth=100, max_transitions=100, debug=True)

print("\nTest case 2: Input = aaaa\n")
trace(a, "aaaa", max_depth=100, max_transitions=100, debug=True)

print("\nTest case 3: Input = aaaaa\n")
trace(a, "aaaaa", max_depth=100, max_transitions=100, debug=True)

print("\nTest case 4: Input = ''\n")
trace(a, "", max_depth=100, max_transitions=100, debug=True)

print("\nTest case 5: Input = b\n")
trace(a, "b", max_depth=100, max_transitions=100, debug=True)
'''