# Read and Translate functions

# Create a function that will read game files
# Create a function that will take output from
# read function and translate it into workable* output
# for the writing function in other file

def I_READ(a_filename):
    filename = open(a_filename, "r")
    longest_string_in_python = filename.read()
    return longest_string_in_python

def I_WRITE(a_filename):
    filename = open("a_filename.txt", "w+")
    longest_string_in_python = filename.write()
    