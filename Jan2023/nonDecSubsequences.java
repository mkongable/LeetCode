public List<List<Integer>> findSubsequences(int[] nums) {
    //keep a hashmap H of the index to all subsequences that end with that index
    //for every element E in nums:
        //append E as a singular subsequence to the hashmap
        //for every element e at an index less than E's index:
            //if e <= E:
                //copy every subsequence that ends with e using the hashmap and append E to it, then add the new subsequence to the hashmap
    //return all subsequences that are stored in the hashmap that are not duplicates and have a length greater than 1

    HashMap<Integer, List<List<Integer>>> H = new HashMap<>();
    //make a set containig all seen subsequences
    HashSet<List<Integer>> seen = new HashSet<>();
    for (int i = 0; i < nums.length; i++) {
        List<List<Integer>> SSendingAti = new ArrayList<>();
        SSendingAti.add(Arrays.asList(nums[i]));
        for (int j = 0; j < i; j++) {
            if (nums[j] <= nums[i]) {
                //can append to all subsequences ending at j
                List<List<Integer>> SSendingAtj = H.get(j);
                //make a copy of all these subsequences and append nums[i] to each one of them
                for (int k = 0; k < SSendingAtj.size(); k++) {
                    ArrayList<Integer> newSubsequence = new ArrayList<>(SSendingAtj.get(k)); //hope this makes a copy
                    newSubsequence.add(nums[i]);
                    SSendingAti.add(newSubsequence);
                }
            }
        }
        H.put(i, SSendingAti);
    }

    //loop through every index's subsequences and stuff them all into the hashset
    for (int i = 0; i < nums.length; i++) {
        for (List<Integer> SS : H.get(i)) {
            seen.add(SS);
        }
    }

    //loop through the hashset and add to the result array IF the size is greater than 1
    List<List<Integer>> result = new ArrayList<>();
    for (List<Integer> entry : seen) {
        if (entry.size() > 1) {
            result.add(entry);
        }
    }

    return result;
}