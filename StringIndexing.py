# String indexing
# Accessing index of a sequence using []
#                   [start:end:step]

name = "Hrishav Sarma"
#       ^^^^^^^^^^^^^
#       0123456789123 
#print(name[1:7])
# start is inclusive and end is exclusive
credit_no="1234-5678-9012-3456"
last_4digits= credit_no[-4:]

#-1 in step reverses the whole string
reverse = credit_no[::-1]

print(f"XXX-XXX-XXX-{last_4digits}")
print(reverse)

