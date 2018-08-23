#The largest Continuous sum is the either Sum of Previous array and current number (or) current number
def largestContinuousSum(arr):
    print(arr)
    if len(arr) == 0:
        return 0
    #Initialize max and current sum always to the first element on array
    max_sum=current_sum = arr[0]
    print('Max sum {} and Current num {} before iteration'.format(max_sum,current_sum))
    #since the first element is already been initialized start from Index 1
    for num in arr[1:]:
        #for each iteration find the maximum sum
        current_sum = max(current_sum+num,num)
        print('Max sum {} and Current num {}'.format(max_sum,current_sum))
        if(current_sum > max_sum):
            max_sum = current_sum
    return max_sum
array = [-1,-2,-1,-3,4,10,10,-10,-1]
maximumContionousSum = largestContinuousSum(array)
print(maximumContionousSum)
