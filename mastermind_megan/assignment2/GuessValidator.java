package assignment2;
/*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */

public class GuessValidator {
	private String guess;
	private String[] colors;
	private String secret_code;
	
	public String getGuess() {
		return guess;
	}

	public void setGuess(String guess) {
		this.guess = guess;
	}

	public GuessValidator(String[] colors, String guess, String secret_code) {
		this.guess = guess;
		this.colors = colors;
		this.secret_code = secret_code;
	}
	
	public GuessValidator(String[] colors, String secret_code) {
		this.colors = colors;
		this.guess = null;
		this.secret_code = secret_code;
	}
	
	public boolean isValidGuess() {
		if (guess.length() != secret_code.length()) { //guess must be the same length as the number of pegs
			return false;
		}
		for (int i = 0; i < guess.length(); i++) {
			if (!colorIsValid(guess.substring(i, i + 1))) { //color must be a valid color in the color pool
				return false;
			}
		}
		return true;
	}
	
	public boolean colorIsValid(String color) {
		//checks if a given color is contained within the color pool (valid)
		for (int i = 0; i < colors.length; i++) {
			if (color.equals(colors[i])) {
				return true;
			}
		}
		return false;
	}
	
	
	
	
}
