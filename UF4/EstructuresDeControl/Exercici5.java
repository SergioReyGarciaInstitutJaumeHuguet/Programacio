package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici5 {

	public static void main(String[] args) {
		Scanner teclat = new Scanner(System.in);
		System.out.print("Dime el usuario: ");
		String user = teclat.nextLine();
		System.out.print("Ahora la contraseña: ");
		String password = teclat.nextLine();
		if(user == "anna" && password == "1234") {
			System.out.println("Sesión iniciada");
		}
		else {
			System.out.println("No has entrado");
		}
		teclat.close();

	}

}
