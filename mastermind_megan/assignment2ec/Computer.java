/*
 * Author: Vallath Nandakumar
 * June 10. 2020
 * 
 * /*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */

package assignment2ec;
import java.util.*;


public class Computer {

	private String lastGuess;
	private Response lastResponse;
	private GameConfiguration gameConfiguration;
	private ArrayList<String> possibilities;
	
	public Computer (GameConfiguration gameConfiguration) {
		this.gameConfiguration = gameConfiguration;
		// TODO: Add whatever else you want here
	}

	public void setLastResponse (Response r) {
		lastResponse = r;
		//cross out any combination that would not give the same response if it were the secret code
		//get a response from the guess, any survivor combination that doesn't give the same cannot possibly be the secret code
		for (int i = 0; i < possibilities.size(); i++) {
			Response compare = copyCheckGuess(lastGuess, possibilities.get(i));
			if (!compare.equals(lastResponse)) {
				possibilities.set(i, "@");
			}
		}
	}

	public void reset () {
		lastResponse = null;
		// TODO: anything else you want here
		possibilities = new ArrayList<String>();
		getCombinations();
		
		//get the all the possible combinations and return them as arraylist of strings
	}
	
	public void getCombinations() {
		String starter = "";
		getCombinationsHelper(gameConfiguration.pegNumber, starter);
	}
	
	public void getCombinationsHelper(int layer, String s) {
		if (layer == 0) {
			possibilities.add(s);
		}
		else {
			for (int i = 0; i < gameConfiguration.colors.length; i++) {
				String copyOfS = s;
				copyOfS = copyOfS + gameConfiguration.colors[i];
				getCombinationsHelper(layer - 1, copyOfS);
			}
		}
	}

	public String pickNextGuess() {
		// TODO: anything else you want here
		for (int i = 0; i < possibilities.size(); i++) {
			if (!possibilities.get(i).equals("@")) {
				lastGuess = possibilities.get(i);
				return possibilities.get(i);
			}
		}
		return "I lost the game and I suck"; //this will never be executed but is there for compiler
	}
	
	public Response copyCheckGuess(String currentGuess, String tempSecretCode) {
		char[] secret_code_sequence = tempSecretCode.toCharArray();
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
