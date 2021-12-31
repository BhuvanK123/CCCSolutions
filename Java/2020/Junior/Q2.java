package Junior;

import java.util.*;

public class Q2 {
    public static void main(String[] args) {
	
        Scanner input = new Scanner(System.in);
	    
	    int P = input.nextInt(); // when to stop the program after it reaches a certain number of people
	    int N = input.nextInt(); // number of people who have the virus on day 0
	    int R = input.nextInt(); // number of people infected each succeeding day
	    
	    int days = 0;
	    int infected = N;
	    int infected_total = N;
	    
	    while (infected_total < P) {
	    	infected = infected * R;
	        infected_total += infected;
	        days=days+1;
	    }
	    
        System.out.println(days);
	    input.close();
	}

}
