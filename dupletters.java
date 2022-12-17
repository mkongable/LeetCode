// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

public String removeDuplicates(String s) {
      /*
       * create a character stack
       * for every character in the string:
       * 	if the current char matches the one on the top of the stack:
       * 		pop the top char
       * 	else
       * 		add the current char
       */
    	
    	Stack<Character> letters = new Stack<>();
    	for(int i = 0; i < s.length(); i++) {
    		if(letters.size() == 0) {
    			letters.push(s.charAt(i));
    		}else if(s.charAt(i) == letters.peek()) {
    			letters.pop();
    		} else {
    			letters.push(s.charAt(i));
    		}
    	}
    	
    	// pop everything onto new stack so that it can be pulled off nicely
    	Stack<Character> orderString = new Stack<>();
    	while(letters.size() != 0) {
    		orderString.push(letters.pop());
    	}
    	
    	StringBuilder tbr = new StringBuilder();
    	while(orderString.size() != 0) {
    		tbr.append(orderString.pop());
    	}
    	return tbr.toString();
    }