def binary_search(num_list, x, left, right):
    if left <= right:
        mid = left + (right - left) // 2

        if num_list[mid] == x:
            return mid
        elif num_list[mid] > x:
            return binary_search(num_list, x, left, mid+1)
        else:
            return binary_search(num_list, x, mid, right)
    else:
        return None


if __name__ == '__main__':
    num = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    num.sort()

    idx = binary_search(num, 30, 0, len(num))
    print(num[idx])
