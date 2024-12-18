# Team Ojeda 
import csv
def read_csv(file_path):
    # read the CSV file for a+ machine 
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        lines = [row for row in reader if row]
    machine_name = lines[0][0]
    states = lines[1]
    input = lines[2]
    tape = lines[3]
    start = lines[4][0]
    accept = lines[5][0]
    reject = lines[6][0]
    # parse transitions
    transitions = {}
    for transition_line in lines[7:]:
        curr, input, next, write, direction = transition_line
        key = (curr, input)
        if key not in transitions:
            transitions[key] = []
        transitions[key].append((next, write, direction))
    machine = {
        "name": machine_name,
        "states": states,
        "input": input,
        "tape": tape,
        "start": start,
        "accept": accept,
        "reject": reject,
        "transitions": transitions,
    }
    return machine
def ntm(machine, input_string, max_depth):
    name = machine["name"]
    states = machine["states"]
    start = machine["start"]
    accept = machine["accept"]
    reject = machine["reject"]
    transitions = machine["transitions"]
    tree = []  
    parents = {}  
    initial_config = ("", start, input_string)
    tree.append([initial_config])
    parents[initial_config] = None  
    count = 0
    accepted_config = None
    #print(f"Machine Name: {name}")
    print(f"Initial Configuration: {initial_config}\n")
    while tree and count < max_depth:
        curr_level = tree[-1]
        next_level = []
        print(f"Depth {count}: Current Level Configurations: {curr_level}")
        for left, state, tape in curr_level:
            # Check if accept or reject states are found
            if state == accept:
                accepted_config = (left, state, tape)
                print(f"\nAccepting Configuration Found: {accepted_config}")
                break
            if state == reject:
                print(f"Rejected Configuration: ({left}, {state}, {tape})")
                continue
            head = tape[0] if tape else '_'
            rest = tape[1:] if tape else ""
            transitions_state = transitions.get((state, head), [])
            for next_state, write, dir in transitions_state:
                if dir == "R":
                    new_left = left + write
                    new_tape = rest
                else:  # elif direction == "L"
                    new_left = left[:-1] if left else ""
                    new_tape = write + (tape if left else rest)
                new_config = (new_left, next_state, new_tape)
                if new_config not in parents:
                    parents[new_config] = (left, state, tape)
                    next_level.append(new_config)
        if accepted_config:
            break
        if next_level:
            #print(f"Next Level Configurations: {next_level}\n")
            tree.append(next_level)
        else:
            print("No More Configurations.\n")
        count += 1
    # Trace the accepting path
    accepting_path = trace(parents, accepted_config)
    print(f"Accepting Path: {accepting_path}\n")
    results(name, accepting_path, count, max_depth, bool(accepted_config))
def trace(parents, accepted_config):
    path = []
    curr_config = accepted_config
    while curr_config is not None:
        path.insert(0, curr_config)
        curr_config = parents.get(curr_config)
    return path
def results(name, accepting_path, steps, max_depth, accepted):
    #print(f"Machine Name: {name}")
    print(f"Total Transitions Simulated: {steps}")
    if accepted:
        print(f"String accepted in {steps} steps.")
        print("Accepting Path:")
        for config in accepting_path:
            print(config)
    else:
        print(f"String rejected in {steps} steps (or terminated at max depth {max_depth}).")
def csv_machine(file_path, test_cases, max_depth=10):
    machine = read_csv(file_path)
    print(f"\nTesting Machine: {machine['name']} from file: {file_path}\n")
    for input, expected_result in test_cases:
        print(f"\nTesting Input: '{input}' (Expected: {expected_result})")
        ntm(machine, input, max_depth=max_depth)
# testing
file_path = 'a_plus.csv'
test_cases = [("a", "Accept"), ("aaa", "Accept"), ("", "Reject"), ("aaaaa", "Accept")]
csv_machine(file_path, test_cases)


