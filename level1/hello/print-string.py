s = "Hey there! what should this string shoud be"

# Length should be 20
print("04. Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
print("06. The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("08. a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("10. The first five characters are '%s'" % s[:5]) 
# Start to 5
print("12. The next five characters are '%s'" % s[5:10]) 
# 5 to 10
print("14. The thirteenth character is '%s'" % s[12]) 
# Just number 12
print("16. The characters with odd index are '%s'" %s[1::2]) 
#(0-based indexing)
print("18. The last five characters are '%s'" % s[-5:]) 
# 5th-from-last to end# Convert everything to uppercase
print("20. String in uppercase: %s" % s.upper())
