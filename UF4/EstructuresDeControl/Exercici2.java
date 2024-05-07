package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici2 {

	public static void main(String[] args) {
		Scanner teclat = new Scanner(System.in);
		System.out.print("Dime un número: ");
		int numero = teclat.nextInt();
		if (numero > 0) {
			System.out.println("Es un número positiu");
		}
		else if(numero < 0) {
			System.out.println("Es un número negatiu");
		}
		else {
			System.out.println("Es un 0");
		}
		teclat.close();
	}

}
