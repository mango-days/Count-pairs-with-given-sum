# Count pairs with given sum

# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

array = [ 1, 5, 7, 1 ]
req_sum = 6
pair_count = 0
for index1 in range ( 0 , len ( array ) - 1 ) :
    for index2 in range ( index1+1 , len ( array ) ) :
        if array [ index1 ] + array [ index2 ] == req_sum : pair_count += 1
print ( pair_count )
