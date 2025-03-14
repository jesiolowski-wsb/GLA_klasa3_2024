perfect_list = ["g", "fwa", "d", "dwafesfe", 325352353232, "ddddaaaaa"]

print(str())

try:
    longest_list = [str(perfect_list[0])]
    shortest_list = [str(perfect_list[0])]

    for i in perfect_list[1:]:
        if len(str(i)) > len(longest_list[0]):
            longest_list.clear()
            longest_list.append(str(i))

        elif len(str(i)) == len(longest_list[0]):
            longest_list.append(str(i))

        if len(str(i)) < len(shortest_list[0]):
            shortest_list.clear()
            shortest_list.append(str(i))

        elif len(str(i)) == len(shortest_list[0]):
            shortest_list.append(str(i))

    if len(longest_list) == 1:
        longest = sorted(longest_list)[0]
    else:
        longest = sorted(longest_list)[-1]
    shortest = sorted(shortest_list)[0]

except IndexError:
    longest = "None"
    shortest = "None"

print("Longest:", longest)
print("Shortest:", shortest)
