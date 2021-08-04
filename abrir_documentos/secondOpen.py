import sys 

file_input = sys.argv[1]

file_object = open(file_input, 'r').readlines()

print(file_object)
