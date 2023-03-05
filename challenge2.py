def byte_xor(a, b):
    if (a==b):
        return 0
    else:
        return 1




hex_1= "1c0111001f010100061a024b53535009181c"
hex_2="686974207468652062756c6c277320657965"
hex_3=""


#converting to binary from hex

bin_1 = bin(int(hex_1,16))
bin_2=bin(int(hex_2, 16))



#buffering the integers 
if len(bin_1)>len(bin_2):
    length=len(bin_1)

else:
    length=len(bin_2)



bin_1=bin_1[2:]
bin_2=bin_2[2:]



bin_1=bin_1.zfill(length)
bin_2=bin_2.zfill(length)



count=0

while (count<len(bin_1)):
    hex_3+=str(byte_xor(bin_1[count],bin_2[count]))
    count=count+1



print(hex(int(hex_3,2)))