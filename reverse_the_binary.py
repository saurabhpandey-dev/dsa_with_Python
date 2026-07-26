# dec = 8
# print(dec)
# dec_bin = str(bin(dec)) # convert decimal to bin in str
# dec_bin = dec_bin[2:] # delete first two letter 0b
# print(dec_bin)

# rev = '0b' # store 0b in rev firstly
# for i in range(len(dec_bin)-1,-1,-1): # reverse loop for dec_bin
#     rev = rev+dec_bin[i]  # add all element in rev

# bin_dec = int(rev,2) # convert binary to decimal
# print(rev)
# print(bin_dec) # print it 



n = 10
result = 0
rem = 0
while(n>0):
    rem = n & 1
    result = result << 1+rem 
    n = n >> 1

# rem = n & 1
print(rem)  