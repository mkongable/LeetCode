    public int evalRPN(String[] tokens) {
    /*
     * create a stack
     * for every input:
     * 		if input is number:
     * 			push onto the stack
     * 		else if operand is encountered
     * 			pop top two numbers off and perform the calc
     * 			push the result back in
     * return the final int   
     */
    	Stack<Integer> stack = new Stack<>();
    	for(int i = 0; i < tokens.length; i++) {
    		if(tokens[i].equals("+")) {
    			int num1 = stack.pop();
    			int num2 = stack.pop();
    			stack.push(num1 + num2);
    		} else if(tokens[i].equals("-")) {
    			int num1 = stack.pop();
    			int num2 = stack.pop();
    			stack.push(num2 - num1);
    		} else if(tokens[i].equals("/")) {
    			int num1 = stack.pop();
    			int num2 = stack.pop();
    			stack.push(num2 / num1);
    		} else if(tokens[i].equals("*")) {
    			int num1 = stack.pop();
    			int num2 = stack.pop();
    			stack.push(num2 * num1);
    		} else {
    			stack.push(Integer.parseInt(tokens[i]));
    		}
    	}
    	return stack.pop();
    }