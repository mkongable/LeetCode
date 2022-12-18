    //https://leetcode.com/problems/daily-temperatures
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> index_stack = new Stack<>();
        Stack<Integer> temp_stack = new Stack<>();
        int[] result = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!temp_stack.isEmpty() && temperatures[i] > temp_stack.peek()) { //new temp incoming, while they are still cooler temperatures in the stack, pop them and update their indices in the result array to the index of this new incoming temp
                result[index_stack.peek()] = i - index_stack.peek();
                index_stack.pop();
                temp_stack.pop();
            }
            index_stack.push(i);
            temp_stack.push(temperatures[i]);
        }
        //anything that remains in the stack has no warmer solution
        while (!index_stack.isEmpty()) {
            result[index_stack.pop()] = 0;
        }
        return result;
    }