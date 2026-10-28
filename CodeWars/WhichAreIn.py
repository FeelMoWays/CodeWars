def in_array(array1, array2):
    substring_list = []
    for i in array2:
        for j in array1:
            if j in i and j not in substring_list:
                substring_list.append(j)
    sorted_substring = sorted(substring_list)
    return sorted_substring

print(in_array(["arp", "live", "strong"],["arp", "live", "strong"]))
