# Uses python3
def calc_fib(n, k):
    """
    Given: Positive integers n≤40 and k≤5.

     Return: The total number of rabbit pairs that 

     will be present after n months, if we begin with 1 pair and in each generation, 

     every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

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