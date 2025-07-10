#BRUTE FORCE

arr=[1,2,5,8,6,9,4,5,78,8,5,8,5,8,5,8,5]
sort_arr=arr.sort()
n=len(arr)
print("largest element",arr[n-1])






#OPTIMAL

array=[1,2,5,8,6,9,4,5,78,8,5,8,5,8,5,8,5]
n=len(array)

def largest_element(array,n):
    largest=array[n-1]
    for i in array:
        if i>largest:
            largest=i


    return largest


print(largest_element(array,n))