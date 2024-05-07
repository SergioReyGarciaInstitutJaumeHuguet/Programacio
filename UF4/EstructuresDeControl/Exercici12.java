package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici12 {
	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.print("Dime un año: ");
		text.close();
		int year = text.nextInt();
		if ((year % 4 == 0) && (year % 100 != 0 || year % 400 == 0)) {
			System.out.println("Es un año bisiesto");
		}
	}
	
}
