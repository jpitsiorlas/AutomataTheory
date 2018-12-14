# Ioannis Panagiotis Pitsiorlas 
# Crestion of an Automate


transitions = []
final_states = []
transition_str = ""
alphabet = []

# reading the file
filename = raw_input("Give the name of the file with the file extension 'txt': " )


file = open(filename, 'r').readlines()

number_of_states = int(file[0])
initial_state = int(file[1])
num_of_final_states = int(file[2])
final_states_str = file[3]
num_of_transitions = int(file[4])

# Adding the transitions in the array
for i in range(0, num_of_transitions):
    transitions.insert(i, file[i+5])

fsindex = 0

# Seperating and adding the final states in a new variable
for i in final_states_str.split():
    if i.isdigit():
        final_states.insert(fsindex, i)
        fsindex += 1

# Adding each character in a string variable
for i in range(0, len(transitions)):
    transition_char = transitions[i]
    transition_str += transition_char[1]

# Searching if there are any duplicates
for i in range(0, len(transition_str)):
    if transition_str[i] not in alphabet:
        alphabet += transition_str[i]

r = number_of_states
c = len(alphabet)

Matrix = [[0 for x in range(c)] for y in range(r)]

#Changing each character in ASCII code
for i in range(0, num_of_transitions):
    temp = transitions[i]
    char1 = temp[0]
    char2 = temp[1]
    char3 = temp[2]
    x = int(char1) - 1
    y = ord(char2) - 97
    z = int(char3)
    Matrix[x][y] = z


while True:
    inputstr = raw_input("Give word: ")

    current_state = 1
    flag = 0


#Evaluate if the characters in the given word are in my Alphabet, keeping the current state
    for i in range(0, len(inputstr)):
        character = inputstr[i]
        if character not in alphabet:
            flag = 1
            current_state = 1
            break
        y = ord(character) - 97
        x = current_state - 1
        current_state = Matrix[x][y]



    finalstatesint = map(int, final_states)

    if current_state in finalstatesint and flag == 0:
        print "accepted"
    else:
        print "not accepted"

    answer = raw_input("Do you want to continue? Yes: 1, No: 2 ")
    if int(answer) == 2:
        break



