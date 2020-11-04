import os
import sys

FILE_NAME = 'scores.txt'
READ_MODE = 'r'
OUTPUT_FILE = 'log.txt'
WRITE_MODE = 'w'

num_students = 0
total_score = 0
avg_score = 0

try:
    scores = open(FILE_NAME, 'r')
    output = open(OUTPUT_FILE, 'w')
    with scores, output:
        for line in scores:
            name, score = line.split()
            try:
                total_score += int(scores)
            except ValueError as error:
                output.write(f'Bad score value for {name}, ignored.\n')
            else:
                num_students += 1
        avg_score = (total_score / num_students)

        output.write(f'The class average is {avg_score: .2f} for {num_students} students.')
        print(f'The class average is {avg_score: .2f} for {num_students} students.')

except OSError as error:
    print(f'Unable to open file {FILE_NAME}. Error message: {error}')
except:
    error = sys.exc_info()[0]
    print(f'Unexpected error: {error}')

finally:
    print('Code block executed')