package assignment2;
import java.util.*;
/*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */
public class Game {
	private int guesses_left;
	private String[] colors;
	private boolean testing_mode;
	private Scanner user_input;
	private String secret_code;
	
	public Game(Scanner userInput, GameConfiguration config, SecretCodeGenerator gen, boolean testingMode) {
		this.testing_mode = testingMode;
		this.guesses_left = config.guessNumber;
		this.colors = config.colors;
		this.user_input = userInput;
		this.secret_code = gen.getNewSecretCode();
	}
	
	public void runGame() {
		GuessValidator rulePolice = new GuessValidator(colors, secret_code);
		Feedback feedback = new Feedback(secret_code);
		String[] history = new String[guesses_left]; //history buffer which stores the history so far
		int historyIndex = 0;
		
		if (testing_mode) {
			System.out.println("Secret code: " + secret_code);
		}
		while (guesses_left > 0) {
			System.out.println();
			System.out.println("You have " + guesses_left + " guess(es) left.");
			System.out.println("Enter guess:");
			String userGuess = user_input.nextLine();
			if (userGuess.equals("HISTORY")) { //quick check for the history keyword before validation
				for (int i = 0; i < historyIndex; i++) {
					System.out.println(history[i]);
				}
				continue;
			}
			rulePolice.setGuess(userGuess);
			while (!rulePolice.isValidGuess()) { //validation of user guess
				System.out.println("INVALID_GUESS");
				System.out.println("");
				System.out.println("You have " + guesses_left + " guess(es) left.");
				System.out.println("Enter guess:");
				userGuess = user_input.nextLine();
				rulePolice.setGuess(userGuess);
			}
			feedback.setValid_guess(userGuess);
			String pegs = feedback.getPegFeedback();
			System.out.println(pegs);
			history[historyIndex] = pegs; //store the previous guess and feedback in the history
			historyIndex++; //increment the history counter
			if (feedback.foundSecretCode()) { 
				System.out.println("You win!");
				System.out.println();
				return;
			}
			guesses_left--;
		}
		System.out.println("You lose! The pattern was " + secret_code);
		System.out.println();
	}
}
