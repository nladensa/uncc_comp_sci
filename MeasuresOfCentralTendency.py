"""
@author: Nicole_Ladensack
"""

import collections.Counter as counter


#finds the mean of a dataset
def mean(dataset):
    return sum(dataset) / len(dataset)

#finds the median of a dataset
def median(dataset):
    n = len(dataset)
    sorted_data = sorted(dataset)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_data[midpoint]
    else:
        l = midpoint - 1
        h = midpoint
        return (sorted_data[l] + sorted_data[h]) / 2

#finds the mode of a dataset
def mode(dataset):
    counts = counter(dataset)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]

def main():
    data = [25, 77, 12, 45, 70, 92, 84, 14, 28, 64, 78, 44, 79, 55, 2, 63, 15, 24, 29, 97, 72, 35, 20, 74, 9, 62, 85, 30, 75, 59, 95, 52, 54, 89, 43]
    print("Mean is " + str(mean(data)))
    print("Median is " + str(median(data)))
    print("Mode is " + str(mode(data)))
    
if __name__ == '__main__':
    main()
