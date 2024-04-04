"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Combine all telephone numbers from texts and calls
telephone_numbers = set()
for text in texts:
    telephone_numbers.add(text[0])
    telephone_numbers.add(text[1])
for call in calls:
    telephone_numbers.add(call[0])
    telephone_numbers.add(call[1])

# Count the number of different telephone numbers
count = len(telephone_numbers)

# Print the result
print(f"There are {count} different telephone numbers in the records.")
