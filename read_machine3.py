# Example NTM Definitions
machines = {
    "a+": {
        "states": ["q1", "q2", "q3"],
        "start_state": "q1",
        "accept_state": "q3",
        "reject_state": "qrej",
        "transitions": {
            ("q1", "a"): [("q1", "a", "R"), ("q2", "a", "R")],
            ("q2", "_"): [("q3", "_", "L")]
        },
    },
    "aa+": {
        "states": ["q1", "q2", "q3"],
        "start_state": "q1",
        "accept_state": "q3",
        "reject_state": "qrej",
        "transitions": {
            ("q1", "a"): [("q2", "a", "R")],
            ("q1", "_"): [("qrej", "_", "R")],
            ("q2", "a"): [("q3", "a", "R")],
            ("q2", "_"): [("qrej", "_", "R")],
            ("q3", "a"): [("q3", "a", "R")],
            ("q3", "_"): [("q3", "_", "L")],
        },
    },
}


def simulate_ntm(machine, input_string, max_depth):
    """Simulate an NTM with the given configuration."""
    name = machine["name"]
    states = machine["states"]
    start_state = machine["start_state"]
    accept_state = machine["accept_state"]
    reject_state = machine["reject_state"]
    transitions = machine["transitions"]

    tree = []  # Configuration tree: a list of lists of triples
    parents = {}  # Track parent-child relationships for path reconstruction
    initial_config = ("", start_state, input_string)
    tree.append([initial_config])
    parents[initial_config] = None  # Root has no parent

    step_count = 0
    accepted_config = None

    print("\n--- Simulation Start ---")
    print(f"Machine Name: {name}")
    print(f"Initial Configuration: {initial_config}\n")

    while tree and step_count < max_depth:
        current_level = tree[-1]
        next_level = []

        print(f"Depth {step_count}: Current Level Configurations: {current_level}")

        for left, state, tape in current_level:
            # Check for accept/reject states
            if state == accept_state:
                accepted_config = (left, state, tape)
                print(f"\nAccepting Configuration Found: {accepted_config}")
                break
            if state == reject_state:
                print(f"Rejected Configuration: ({left}, {state}, {tape})")
                continue

            # Simulate transitions
            head = tape[0] if tape else '_'
            rest = tape[1:] if tape else ""
            transitions_from_state = transitions.get((state, head), [])

            for next_state, write_char, direction in transitions_from_state:
                if direction == "R":
                    new_left = left + write_char
                    new_tape = rest
                else:  # direction == "L"
                    new_left = left[:-1] if left else ""
                    new_tape = write_char + (tape if left else rest)
                new_config = (new_left, next_state, new_tape)

                if new_config not in parents:
                    parents[new_config] = (left, state, tape)
                    next_level.append(new_config)

        if accepted_config:
            break

        if next_level:
            print(f"Next Level Configurations: {next_level}\n")
            tree.append(next_level)
        else:
            print("No More Configurations to Explore.\n")
        step_count += 1

    # Trace the accepting path
    print("\n--- Tracing Accepting Path ---")
    accepting_path = trace_accepting_path(parents, accepted_config)
    print(f"Accepting Path: {accepting_path}\n")
    output_results(name, accepting_path, step_count, max_depth, bool(accepted_config))


def trace_accepting_path(parents, accepted_config):
    """Reconstruct the path from the initial configuration to the accepting state."""
    path = []
    current_config = accepted_config

    while current_config is not None:
        path.insert(0, current_config)
        current_config = parents.get(current_config)

    return path


def output_results(name, accepting_path, steps, max_depth, is_accepted):
    """Output the results of the NTM simulation."""
    print(f"Machine Name: {name}")
    print(f"Total Transitions Simulated: {steps}")

    if is_accepted:
        print(f"String accepted in {steps} steps.")
        print("Accepting Path:")
        for config in accepting_path:
            print(config)
    else:
        print(f"String rejected in {steps} steps (or terminated at max depth {max_depth}).")


def test_all_machines():
    """Run test cases for all machines."""
    test_cases = {
        "a+": [
            ("a", "Accept"),
            ("aaa", "Accept"),
            ("aaaaa", "Accept"),
            ("", "Reject"),
            ("b", "Reject"),
        ],
        "aa+": [
            ("aa", "Accept"),
            ("aaa", "Accept"),
            ("aaaa", "Accept"),
            ("a", "Reject"),
            ("", "Reject"),
            ("b", "Reject"),
        ],
    }

    for machine_name, cases in test_cases.items():
        print(f"\nTesting Machine: {machine_name}")
        machine = {"name": machine_name, **machines[machine_name]}
        for input_string, expectation in cases:
            print(f"\nTesting Input: '{input_string}' (Expected: {expectation})")
            simulate_ntm(machine, input_string, max_depth=10)


# Run tests
test_all_machines()
