package assignment2ec;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

// import scoreannotation.Score; // for grading script
// import testutils.NoExitSecurityManager;

public class AIChoiceTests {

	static boolean DEBUG = true;
	static int noPegs;
	GameConfiguration gameConfiguration;
	Computer computer;
	
	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	// @Score(1) // for grading script
	public void testMaxNoGuesses() {
		// set up and instantiate Computer class
		// Change if necessary for each test.
		// Each test will have this setup code.
		String [] colors = {"R", "G", "B", "O", "Y", "P"};
		int noPegs = 4;
		int testMode = 1; // not used
		gameConfiguration = new GameConfiguration(testMode, colors, noPegs);
		SecretCodeGenerator scg = new SecretCodeGenerator(gameConfiguration);
		Computer computer = new Computer(gameConfiguration);
		
		// test
		computer.reset();
		String secretCode = scg.getNewSecretCode();
		if (DEBUG)
			System.out.println("Secret Code is " + secretCode);
		int guessesSoFar = 0;
		int maxGuesses = 10; // depends on number of pegs and colors

		while (guessesSoFar <= maxGuesses) {
			String guess = computer.pickNextGuess();
			if (DEBUG)
				System.out.println("Computer guessed " + guess);
			guessesSoFar++;
			Response result = CheckGuess.checkGuess(guess, secretCode);
			if (result.b == noPegs) 
				break;
			computer.setLastResponse(result);
		}

		if (guessesSoFar > maxGuesses)
			fail ("Too many guesses -- " + guessesSoFar);
		if (DEBUG)
			System.out.println(guessesSoFar);
	}
	
	@Test
	// @Score(9) // for grading script
	public void testMultipleMaxGuesses () {
		for (int i = 0; i < 10000; i++) {
			testMaxNoGuesses();
		}
	}
}
