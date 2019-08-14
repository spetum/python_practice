from collections import Counter

a = [0,1,1,1,2,3,7,7,23]

def count_element(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i,0) + 1
    return hist

counted = count_element(a)
print(counted)

recounted = Counter(a)
print(recounted)

print(recounted.items() == counted.items())

