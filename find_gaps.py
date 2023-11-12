test1 = [(10, 12), (13, 14)]
test1_out = [(12, 13)]

test2 = [(9, 11), (10, 10.5), (11, 13), (19, 20)]
test2_out = [(13, 19)]

test3 = [(9, 10), (10.5, 12), (11, 15), (17, 18)]
test3_out = [(10, 10.5), (15, 17)]

def find_gaps(schedule):
    gaps = []
    for index, pair in enumerate(schedule):
        if index == len(schedule) - 1:
            break
        next_pair = schedule[index + 1]
        if pair[1] < next_pair[0]:
            gaps.append((pair[1], next_pair[0]))
    return gaps

print(find_gaps(test1) == test1_out)
print(find_gaps(test2), test2_out)
print(find_gaps(test3) == test3_out)