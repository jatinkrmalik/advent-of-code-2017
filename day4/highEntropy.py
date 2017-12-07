def pass_checker_part1(ip):
    correct_count = 0
    for line in ip.readlines():
        lst = line.split()

        if len(lst) == len(set(lst)):
            correct_count += 1
        else:
            pass

    return correct_count


def main():
    with open('input.txt', 'r+') as f:
        print(pass_checker_part1(f))

if __name__ == "__main__":
    main()
