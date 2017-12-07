def pass_checker_part1(ip):
    correct_count = 0

    for line in ip.readlines():
        lst = line.split() # making list of each line by spliting word by word

        if len(lst) == len(set(lst)): # checking if len of list == set of list by eliminating the repeated modules
            correct_count += 1
        else:
            pass

    return correct_count

def pass_checker_part2(ip):
    correct_count = 0

    for line in ip.readlines():
        lst = line.split()
        temp_line = [] # to store a temporary list of sorted words in each line
        for word in lst:
            temp_line.append("".join(sorted(word))) # to sort a string/word and join it back

        if len(lst) == len(set(temp_line)):
            correct_count += 1
        else:
            pass

    return correct_count

def main():
    with open('input.txt', 'r+') as ip:
        print("Answer of part1 is:", pass_checker_part1(ip))
        ip.seek(0) # seeking back the file to it's initial position for part 2
        print("Answer of part2 is:", pass_checker_part2(ip))
        
if __name__ == "__main__":
    main()
