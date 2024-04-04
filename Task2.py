"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
call_duration = {}
for call in calls:
    caller = call[0]
    receiver = call[1]
    duration = int(call[3])

    call_duration[caller] = call_duration.get(caller, 0) + duration
    call_duration[receiver] = call_duration.get(receiver, 0) + duration

longest_duration = max(call_duration.values())
telephone_number = max(call_duration, key=call_duration.get)

print(f"{telephone_number} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")
