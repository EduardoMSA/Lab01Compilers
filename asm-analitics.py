log = open('log','r')
lines = log.readlines()

instructions = {}
functions = {}

for line in lines:
    if line[0].isnumeric():
        direction = line[:16]
        function = line[17:].replace(":\n","")
        functions[function[1:-1]] = direction
    if line[:4] == "    ":
        if len(line[32:].split()) == 0: 
            continue
        instruction = line[32:].split()[0]
        if instruction not in instructions.keys():
            instructions[instruction] = 1
        else:
            instructions[instruction] += 1

print('Hi, this is the output of the analysis:')
print('\tYou have %d kind of instructions in this object file:' % len(instructions))
for instruction in instructions:
    print('\t\t{0:<10s} : Executed {1:3d} times'.format(instruction, instructions[instruction]))
print('\tYou have %d functions' % len(functions))
for function in functions:
    print('\t\t{0:<21s} : Located at {1:<16s} addr'.format(function, functions[function]))