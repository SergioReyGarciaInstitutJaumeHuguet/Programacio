package UF4;
import java.util.Scanner;

public class Input {
	public static void main(String[] args) {
		
		// Declaro y inicializo el escaner
		Scanner teclat = new Scanner(System.in);
		// Pido el nombre
		System.out.print("Dime tu nombre: ");
		String texto = teclat.nextLine();
		// Printeo
		System.out.println("Hola " + texto);
		// Cierro la conexión con el teclado
		System.out.print("Ahora un número: ");
		int numero = teclat.nextInt();
		System.out.println("Tu número es: " + numero);
		teclat.close();
		}
}
