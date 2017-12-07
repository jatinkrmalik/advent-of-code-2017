def convertToList(ip):
    '''
    Function to read the file, split on each new line, convert to list and ignore the last blank and then convert each element to int
    '''
    return list(map(int, ip.read().split('\n')[:-1])) 

def mazeRunner_part1(steps):
    '''
    Function to play the game - Part 1
    '''
    curr_position = 0
    step_count = 0
    while curr_position < len(steps):
        step_count += 1

        if steps[curr_position] == 0:
            steps[curr_position] += 1
            
        else:
            move_by = steps[curr_position]
            steps[curr_position] += 1
            curr_position = curr_position + move_by
    
    return step_count

def mazeRunner_part2(steps):
    '''
    Function to play the game - Part 2
    '''
    curr_position = 0
    step_count = 0
    while curr_position < len(steps):
        step_count += 1

        if steps[curr_position] == 0:
            steps[curr_position] += 1
        
        elif steps[curr_position] >= 3:
            move_by = steps[curr_position]
            steps[curr_position] -= 1
            curr_position = curr_position + move_by

        else:
            move_by = steps[curr_position]
            steps[curr_position] += 1
            curr_position = curr_position + move_by
        
    return step_count

def main():
    with open('input.txt', 'r+') as ip:
        steps = convertToList(ip)
        steps2 = steps.copy() # so that we can pass the fresh input into part2
        print(mazeRunner_part1(steps))
        print(mazeRunner_part2(steps2))


if __name__ == "__main__":
    main()
