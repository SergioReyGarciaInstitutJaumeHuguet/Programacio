// Falta por hacer
package UF4.EstructuresDeControl;
import java.util.Scanner;
public class Exercici16 {
	static Scanner TEXT = new Scanner(System.in);
	
	public static int dia(char day) {
		if(day == 'D') {
			return 3;
		} else {
			char dia;
			while(true) {
				System.out.println("M - Mañana");
				System.out.println("T - Tarde");
				System.out.println("¿Mañana o tarde?");
				dia = TEXT.next().charAt(0);
				dia = Character.toUpperCase(dia);
				if(dia == 'M') {return 15;}
				else if(dia == 'T') {return 10;}
				else {System.out.println("No es una opción válida");}
			}
		}
	}
	
	public static int minuts(int minuts) {
		
	}
	
	public static void main(String[] args) {
		char day;
		while(true) {
			System.out.println("L - Lunes");
			System.out.println("M - Martes");
			System.out.println("X - Miercoles");
			System.out.println("J - Jueves");
			System.out.println("V - Viernes");
			System.out.println("S - Sabado");
			System.out.println("D - Domingo");
			System.out.print("Dime el día: ");
			day = TEXT.next().charAt(0);
			day = Character.toUpperCase(day);
			if(day != 'L' && day != 'M' && day != 'X' && day != 'J' && day != 'V' && day != 'S' && day != 'D') {
				System.out.println("No es una opción correcta");
			} else {break;}
		}
		int dia = dia(day);
		System.out.println(dia);
		TEXT.close();
	}

}
