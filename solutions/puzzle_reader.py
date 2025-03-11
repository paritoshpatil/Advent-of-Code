import os

def get_data():
    # open inputs/1.txt file
    cwd = os.getcwd()
    with open(cwd + '/inputs/1.txt', 'r') as file:
        data = file.readlines()
        # Process the data into two columns
        column1 = []
        column2 = []
        for line in data:
            values = line.strip().split()  # Split by whitespace
            if len(values) == 2:  # Ensure there are two values
                column1.append(int(values[0]))  # First column
                column2.append(int(values[1]))  # Second column
    return column1, column2