def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == '__main__':
    l = [23, 8, 15, 17, 4, 40, 11, 31]
    bubble_sort(l)
    print(l)