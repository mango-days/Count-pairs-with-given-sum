array = [ 1, 5, 7, 1 ]
req_sum = 6

pair_count = 0
library = {}

for index in range ( 0 , len ( array ) ) :
    temp = array [ index ]
    if temp not in library : library [ temp ] = 1
    else : library [ temp ] += 1
    
for x in library.keys() :
    temp = req_sum - x
    if temp in library.keys() : 
        pair_count += 1 
        
print ( pair_count ) 
