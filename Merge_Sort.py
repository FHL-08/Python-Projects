def main():
    inp = input("Enter an array of numbers: ")
    array = inp.split(", ")
    int_arr = [int(i) for i in array]
    print("Here is the sorted array: ")
    print(merge_sort(int_arr))


def merge(left, right):
    if (len(left) == 0):
        return left
    if (len(right) == 0):
        return right

    result = []
    index_left = index_right = 0

    while (len(result) < (len(left) + len(right))):
        if (left[index_left] <= right[index_right]):
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if (index_left == len(left)):
            result += (right[index_right:])
            break
        if (index_right == len(right)):
            result += (left[index_left:])
            break
    
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid_pt = len(arr)//2
    return merge(merge_sort(arr[:mid_pt]), merge_sort(arr[mid_pt:]))

main()
