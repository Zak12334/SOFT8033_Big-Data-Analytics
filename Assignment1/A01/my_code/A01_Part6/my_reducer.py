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
    # - The goal is to identify when the bike was moved by truck (not by users).
    # - Reducer's job: Sort all trips chronologically, then find gaps where:
    #   1. The bike ended trip at Station A
    #   2. The next trip starts at Station B (different from A)
    #   3. There's no user trip record showing how it got from A to B
    # - These gaps indicate truck movements for rebalancing the bike fleet.
    # - Format output exactly as shown in the reference solution.
    
    # Parse and collect all trips
    trips = []
    
    for line in my_input_stream:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            continue
            
        # Get the content inside parentheses
        content = parts[1]
        if not content.startswith('(') or not content.endswith(')'):
            continue
            
        # Remove parentheses and split by comma
        content = content[1:-1]
        segments = [s.strip() for s in content.split(',')]
        
        # Each line has 4 elements: start_time, stop_time, start_station_name, stop_station_name
        if len(segments) == 4:
            trips.append(segments)
    
    # Sort trips chronologically by stop_time
    trips.sort(key=lambda x: x[1])
    
    # Find truck movements
    for i in range(len(trips) - 1):
        current_trip = trips[i]
        next_trip = trips[i+1]
        
        # If the bike ended at one station and started at another
        if current_trip[3] != next_trip[2]:
            # Write in exact format with proper spacing after "By_Truck"
            my_output_stream.write(f"By_Truck\t({current_trip[1]}, {current_trip[3]}, {next_trip[0]}, {next_trip[2]})\n")
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
