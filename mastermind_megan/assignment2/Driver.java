/*
 * EE422C Project 2 (Mastermind) submission by Kevin Li
 * Kevin Li
 * kal3552
 * Slip days used: 0
 * Fall 2020
 */

package assignment2;
import java.util.Scanner;

public class Driver {
    public static void main(String[] args) {
    	String[] colors = new String[] {"R", "G", "B", "W", "Y", "K"}; //k == black
        GameConfiguration config = new GameConfiguration(10, colors, 6);
        SecretCodeGenerator gen = new SecretCodeGenerator(config);
        start(false, config, gen);
    }

    public static void start(Boolean isTesting, GameConfiguration config, SecretCodeGenerator generator) {
    	Scanner userInput = new Scanner(System.in);
    	System.out.println("Welcome to Mastermind.");
    	while(true) { //loop creates a game if the user types Y
	    	System.out.println("Do you want to play a new game? (Y/N):");
			String userResponse = userInput.nextLine();
			if (userResponse.equals("N")) {
				//quit the game
				return;
			}
			Game newGame = new Game(userInput, config, generator, isTesting); //create new game
			newGame.runGame();
    	}
    }
}
