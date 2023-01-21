package assignment2ec;
/*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */
public class CheckGuess {
	// You don't need GameConfiguration for this class's methods.
	public static  Response checkGuess(String currentGuess, String secretCode) {
		// TODO for your extra credit part testing.  Do not turn this in.
		//get the guess and secret code in charArray form
		char[] secret_code_sequence = secretCode.toCharArray();
		char[] valid_guess_sequence = currentGuess.toCharArray(); 

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
		return new Response(black_pegs, white_pegs);
	}
}
