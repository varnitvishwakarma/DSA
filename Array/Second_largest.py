#BRUTE FORCE

arr=[7,8,4,5,9,5,4,8,74,5,5,5,9,9,9,9,9,9,95]
arr.sort()
n=len(arr)
largest=arr[n-1]
for i in range(n-2,0,-1):
    if i < largest:
        print(arr[i])
        break
    else:
        pass


# optimal 


arr=[7,8,4,5,9,5,4,8,74,5,5,5,9,9,9,9,9,9,95]
largest_element=arr[0]
second_element=-1


def second(arr,largest_element,second_element):
    for i in arr:
        if largest_element<i:
            second_element=largest_element
            largest_element=i
            
        elif i<= largest_element:
            if i>second_element:
                second_element=i
            else:
                pass

    return second_element


print(second(arr,largest_element,second_element))