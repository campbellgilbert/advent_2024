import numpy as np

#read in input txt
"""
18944   47230
94847   63037
93893   35622
37174   43365
77982   51397
"""
with open('day1_input.txt') as f:
    lines = f.readlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

#CHECK and make sure right and left look right


left_list = np.array(left_list)
right_list = np.array(right_list)
left = np.sort(left_list)
right = np.sort(right_list)
sum = np.abs(left - right).sum()
print(sum)

"""
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
"""

"""
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity score:

    The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
    The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
    The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
    The fourth number, 1, also does not appear in the right list.
    The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
    The last number, 3, appears in the right list three times; the similarity score again increases by 9.

31 (9 + 4 + 0 + 0 + 9 + 9).
"""
right_test = np.array([4, 3, 5, 3, 9, 3])
left_test = np.array([3, 4, 2, 1, 3, 3])

unique, counts = np.unique(right_test, return_counts=True)
print(dict(zip(unique.tolist(), counts.tolist())))

unique, counts = np.unique(left_test, return_counts=True)
print(dict(zip(unique.tolist(), counts.tolist())))

"""
left:
{1: 1, 
2: 1, 
3: 3, 
4: 1}

right:
{3: 3, 
4: 1, 
5: 1, 
9: 1}

1 does not appear in right list so that's *0
2 does not appear in right list so that's *0
3 appears in right list
    -> 3 appears 3 times in right list: 3 * 3 = 9
        -> 3 appears 3 times in left list: 9 * 3 = 27

4 appears in right list
    -> 4 appears 1 time in right list: 4 * 1 = 4
        -> 4 appears 1 time in left list: 4 * 1 = 4

9 appears in right list
    -> 9 appears 1 time in right list: 9 * 1 = 9
        -> 9 appears 0 times in left list: 9 * 0 = 0



for r_unique, r_count in right_dict
    if r_unique in left_dict:
        mult = r_unique * r_count * left_dict[r_unique] #this should get left count
        #e.g., 4 * 1 * 1
"""
r_u, r_c = np.unique(right, return_counts=True)
r_dict = dict(zip(r_u.tolist(), r_c.tolist()))

l_u, l_c = np.unique(left, return_counts=True)
l_dict = dict(zip(l_u.tolist(), l_c.tolist()))

final_sum = 0
for r_unique, r_count in r_dict.items():
    if r_unique in l_dict:
        final_sum = final_sum + (r_unique * r_count * l_dict[r_unique])

print(final_sum)

"""
similarity_score = 0
we know both lists are sorted already so presumably if number n in left list appears in right list it should be relatively close by

import numpy
a = numpy.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])
unique, counts = numpy.unique(a, return_counts=True)

>>> dict(zip(unique, counts))
{0: 7, 
1: 4, 
2: 1, 
3: 2, 
4: 1}



SUPER NAIVE SOLUTION
total_sum = 0
for i in left_list:
    mult = 0
    unique, counts = numpy.unique(right_list)
    

"""

