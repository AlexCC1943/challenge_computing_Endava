def binarySearch(lis, ele):
    if len(lis) <= 0:
        return "No se encontró el elemento"

    mitad = lis[len(lis)//2]
    if mitad == ele:
        return "Se encontró el elemento"
    else:
        if ele < mitad:
            return binarySearch(lis[:len(lis)//2], ele)
        else:
            return binarySearch(lis[(len(lis)//2)+1:], ele)


n = 47
lisN = [1, 2, 3, 4, 8, 12, 25, 34, 47, 89, 92, 135, 147, 150]
print(binarySearch(lisN, n))
