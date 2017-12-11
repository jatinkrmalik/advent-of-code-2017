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

        print("Pivot:", pivot, "at index:", pivot_index, "in arr of length of rest elements", ln, "Redist: ", redist, "and keep ", keep_dist)
        for i in range(ln+1):
            mod_index = i + pivot_index
            
            if mod_index == pivot_index:
                print("Updating at index", mod_index)
                memBlox[mod_index] = keep_dist

            elif mod_index > ln:
                print("Updating at index", mod_index%ln)
                memBlox[mod_index%ln] += redist

            else:
                print("Updating at index", mod_index)
                memBlox[mod_index] += redist
        
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
