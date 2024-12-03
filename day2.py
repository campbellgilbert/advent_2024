import numpy as np

#read in the file
"""format:
62 65 67 70 73 76 75
68 71 73 76 78 78
77 80 81 82 86
44 47 48 51 53 58
51 53 56 57 59 56 57 60
68 70 71 69 72 74 71
59 61 63 66 64 66 66
... etc
"""

#create some kind of data structure then read in the lines 
#and append them to the data structure
file = 'day2_input.txt'
with open(file) as f:
    lines = f.readlines()
    data = []
    for line in lines:
        data.append([int(x) for x in line.split()])

"""
PT 1
a = [3, 8, 12, 18, 25]

#Define the range
start, end = 10, 20

# Check if any element in the list is in the range
in_range = any(start <= num <= end for num in a)


7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.
"""

"""
knee jerk instinct is to sort and then check increasing/decreasing, but could be better to check differences between each item in list
or -- python *probably* has a way to check the biggest difference in a list
#or, duh, use np diff
"""

safe_reports = 0
for level in data:
    levarr = np.array(level)
    diff = np.diff(levarr)

    #check for either all positives or all negatives
    if (all(i <= 0 for i in diff) or all(i >= 0 for i in diff)):
        if all(1 <= abs(i) <= 3 for i in diff):
            safe_reports = safe_reports + 1
print(safe_reports)

#is there a way to do this as a oneline?
#this would probably involve not iterating, or at least not iterating as much.

"""
PT 2
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:
    7 6 4 2 1: Safe without removing any level.
    -> [-1 -2 -2 -1]

    1 2 7 8 9: Unsafe regardless of which level is removed.
    -> [1 5 1 1]
        
    9 7 6 2 1: Unsafe regardless of which level is removed.
    -> [-2 -1 -4 -1]

    1 3 2 4 5: Safe by removing the second level, 3.
    -> [ 2 -1  2  1]
    meets one fail condition (positivity) but not the second

    for i in range(len(level) - 1):
        if abs(level[i]) - abs(level[i + 1]) 

    8 6 4 4 1: Safe by removing the third level, 4.
    -> [-2 -2  0 -3]
    meets one fail condition (bounds) but not the first

    1 3 6 7 9: Safe without removing any level.
    -> [2 3 1 2]

we can't just take every unsafe level and iterate thru all the possible diffs to see if they meet the right condition
time complexity would be catastrophic

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
def check_level(levarr):
    #levarr = np.array(level)
    diff = np.diff(levarr)
    #check for either all positives or all negatives
    if not (all(i <= 0 for i in diff) or all(i >= 0 for i in diff)):
        print("not strictly asc/desc")
        return 0
    
    if any(abs(i) < 1 for i in diff) or any(abs(i) > 3 for i in diff):
        print("out of bounds")
        return 0
    return 1

def check_if_safety_possible(level):
    print("checking if level can be made safe...")
    level = np.array(level)
    for i in range(len(level)):
        current_test_level = np.delete(level, i)
        print(current_test_level)
        if check_level(current_test_level) == 1:
            return 1
    return 0

def check_if_safety_possible_recursive(level, i):
    print("checking if safety is possible RECURSIVELY")
    #base case
    #we've gotten to the end of the array and it's still unsafe
    if i == len(level):
        return 0

    #recursive call
    current_test_level = np.delete(level, i)
    print(current_test_level)
    check = check_level(current_test_level)
    #if passes test
    if check == 1:
        return 1
    if check == 0:
        return check_if_safety_possible_recursive(level, i + 1)

safe_reports = 0

for i in data:
    print("hello world")
    i = np.array(i)

    safety = check_level(i)
    safe_reports += safety
    if safety == 1:
        continue
    
    #depressingly enough i don't see a way out but to brute force it
    #8 6 4 4 1 saved by removing the first 4
    #1 3 2 4 5 saved by removing the 3\
    safe_reports += check_if_safety_possible_recursive(i, 0)
    
#correct answer is 436

print(safe_reports)

"""safe_reports = 0
for level in data:
    levarr = np.array(level)
    diff = np.diff(levarr)

    #check for either all positives or all negatives
    if (all(i <= 0 for i in diff) or all(i >= 0 for i in diff)):
        if all(1 <= abs(i) <= 3 for i in diff):
            safe_reports = safe_reports + 1
print(safe_reports)"""