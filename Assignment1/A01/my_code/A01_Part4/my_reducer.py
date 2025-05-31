#!/usr/bin/python
# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------


# ------------------------------------------
# IMPORTS
# ------------------------------------------
import sys
import codecs

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # Initial Thought:
    # - The goal is to count trips starting from and ending at each station.
    # - The mapper has already emitted station names with 'start' or 'end' tags.
    # - Need to aggregate these counts and format the output as requested.
    # - Use a dictionary to store counts, then sort and write the results to the output file.
    
    station_counts = {}
    
    # Process each line from the mapper output
    for line in my_input_stream:
        line = line.strip()
        if not line:
            continue
            
        # Parse input line
        try:
            # Split by tab
            parts = line.split('\t')
            if len(parts) != 2:
                continue
                
            station = parts[0]
            # Parse the counts from (X, Y) format
            value = parts[1].strip('()')
            starts, ends = map(int, value.replace(' ', '').split(','))
            
            # Initialize or update station counts
            if station not in station_counts:
                station_counts[station] = [0, 0]
            
            station_counts[station][0] += starts
            station_counts[station][1] += ends
        except:
            continue
    
    # Output in alphabetical order
    for station in sorted(station_counts.keys()):
        start_count, end_count = station_counts[station]
        my_output_stream.write(f"{station}\t({start_count}, {end_count})\n")

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We collect the input values
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    my_reducer_input_parameters = []

    # 5. We call to my_reduce
    my_reduce(my_input_stream,
              my_output_stream,
              my_reducer_input_parameters
             )
