def quick_select(arr, k):
    '''
    Quick Select 是一种用于在未排序的数组中查找第 k 小元素的算法。它与快速排序（Quick Sort）算法类似，但只关注找到第 k 小的元素，而不是对整个数组进行排序。Quick Select 的平均时间复杂度为 O(n)
    
    以下是 Quick Select 算法的步骤：
    1. 选择一个枢轴（pivot）元素。
    2. 将数组分成两部分：小于枢轴的元素和大于枢轴的元素。
    3. 判断枢轴的位置：
        a. 如果枢轴的位置正好是 k，则返回枢轴元素。
        b. 如果枢轴的位置大于 k，则在左半部分递归查找第 k 小元素。
        c. 如果枢轴的位置小于 k，则在右半部分递归查找第 (k - pivot 位置 - 1) 小元素。
    '''
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_num = len(arr) - len(left) - len(right)

    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + pivot_num:
        return pivot
    else:
        return quick_select(right, k - len(left) - pivot_num)

if __name__ == '__main__':
    # 示例用法
    arr = [3, 2, 1, 5, 4]
    k = 2
    print(f"数组中第 {k} 小的元素是: {quick_select(arr, k)}, arr={arr}")