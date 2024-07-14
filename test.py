def find_and_divide(value, arr):
    for index, x in enumerate(arr):
        if x % value == 0:
            arr[index] = x / value
            return True
    return False

def main():
    n = int(input())
    arr_a = list(map(int, input().split()))
    m = int(input())
    arr_b = list(map(int, input().split()))
    (min_arr, max_arr) = (arr_a, arr_b) if n < m else (arr_b, arr_a)
    res = []
    for x in min_arr:
        if find_and_divide(x, max_arr):
            res.append(x)
    print(res)



if __name__ == '__main__':
    main()