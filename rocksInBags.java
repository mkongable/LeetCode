public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
    /*
    * create an array of rocks needed (capacity[i] - rocks[i]) to fill each bag
    * sort the array
    * run through the array and subtract from the additional Rocks to fill each bag
    * break out of the array at the end or if additional rocks is <= 0
    */ 
    int[] rocksNeeded = new int[capacity.length];
    for(int i = 0; i < capacity.length; i++) {
        rocksNeeded[i] = capacity[i] - rocks[i];
    }

    Arrays.sort(rocksNeeded);
    int bagsFilled = 0;
    for(int i = 0; i < rocksNeeded.length; i++) {
        if(additionalRocks - rocksNeeded[i] >= 0) {
            additionalRocks -= rocksNeeded[i];
            bagsFilled++;
        } else {
            break;
        }
    }
    return bagsFilled;
}

public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
/*add the difference between each capacity and the rocks in the bag so far to a min heap. Then keep taking the minimum of the min heap and use additionalRocks to cover*/
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    for(int i = 0; i < capacity.length; i++) {
        minHeap.add(capacity[i] - rocks[i]);
    }
    int bagsFilled = 0;
    while(!minHeap.isEmpty()) {
        int rocksNeeded = minHeap.poll();
        if(additionalRocks >= rocksNeeded) {
            additionalRocks -= rocksNeeded;
            bagsFilled++;
        } else {
            break;
        }
    }
    return bagsFilled;
}