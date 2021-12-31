package Junior;

import java.util.*;

public class Q1 {
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
	    // Scanner m = new Scanner(System.in);
	    // Scanner l = new Scanner(System.in);
	    
	    int Sval =  s.nextInt();
	    int Mval = s.nextInt();
	    int Lval = s.nextInt();
	    
	    int total = Sval*1 + Mval*2 + Lval*3; 
	
	    if (total >= 10) {
	      System.out.println("happy");
	    }
	    else if (total < 10) {
	      System.out.println("sad");
	    }
	    
	    s.close();
	    // m.close();
	    // l.close();
	}
}
