import collections


def solution(T):
    shared_amount = len(T) / 2
    counter = collections.Counter(T)
    sorted_dict = collections.OrderedDict(sorted(counter.items(), key=lambda kv: kv[1]))
    for k, v in sorted_dict.items():
        shared_amount -= v-1
    if shared_amount == 0:
        return len(sorted_dict)-1
    else:
        return len(sorted_dict)

if __name__ == '__main__':
    print(solution([3, 4, 7, 7, 6, 6]))