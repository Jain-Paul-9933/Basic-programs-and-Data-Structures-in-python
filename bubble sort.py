def bubblsort(list, size, key):
    for sort in range(size-1):
        swap = False
        for i in range(size-1):
            if list[i].get(key) > list[i+1].get(key):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap = True
        if not swap:
            break
        else:
            size -= 1
    return list


list = [
    {'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    {'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    {'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]
size = len(list)
list = bubblsort(list, size, key='transaction_amount')
for i in list:
    print(i)
