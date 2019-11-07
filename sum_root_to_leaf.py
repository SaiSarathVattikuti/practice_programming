#Time:O(N),Space:O(N)
def maxSums(array):
    if (len(array)==0):
        return 0
    elif(len(array)==1):
        return array[0]
    maxSums=array[:]
    maxSums[1]=max(array[0],array[1])
    for i in range(2,len(array)):
        maxSums[i]=max(array[i-1],array[i-2]+array[i])
    return(maxSums[-1])    