public String removeStars(String s) {
    /*
    * create a stack
    * iterate through the string
    * if the character is not a star, push it to the stack
    * if the character is a star, pop the stack
    * create a new string builder
    * while the stack is not empty, pop the stack and append it to the string builder
    * return the string builder in reverse
    */
    Stack<Character> stack = new Stack<>();
    for(int i = 0; i < s.length(); i++) {
        if(s.charAt(i) != '*') {
            stack.push(s.charAt(i));
        } else {
            stack.pop();
        }
    }
    StringBuilder sb = new StringBuilder();
    while(!stack.isEmpty()) {
        sb.append(stack.pop());
    }
    return sb.reverse().toString();
}