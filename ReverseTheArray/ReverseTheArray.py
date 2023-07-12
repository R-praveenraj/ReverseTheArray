#You are given a constant array A.
#You are required to return another array which is the reversed form of the input array.

def Reverse(array):
    j=len(array)-1
    for i in range(0,(len(array)//2)):
        array[i],array[j]=array[j],array[i]
        j-=1
    return array

        


array = [1, 2, 3, 2,1]

print(Reverse(array))