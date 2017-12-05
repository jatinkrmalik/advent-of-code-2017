ip = open('input.txt', 'r+')
#ip = input()
sheets = []

for line in ip.readlines():
    sheets.append(line.split())

new_sheet = []

for sheet in sheets:
    new_sheet.append(sorted(list(map(int, sheet))))

checksum = 0

for row in new_sheet:
    checksum += row[-1] - row[0]

print(checksum)
