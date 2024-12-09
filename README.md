# traceTM_Ojeda
# Project x Readme Team Ojeda

### Team Name: 
Ojeda

### Team members names and netids: 
Isabel Ojeda (iojeda)

### Overall project attempted, with sub-projects: 
Tracing NTM Behavior 

### Overall success of the project: 
Successful 

### Approximately total time (in hours) to complete: 
3-4 hours in general per day for 5 days. 

### Link to github repository: 
https://github.com/iojeda1/traceTM_Ojeda.git 


### List of included files

Code files: read_machine_Ojeda.py
This code simulates the behavior of a NTM defined in a CSV file. The code reads this configuration, runs the NTM for a given set of test cases, and determines if each input string is accepted, rejected, or terminates due to reaching a predefined depth. 

Test File: The test cases are included in the code file as a function for the a+ machine included in the a_plus_Ojeda.csv file 
The a_plus_Ojeda.csv file contains the configuration of an a+ NTM machine designed to process strings. It includes the machine name, the states, the input symbols, the tape symbols, the accept state, and the reject state. 

test_cases = [("a", "Accept"), ("aaa", "Accept"), ("", "Reject"), ("aaaaa", "Accept")]


Output Files: output_Ojeda.txt
The output details the NTM simulation for each input, including the machine's configurations at each depth, the path to acceptance (if found), and metrics such as the total transitions simulated and the maximum depth explored. For accepted inputs, it displays the sequence of configurations leading to the accept state. For rejected inputs, it shows the machine's inability to progress further, terminating after reaching the maximum depth.

Analysis
Input String	Result	Depth	# Configurations Explored	Average Non-Determinism
a	           Accepted	 2	              4	                            2
aaa	           Accepted	 4	              8	                            2
" "            Rejected	 10	              12	                       1.2
aaaaa	       Accepted	 6	              14	                   2.333333333
The table summarizes the results of the NTM simulations for various input strings using the machine defined in the a+ machine. Each row represents a test case, detailing the input string tested, the result , the depth of the configuration tree explored, the total number of configurations visited, and the average nondeterminism (number of configurations explored/depth). 


### Programming languages used, and associated libraries: 
Python (libraries = csv)

### Key data structures (for each sub-project): 
Lists, dictionary, and tuples. 

### General operation of code (for each subproject)
The code operates in distinct phases to simulate and analyze the behavior of a NTM. It starts by reading the machine's configuration from a CSV file using the, extracting key components like states, input symbols, and transitions into a structured dictionary. The ntm function then simulates the machine for a given input string, employing a BFS approach to explore configurations up to a specified depth, while tracking the path to acceptance or rejection. If the input string is accepted, the code reconstructs the path of configurations leading to the accepting state; if rejected, the simulation outputs the maximum depth reached or the lack of valid configurations. The results function summarizes the simulation by detailing the total transitions, depth of the configuration tree, and whether the input was accepted or rejected.

### What test cases you used/added, why you used them, what did they tell you about the correctness of your code.
The test cases used included a, aaa, aaaaa, and “ “, designed to evaluate the correctness and robustness of the NTM simulation. Valid inputs tested whether the machine could process strings of varying lengths composed entirely of “a” characters, ensuring that transitions and acceptance logic were correctly implemented. The empty string was included to verify that the machine correctly rejects invalid inputs by halting when no valid transitions exist. These test cases demonstrated that the machine handles both deterministic and nondeterministic paths, processes multiple transitions effectively, and terminates appropriately, confirming the correctness of its state transitions, configuration exploration, and path tracing mechanisms.

### How you managed the code development: 
The code development was managed in an iterative manner, starting with the implementation of core functionalities like reading the NTM configuration from a CSV file and simulating the machine's transitions. Each component, such as configuration parsing, state transitions, and acceptance path tracing, was developed and tested independently to ensure correctness and clarity. Test cases were added incrementally to evaluate edge cases, valid paths, and rejection scenarios, which helped refine the code further. Additionally, reusable functions were created for tracing paths and summarizing results, ensuring the code remained clear for batch testing multiple inputs. 

### Detailed discussion of results:
The results showed that the NTM correctly handled valid and invalid inputs, demonstrating the robustness of the simulation. For valid inputs like the machine successfully reached the accept state, with the accepting path traced accurately. The simulation processed each input efficiently, exploring configurations level by level and stopping upon acceptance. For the invalid input, the machine correctly terminated without valid transitions, rejecting the input and halting after reaching the maximum depth. These results validated the correctness of the state transitions, nondeterministic branching, and acceptance logic.

### How team was organized: 
This is a one person team, so I worked on the code little by little each day. 

### What you might do differently if you did the project again: 
I would have taken more time to read all of the instructions and understand what the problem we were trying to solve was. Sometimes, I rush too much to get started to code, however, it is utterly important to understand what the algorithm is set to do. This caused me many setbacks as I had to restart a couple times. 

Any additional material: N/A


