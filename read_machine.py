from collections import deque 

# machine for a+ 
def a(): 
    name = "a+"
    states = ["q0", "q1", "qaccept", "qreject"]
    sigma = ["a", "_"]
    gamma = ["a", "_"]
    start = "q0"
    accept = "qaccept"
    reject = "qreject"
    transitions = {
        # if you are in state q1 and the head reads a, go to q1 or to q2
        ("q0", "a"): [("q0", "a", "R"), ("q1", "a", "R")], 
        # accept if blank is found 
        ("q1", "_"): [("qaccept", "_", "L")], 
        # reject if after blank another symbol is found 
        ("q1", "a"): [("qreject", "a", "L")],
    }

    return name, states, sigma, gamma, start, accept, reject, transitions

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
        
    }


def trace(machine, string, max_depth=100): 
    name, states, sigma, gamma, start, accept, reject, transitions = machine()
    print("Machine: " + name)
    print("Input: " + string)
    # make a queue for bfs exploration 
    queue = deque([(string, start, 0, 0)]) 

    while queue:
        # get parent configuration from the queue 
        tape, state, head, depth = queue.popleft()
        if state == accept: 
            print(f"The string was accepted in {depth} transitions")
            return 
        if state == reject or depth >= max_depth: 
            continue 

        if head < len(tape):
            curr = tape[head]
        else: 
            curr = '_'
        # generate tree branches 
        if (state, curr) in transitions:
            for next, s, dir in transitions[(state, curr)]:
                tape2 = list(tape)
                if head < len(tape2):
                    tape2[head] = s
                else:
                    tape2.append(s)
                if dir == 'R':
                    head2 = head + 1
                else:
                    head2 = head - 1
                head2 = max(0, head2)
                queue.append((''.join(tape2), next, head2, depth+1))
    print(f"String rejected in {max_depth} transitions.")

print("Test case 1: Input = aaa\n")
trace(a, "aaa")

print("Test case 2: Input = a\n")
trace(a, "a")

print("Test case 2: Input = ""\n")
trace(a, "")

print("Test case 2: Input = b\n")
trace(a, "b")