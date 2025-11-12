# for loop
for i in range(5):
    print(f"Iteration {i}")

for i in range(2, 7):
    print(f"Iteration {i}")

# while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# do-while loop simulation
num = 0
while True:
    print(f"Number is {num}")
    num += 1
    if num >= 5:
        break

# nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
