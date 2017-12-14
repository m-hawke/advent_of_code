test_data = ['5 1 9 5', '7 5 3', '2 4 6 8',]

def checksum(sequence):
    checksum = 0
    for line in sequence:
        row = [int(s) for s in line.strip().split()]
        checksum += (max(row) - min(row))
    return checksum

assert checksum(test_data) == 18

with open('advent_2.data') as f:
    print(checksum(f))
