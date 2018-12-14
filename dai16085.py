# Ioannis Panagiotis Pitsiorlas dai16085
# 1st Exercise Automata Theory


transitions = []
final_states = []
transition_str = ""
alphabet = []

# diavasma tou arxeiou
filename = raw_input("Give the name of the file with the file extension 'txt': " )


file = open(filename, 'r').readlines()

number_of_states = int(file[0])
initial_state = int(file[1])
num_of_final_states = int(file[2])
final_states_str = file[3]
num_of_transitions = int(file[4])

# Prosthetw tis metavivaseis se enan pinaka
for i in range(0, num_of_transitions):
    transitions.insert(i, file[i+5])

fsindex = 0

# Xwrizw tis telikes katastaseis me elegxo gia to an einai psifia kai tis vazw se mia kainouria metavlith final states
for i in final_states_str.split():
    if i.isdigit():
        final_states.insert(fsindex, i)
        fsindex += 1

# Pairnw kathe gramma apo tis metavivaseis kai ta vazw se mia string metavliti
for i in range(0, len(transitions)):
    transition_char = transitions[i]
    transition_str += transition_char[1]

# Elegxw to string wste na mhn mpoun diplotipa grammata mesa sto alphavito mou
for i in range(0, len(transition_str)):
    if transition_str[i] not in alphabet:
        alphabet += transition_str[i]

r = number_of_states
c = len(alphabet)

# Dimiourgw enan pinaka me tis katastaseis kai thn alphavita
Matrix = [[0 for x in range(c)] for y in range(r)]

# Allazw se ASCII ta grammata tis alphavitou kai ta prosthetw ston pinaka pou dimiourgisa
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

# Elegxw an sthn leksh pou dothike oi xaraktires ths vriskontai sto alphavito mou, krataw thn katastash pou vriskete to
# automato kai allazw kathe xaraktira se ASCII
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
# Elegxw an h katastash sthn opoia vrisketai to automato einai telikh kai analogws dexomai thn leksh
    if current_state in finalstatesint and flag == 0:
        print "accepted"
    else:
        print "not accepted"

# Elegxw an o xristis thelei na sinexisei to programma
    answer = raw_input("Do you want to continue? Yes: 1, No: 2 ")
    if int(answer) == 2:
        break



