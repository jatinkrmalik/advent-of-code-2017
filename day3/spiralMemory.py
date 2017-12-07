import sys
import math

def get_square(ip):
    '''
    To calculate the size of square required
    '''
    square = 1
    
    while square * square < ip:
        square = square + 2
    
    return square

def distance_to_one(num, base, offset, side):
    '''
    To find the number of step after each step recursively
    '''
    
    first = base + 1
    
    if num < first + side:
        return int(math.fabs(num - first - offset))
    
    elif num < first + side * 2:
        return int(math.fabs(num - first - offset - side))
    
    elif num < first + side * 3:
        return int(math.fabs(num - first - offset - side * 2))
    
    else:
        return int(math.fabs(num - first - offset - side * 3))


def get_eight_neighbours(pos):
    return [(x,y) for x in range(pos[0] - 1, pos[0] + 2) for y in range(pos[1] - 1, pos[1] + 2) if [x, y] != pos]


def distance_to_one_part2(n):
    pos = [0, 0]
    turns = 0
    seen = {(0, 0): 1}

    while True:
        length = (turns // 2) + 1
        for _ in range(length):
            direction = turns % 4
            if direction == 0:
                pos[0] += 1
            elif direction == 1:
                pos[1] += 1
            elif direction == 2:
                pos[0] -= 1
            else:
                pos[1] -= 1
            
            score = 0
            neighbours = get_eight_neighbours(pos)
            for neighbour in neighbours:
                if neighbour in seen:
                    score += seen[neighbour]

            if score > n:
                return score

            seen[tuple(pos)] = score
        
        turns += 1

def main():
    ip = int(input()) # getting input from STDIN
    square = get_square(ip)
    side_len = square - 1
    path_to_one = math.floor(square/2)
    side_offset_to_middle = path_to_one - 1
    prev_square = square - 2
    print(path_to_one + distance_to_one(ip, prev_square * prev_square, side_offset_to_middle, side_len))

    # print(distane_to_one_part2(ip))

if __name__ == "__main__":
    main()

