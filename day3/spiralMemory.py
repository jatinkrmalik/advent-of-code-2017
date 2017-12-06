
import math
import sys


def stats(val):
  if val <= 1: return (0, 0, 0)
  root = int(math.ceil(math.sqrt(val)))
  root += 1 if (root % 2 == 0) else 0
  max = root if root % 2 == 0 else root - 1
  return (root**2, max, max // 2)

def distanceToOne(stats, entry):
  diff = (stats[0] - entry) % stats[2]
  if diff > stats[2]:
    print(stats[2] + (diff - stats[2]))
  else:
    print(stats[1] - diff)

def main():
        ip = int(input())
        
        ip_stat = stats(ip)
        
        distanceToOne(ip_stat, ip)

if __name__ == "__main__":
    main()
