from collections import deque

class MinHeap:
    def __init__(self):
        self.heap = deque()
    
    def sift_up(self, index):
        '''
        上滤操作，比较当前节点与其父节点的值，如果当前节点更小则交换位置，直到堆性质恢复
        '''
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            # 交换当前节点与父节点
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
    
    def sift_down(self, index):
        '''
        下滤操作，比较当前节点与其子节点的值，如果有更小的子节点则交换位置，直到堆性质恢复
        '''
        size = len(self.heap)
        while True:
            smallest = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            
            if left_child_index < size and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            
            if right_child_index < size and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index
            
            if smallest != index:
                # 交换当前节点与最小子节点
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
    
    def heappush(self, item):
        '''
        向堆中添加一个新元素，先将元素添加到堆的末尾，然后进行上滤操作恢复堆性质
        '''
        self.heap.append(item)  # O(1)
        self.sift_up(len(self.heap) - 1)  # O(log n)

    def heappop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        min_item = self.heap[0]
        # 用最后一个元素替换堆顶
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # O(1)
        self.sift_down(0)  # O(log n)
        return min_item