# Uses python3
def calc_fib(n, k):
    """
    Given: Positive integers n≤100 and m≤20.

    Return: The total number of pairs of rabbits that will remain 

    after the n-th month if all rabbits live for m months.
    """

    array = [1, 1, 1]
    if n <= 2:
        return array[-1]
    for i in range(3, n+1):
        if i > k:
            array.append(array[i-2] + array[i-1]- array[i-k-1])
        else:
            array.append(array[i-2] + array[i-1]) 
    return array[-1]