from collections import deque
import csv

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

def trace(machine, string, max_depth=100, max_transitions=200, debug=False): 
    name, states, sigma, gamma, start, accept, reject, transitions = machine()
    print("Machine: " + name)
    print("Initial string: " + string)
    # make a queue for bfs exploration 
    queue = deque([(string, start, 0, 0, [])])  # Add a path tracker in each queue entry
    transitions_total = 0
    while queue:
        # get parent configuration from the queue 
        tape, state, head, depth, path = queue.popleft()
        path.append((tape, state, head))  # Track the current configuration
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
            print("\nPath to accept:")
            for d, (t, s, h) in enumerate(path):
                # Safely access tape characters, treating out-of-bounds as "_"
                head_char = t[h] if h < len(t) else "_"
                right = t[h+1:] if h+1 < len(t) else "_"
                print(f"Level {d}: Left: {t[:h]} | State: {s} | Head: {head_char} | Right: {right}")
            return 
        if state == reject: 
            print(f"\nThe string was rejected in {depth} transitions.")
            print(f"The depth is: {depth}")
            print(f"Total transitions: {transitions_total-1}")
            return 
        if head < len(tape):  # Current head character
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
                queue.append((''.join(tape2), next, head2, depth+1, path[:]))
    print(f"Execution stopped without accept or reject after {transitions_total}.\n")

# Test cases
print("Test case 1: Input = aaa\n")
trace(aa, "aaa", debug=True)

print("\nTest case 2: Input = aaaa\n")
trace(aa, "aaaa", debug=True)

print("\nTest case 3: Input = ''\n")
trace(aa, "", debug=True)

print("\nTest case 4: Input = b\n")
trace(aa, "b", debug=True)

print("\nTest case 5: Input = aaaaa\n")
trace(a, "aaaaa", max_depth=15, max_transitions=15, debug=True)
