# For Loop -> execute a block of code for a fixed number of times.
#             iterates over a range, string, sequence, etc.

# for counter in reversed(range(1,11)):
#    print(counter)

for x in range(1,11,2):
    print(x)

# for x in range (1,10):
#     if x == 7:
#         continue #or break
#     else:
#         print(x)

credit_no = "1234-5678-9012-3456"
for x in credit_no:
    print(x)