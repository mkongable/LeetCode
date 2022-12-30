public int lastStoneWeight(int[] stones) {
    //use a max heap to find the biggest stones in LogN
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    //put every element in stones in the max heap
    for (int stone : stones) {
        maxHeap.add(stone);
    }
    while (maxHeap.size() > 1) {
        //remove the two biggest stones
        int stone1 = maxHeap.remove();
        int stone2 = maxHeap.remove();
        //if they are not equal, put the difference back in the heap
        if (stone1 != stone2) {
            maxHeap.add(stone1 - stone2);
        }
    }
    //if there is only one stone left, return it
    if (maxHeap.size() == 1) {
        return maxHeap.remove();
    }
}