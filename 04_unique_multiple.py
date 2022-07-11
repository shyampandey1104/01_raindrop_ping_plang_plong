def sum_of_multiples(a1,a2,n):
    
    total_sum = 0
    for i in range(1, n):
        if (i % a1 == 0 or i % a2 == 0):
            total_sum = total_sum + i

    return total_sum

print(sum_of_multiples(3,5,20))