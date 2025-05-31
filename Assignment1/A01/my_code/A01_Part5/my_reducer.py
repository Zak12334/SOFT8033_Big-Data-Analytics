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
    # Initial Thoughts:
    # - The goal is to aggregate duration and trip counts per bike, then find the top N bikes.
    # - Reducer's job: Sum up all durations and count trips for each bike_id.
    # - Sort bikes by total duration (descending) and output the top N as specified.
    # - Ensure exact output format with proper spacing for the test checker.

    # Extract top_n_bikes from input parameters
    top_n_bikes = my_reducer_input_parameters[0]

    # Dictionary to store bike data: {bike_id: [total_duration, total_trips]}
    bike_data = {}

    # Parse input lines
    for line in my_input_stream:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) != 2:
            continue

        try:
            # Parse the tuple (bike_id, duration, count)
            value_str = parts[1].strip('()')
            values = value_str.split(',')

            if len(values) == 3:
                bike_id = int(values[0].strip())
                duration = int(values[1].strip())
                count = int(values[2].strip())

                # Aggregate data for each bike
                if bike_id in bike_data:
                    bike_data[bike_id][0] += duration
                    bike_data[bike_id][1] += count
                else:
                    bike_data[bike_id] = [duration, count]
        except Exception:
            continue

    # Sort bikes by total duration in descending order
    sorted_bikes = sorted(bike_data.items(), key=lambda x: x[1][0], reverse=True)

    # Strictly output only the specified number of bikes
    for bike_id, (total_duration, trip_count) in sorted_bikes[:top_n_bikes]:
        # Exact formatting is crucial
        my_output_stream.write(f"{bike_id}\t({total_duration}, {trip_count})\n")
# ---------------------------------------------------------------
#           PYTHON EXECUTION
# ---------------------------------------------------------------
if __name__ == '__main__':
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout
    top_n_bikes = int(sys.argv[1]) if len(sys.argv) > 1 else 10  # Default to 10 bikes
    my_reducer_input_parameters = [top_n_bikes]

    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)