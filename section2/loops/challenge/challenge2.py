for i in range(0, 20):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    
    print(i)


print("-"*80)

# without continue

for i in range(0, 20):
    if i != 0 or i % 3 != 0 or i % 5 != 0:
        print(i)