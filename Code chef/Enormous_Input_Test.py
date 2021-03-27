a, b = [int(a) for a in input().split()]
input_no = []
divisible_count = 0
for i in range(0, a):
    input_no.append(int(input()))
list_length = input_no.__len__()
for j in range(0, list_length):
    if input_no[j] % b == 0:
        divisible_count += 1
print(divisible_count)