cd#Find the numbers of pairs of socks of the same color given a pile of socks

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 70, 80, 20, 40, 70, 20, 30, 60, 50, 10, 10, 70, 70]

def sockMerchant(ar):
    zero_values = [0] * len(set(ar))
    zip_iter = zip(set(ar), zero_values)
    pairs = dict(zip_iter)

    for sock in ar:
        pairs[sock] += 1
    
    pairs_sum = 0
    pair_lst = list(pairs.values())
    
    for color in pair_lst:        
        pairs_sum += color // 2
    
    print(pairs_sum)
    return pairs_sum

sockMerchant(ar)

