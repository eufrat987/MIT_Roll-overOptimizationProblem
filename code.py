F = 3
ps =        [1, 2, 3, 5, 11]
choice =    [10, 10, 10, 10, 10] # 0 or 10

def score(choice):
    return (60 - sum(choice))*F + sum([val * ps[i] for i, val in enumerate(choice)])

def maxVal(choice, i):
    if i == len(choice):
        return score(choice), sum(choice)
    
    ret = 0
    ravail = 0
    choice[i] = 0
    ret1, avail1 = maxVal(choice, i+1)
    choice[i] = 10
    ret2, avail2 = maxVal(choice, i+1)
    
    if avail1 >= 20:
        choice[i] = 10
        ret = ret1
        ravail = avail1
    if avail2 >= 20 and ret2 > ret:
        ret = ret2
        ravail = avail2
    
    return ret, ravail

def brute():
    scorer = None
    
    num_bits = (31).bit_length()  # Only loop over significant bits
    for n in range(0,31):
        choice = []

        for i in range(num_bits):
            bit = (n >> i) & 1
            choice += [bit*10]

        if sum(choice) >= 20 and (scorer is None or scorer < score(choice)):
            scorer = score(choice)
    return scorer

print(brute())
print(maxVal(choice, 0))

