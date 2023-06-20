def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)
#pass

def find_min(arr, n):
    if n == 1:
        return arr[0]
    else:
        return min(arr[n-1], find_min(arr, n-1))
#pass

def findsum(a, n):
    if n == 0:
        return 0
    else:
        return a[n - 1] + findsum(a, n - 1)
#pass

def ispalindrome(a, n):
    if n <= 1:
        return 1
    elif a[0] == a[n - 1]:
        return ispalindrome(a[1:n - 1], n - 2)
    else:
        return 0
#pass
  
def binary_search(array, start, end, target):
  if start > end:
    return False

  mid = (start + end) // 2
  if target == array[mid]:
    return True
  elif target > array[mid]:
    return binary_search(array, mid + 1, end, target)
  else:
    return binary_search(array, start, mid - 1, target)
#pass

def cal_gcd(number1, number2):
  if number2 == 0:
    return number1
  return cal_gcd(number2,number1%number2)
#pass

def power(x,n):
  if n == 0:
    return 1
  return x*power(x,n-1)
#pass
def factorial(n):
  if n == 1:
    return 1
  return n*factorial(n-1)
#pass
def fibonacci(n):
  if n <= 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
#pass
def addReciprocals(n):
  if n == 1:
    return 1
  return 1/n + addReciprocals(n-1)
#pass
class BinaryTree:
  def __init__(self, root):
    self.root = root

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def height(self):
    pass
#pass

# Example usage   
result = sum_recursive(5)
print("SUM: ",result)  # Output: 15

# Example usage
arr = [5, 2, 8, 1, 4]
result = find_min(arr, len(arr))
print("MIN: ",result)  # Output: 1

# Example usage
arr = [1, 2, 3, 4, 5]
result = findsum(arr, len(arr))
print(result)  # Output: 15

# Example usage
arr1 = [1, 2, 3, 2, 1]
result1 = ispalindrome(arr1, len(arr1))
print(result1)  # Output: 1 (arr1 is a palindrome)

arr2 = [1, 2, 3, 4, 5]
result2 = ispalindrome(arr2, len(arr2))
print(result2)  # Output: 0 (arr2 is not a palindrome)

# Example usage
my_list = [2, 3, 4, 9]
print(binary_search(my_list, 0, len(my_list) - 1, 4))

# Example usage
number1 = 42
number2 = 18
print(cal_gcd(number1, number2))

# Example usage
print(power(2,3))
# Example usage
print(factorial(5)) 
# Example usage
print(fibonacci(5))
# Example usage
print(addReciprocals(3))
# Example usage

# Example usage

# Example usage

# Example usage

# Example usage

