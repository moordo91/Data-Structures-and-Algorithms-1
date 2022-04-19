class Minheap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.FRONT = 1
    
    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):
        return 2 * pos
    
    def rightChild(self, pos):
        return 2 * pos + 1
    
    def isLeaf(self, pos):
        return pos * 2 > self.size
    
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" p " + str(self.Heap[i]) + " le " + str(self.Heap[2*i]) + " re " + str(self.Heap[2*i+1]))
    
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def Insert(self, element):

        if self.size > self.maxsize:
            return
        
        self.size += 1
        self.Heap[self.size] = element

        print("Insert: " + str(element))

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def heapDown(self, pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapDown(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapDown(self.rightChild(pos))

    def remove(self):

        popped = self.Heap[self.FRONT]

        self.Heap[self.FRONT] = self.Heap[self.size]

        self.size -= 1
        self.heapDown(self.FRONT)
        
        self.Heap[self.size+1] = 0
        
        return popped

if __name__ == "__main__":

    print("The minHeap is ")
    minHeap = Minheap(15)
    minHeap.Print()

    minHeap.Insert(5)
    minHeap.Print()

    minHeap.Insert(3)
    minHeap.Print()

    minHeap.Insert(17)
    minHeap.Print()

    minHeap.Insert(10)
    minHeap.Print()

    minHeap.Insert(84)
    minHeap.Print()

    print("the min value is " + str(minHeap.remove()))
    print("Heap Status -----------------------")
    minHeap.Print()

    print("the min value is " + str(minHeap.remove()))
    print("Heap Status -----------------------")
    minHeap.Print()

    print("the min value is " + str(minHeap.remove()))
    print("Heap Status -----------------------")
    minHeap.Print()
