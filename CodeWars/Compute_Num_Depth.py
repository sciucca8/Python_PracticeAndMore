def compute_depth(n):
    multiplier = 1
    nums = set()

    while True:
        num = str(n * multiplier)
        nums.update(set((num)))
        nums = set(map(int, nums))

        if nums == set(range(10)):
            return multiplier

        multiplier += 1

print(compute_depth(256235))


#Optimized
def compute_depth(n):
    multiplier = 0
    nums = set()

    while len(nums) < 10:
        multiplier += 1
        num = str(n * multiplier)
        nums.update(set((num)))
        nums = set(map(int, nums))
        
    return multiplier 

print(compute_depth(256235))

