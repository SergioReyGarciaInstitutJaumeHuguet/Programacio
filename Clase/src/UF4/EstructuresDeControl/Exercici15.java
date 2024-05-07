package UF4.EstructuresDeControl;
import java.util.Scanner;
public class Exercici15 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.println("Inserta el número de alumnos que van a la excursión");
		int alumnes = text.nextInt();
		text.close();
		int euros;
		if(alumnes >= 100) {euros = 65; System.out.println("En total costará " + euros*alumnes + "€");}
		else if(alumnes >= 50 && alumnes < 100) {euros = 70; System.out.println("En total costará" + euros*alumnes + "€");}
		else if(alumnes <= 30 && alumnes < 50) {euros = 95; System.out.println("En total costará" + euros*alumnes + "€");}
		else {euros = 4000; System.out.println("En total costará" + euros + "€");}

	}

}
