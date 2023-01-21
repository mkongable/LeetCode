package assignment2;
/*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */
public class Feedback {
	private String valid_guess;
	private String secret_code;
	private boolean found_code = false;
	
	public Feedback(String secret_code, String valid_guess) {
		this.valid_guess = valid_guess;
		this.secret_code = secret_code;
	}
	
	public Feedback(String secret_code) {
		this.secret_code = secret_code;
	}
	
	public String getValid_guess() {
		return valid_guess;
	}

	public void setValid_guess(String valid_guess) {
		this.valid_guess = valid_guess;
	}
	
	public String getPegFeedback() {
		//get the guess and secret code in charArray form
		char[] secret_code_sequence = secret_code.toCharArray();
		char[] valid_guess_sequence = valid_guess.toCharArray(); 

		int black_pegs = 0;
		int white_pegs = 0;
		//count up the black pegs and mark the matches with #
		for (int i = 0; i < secret_code_sequence.length; i++) {
			if (secret_code_sequence[i] == valid_guess_sequence[i]) {
				black_pegs ++;
				secret_code_sequence[i] = '#';
				valid_guess_sequence[i] = '#';
			}
		}
		//duplicates have been found, look for and cancel out white peg matches for every letter 
		//in guess
		for (int i = 0; i < valid_guess_sequence.length; i++) {
			if (valid_guess_sequence[i] == '#') {
				continue;
			}
			for (int j = 0; j < secret_code_sequence.length; j++) {
				if (valid_guess_sequence[i] == secret_code_sequence[j]) {
					valid_guess_sequence[i] = '#';
					secret_code_sequence[j] = '#';
					white_pegs ++;
					break;
				}
			}
		}
		if (black_pegs == secret_code.length()) {
			found_code = true;
		}
		//return the guess response as a formatted string
		String pegMessage = valid_guess + " -> " + black_pegs + "b_" + white_pegs + "w";
		return pegMessage;
	}
	
	public boolean foundSecretCode() {
		return found_code;
	}
}
