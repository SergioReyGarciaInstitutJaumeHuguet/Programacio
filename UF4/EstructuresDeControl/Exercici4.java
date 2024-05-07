package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici4 {
	public static void main(String[] args) {
		Scanner teclat = new Scanner(System.in);
		System.out.print("Dime un número: ");
		int numero1 = teclat.nextInt();
		System.out.print("Dime otro número: ");
		int numero2 = teclat.nextInt();
		if (numero2 == 0) {
			System.out.println("No se puede hacer la división");
		}
		else {
			System.out.println("El resultado de la división entre el número 1 y el número 2 es: " + numero1/numero2);
		}
		teclat.close();
	}

}
