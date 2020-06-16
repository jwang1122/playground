# Python program to demonstrate 
# tell() method 
  
  
# Open the file in read mode 
fp = open("mylogs.log", "r") 
  
# Print the position of handle 
print(fp.tell()) 
  
#Closing file 
fp.close() 

# Python program to demonstrate 
# tell() method 
  
# Opening file 
fp = open("mylogs.log", "r") 
fp.read(8) 
  
# Print the position of handle 
print(fp.tell()) 
  
# Closing file 
fp.close() 


# Python program to demonstrate 
# tell() method 
  
# for reading binary file we 
# have to use "wb" in file mode. 
fp = open("mylogs.log", "wb") 
print(fp.tell()) 
  
# Writing to file 
fp.write(b'1010101') 
  
print(fp.tell()) 
  
# Closing file 
fp.close() 