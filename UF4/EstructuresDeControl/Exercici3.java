package UF4.EstructuresDeControl;

import java.util.Scanner;

public class Exercici3 {

	public static void main(String[] args) {
		Scanner teclat = new Scanner(System.in);
		System.out.print("Dime un número: ");
		int numero = teclat.nextInt();
		if (numero%2 == 0) {
			System.out.println("Es parell");
		}
		else {
			System.out.println("Es imparell");
		}
		teclat.close();
	}

}
