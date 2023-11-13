test1 = [(10, 12), (13, 14)]
test1_out = [(10, 12), (13, 14)]

test2 = [(9, 11), (10, 10.5), (11, 13), (19, 20)]
test2_out = [(9, 13), (19, 20)]

test3 = [(9, 10), (10.5, 12), (11, 15), (12, 14), (17, 18)]
test3_out = [(9, 10), (10.5, 15), (17, 18)]

def merge_intervals(schedule):
    intervals = [schedule[0]]
    for current_start, current_end in schedule:
        previous_start, previous_end = intervals[-1]

        if previous_end >= current_start:
            intervals[-1] = (previous_start, max(current_end, previous_end))
        else:
            intervals.append((current_start, current_end))
    
    return intervals

print(merge_intervals(test1) == test1_out)
print(merge_intervals(test2) == test2_out)
print(merge_intervals(test3) == test3_out)
