package UF4.EstructuresDeControl;
import java.util.Scanner;
public class Exercici6 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.print("Dime una letra: ");
		char caracter = text.next().charAt(0);
        int ascii = (int) caracter;
		text.close();
		if(ascii >= 65 && ascii <= 90) {
			System.out.println("La letra " + caracter + " está en mayuscula");
		} else if (ascii >= 95 && ascii <= 122) {
			System.out.println("La letra " + caracter + " está en minuscula");
		} else {
			System.out.println("No has ingresado una letra correcta");
		}

	}

}
