"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import operator

# Initialisation
a = [1,2,3,3,4,4,5,5,5,"a","a","a","a"]     # input array
k = 2                                       # display k most frequent elements
d = {}                                      # empty dictionnary

# Count the occurence of each unique value in the array: complexity = O(n)
for e in a:
    if e not in d.keys():
        d[e]=1
    else:
        d[e]+=1
print("List of all items with occurrecies: ", d)        

# Sort elements by their occurence: complexity <= O(n log n)
dsort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print("Sorted list by the occurence: ", dsort)

# Display first k elements: compexity <= O(n)
s=[]
for i in range(k):
    s.append(dsort[i][0])
print("First",k,"most frequent elements: ", s)

# Overall complexity is at most O(n log n), depending on the number of unique values (due to sorting). 
# More repetitions => less unique values => easier sorting => lower complexity.

# One-line solution:
print("One-line solution: ", sorted([e for e in set(a)], key=a.count, reverse=True)[0:k])
