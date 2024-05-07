package UF4.EstructuresDeControl;

import java.util.Scanner;

public class Exercici7 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.print("Dime la base: ");
		int base = text.nextInt();
		System.out.print("Dime la exponent: ");
		int exponent = text.nextInt();
		text.close();
		System.out.print("Resultat: ");
		if(exponent > 0) {
			System.out.print(base*exponent);
		} else if(exponent == 0) {
			System.out.print(1);
		}else {
			System.out.print(1/(base*(exponent*exponent)));
		}
	}

}
