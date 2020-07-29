def merge(l1, l2):
    arr = l1+l2
    arr.sort()
    return arr

def q3(liste):
    if(len(liste)==1):
        return liste.pop()
    half = len(liste)//2
    return merge(q3(liste[:half]),q3(liste[half:]))

input =  [[1, 10, 11, 15],

        [2,  4,  9, 14],

        [5,  6,  8, 16],

        [3,  7, 12, 13]]

print(q3(input))
