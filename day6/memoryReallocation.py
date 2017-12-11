def mem_reloc_part1(memBlox):
    iterations = [] # master list to keep all iterations
    steps = 0
    og_memBlox = memBlox.copy()

    while True:
        iterations.append(memBlox.copy())
        steps += 1
        print("Step", steps, "Iterations", iterations)
        pivot = max(memBlox)
        pivot_index = memBlox.index(pivot)
        ln = len(memBlox) - 1
        redist = pivot//ln
        keep_dist = pivot%ln

        for i in range(ln+1):
            if i == pivot_index:
                memBlox[i] = keep_dist
            else:
                memBlox[i] += redist
        
        print("New array", memBlox)
        print("********")        
        if memBlox in iterations:
            return steps
        else:
            pass


def main():
    memBlox = [int(x) for x in input().split()]
    print(mem_reloc_part1(memBlox))


if __name__ == "__main__":
    main()
