__author__ = 'Stan'

def distance(string_one, string_two):
    len_one = len(string_one)
    len_two = len(string_two)
    results_table = [[0 for x in range(len_two + 1)] for x in range(len_one + 1)]

    for i in range(len_one + 1):
        for j in range(len_two + 1):
            if i == 0:
                results_table[i][j] = j
            elif j == 0:
                results_table[i][j] = i
            elif string_one[i-1] == string_two[j-1]:
                results_table[i][j] = results_table[i-1][j-1]
            else:
                results_table[i][j] = 1 + min(results_table[i-1][j],
                                              results_table[i-1][j-1],
                                              results_table[i][j-1])
    return results_table[len_one][len_two]

print(distance("stan", "rox"))