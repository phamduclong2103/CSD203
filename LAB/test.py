#LAD3:
#def
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)
#def
def find_min(arr,n):
    if n == 1:
        return arr[0]
    else:
        return min(arr[n-1],find_min(arr,n-1))
#def
def find_sum(arr,n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + find_sum(arr,n-1)

#def
def ispalidrome(arr,n):
    if n <=1:
        return 1
    elif arr[0] == arr[n-1]:
        return ispalidrome(arr[1:n - 1], n-2)
    else:
        return 0

#def

# Example usage   
result = sum_recursive(5)
print("SUM: ",result)  # Output: 15