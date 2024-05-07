package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici1 {

	public static void main(String[] args) {
		Scanner teclat = new Scanner(System.in);
		System.out.print("Dime un número: ");
		int numero1 = teclat.nextInt();
		System.out.print("Ahora dime otro número: ");
		int numero2 = teclat.nextInt();
		if (numero1 > numero2) {
			System.out.println("El primer número es más grande: " + numero1);
		}
		else if(numero2 > numero1) {
			System.out.println("El segundo número es más grande: " + numero2);
		}
		else {
			System.out.println("Los dos números son iguales");
		}
		teclat.close();
	}

}
