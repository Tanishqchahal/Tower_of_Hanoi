NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

# starting configuration
print(A, "\n")

def move(n, source, auxiliary, target):
    if n <= 0:
        return