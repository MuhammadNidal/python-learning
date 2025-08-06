numbers=[1,2,3,4,5]
def square(x):
    return x * x



numbers_squared =map(square,numbers)
print(list(numbers_squared))



count=[2,9,8,5,2,4,1,3]

def is_even(x):
    return x % 2 == 0
counting= map(is_even,count)
print(list(counting))


numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))


from functools import reduce
arr1: list[int] = [1, 2, 3]
arr2: list[int] = [4, 5, 6]
arr3: list[int] = [7, 8, 9]
arr = arr1 + arr2 + arr3
arr_sum = reduce(lambda x, y: x + y, arr)
print(arr_sum)