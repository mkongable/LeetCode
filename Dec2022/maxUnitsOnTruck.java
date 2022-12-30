public int maximumUnits(int[][] boxTypes, int truckSize) {
    //sort by box capacity, and then start taking the boxes with biggest capacity
    Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
    int units = 0;
    int loadedBoxes = 0;
    for (int i = 0; i < boxTypes.length; i++) {
        int boxes = boxTypes[i][0];
        int capacity = boxTypes[i][1];
        if (loadedBoxes + boxes <= truckSize) {
            units += boxes * capacity;
            loadedBoxes += boxes;
        } else {
            //last load is a partial load
            int remainingBoxes = truckSize - loadedBoxes;
            units += remainingBoxes * capacity;
            loadedBoxes += remainingBoxes;
            break;
        }
    }
    return units;
}