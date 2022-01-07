package Junior;

import java.util.*;

public class Q3 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in); 
		
		int N = input.nextInt();
		
		int z = 0;
		
		List<Integer> xCoords = new ArrayList();
		List<Integer> yCoords = new ArrayList();
						
		while (z < N) {
			String[] currentLine = input.next().split(",");
			int x = Integer.parseInt(currentLine[0]);
			int y = Integer.parseInt(currentLine[1]);
			
			xCoords.add(x);
			yCoords.add(y);
			
			z = z + 1;
		}

		input.close();

		Collections.sort(xCoords);
		Collections.sort(yCoords);
		
		int smallX = xCoords.get(0) - 1;
		int smallY = yCoords.get(0) - 1;
		int bigX = xCoords.get(xCoords.size() - 1) + 1;
		int bigY = yCoords.get(yCoords.size() - 1) + 1;
		
		System.out.println(smallX + "," + smallY);
		System.out.println(bigX + "," + bigY);
	}

}