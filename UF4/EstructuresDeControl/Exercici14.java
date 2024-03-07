package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici14 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.println("Añade un precio inicial a la uva");
		float preuInicial = text.nextFloat();
		char tipo;
		while(true) {
			System.out.println("Añade el tipo de uva que es (A o B)");
			tipo = text.next().charAt(0);
			tipo = Character.toUpperCase(tipo);
			if(tipo=='A' || tipo=='B') {
				break;
			}else {System.out.println("Tienes que poner 'A' o 'B'");}
		}
		int medida;
		while(true) {
			System.out.println("Añade su medida (1 o 2)");
			medida = text.nextInt();
			if(medida==1 || medida==2) {
				break;
			}else {System.out.println("Tienes que poner '1' o '2'");}
		}
		System.out.println("Añade cuantas uvas tienes");
		int inventario = text.nextInt();
		text.close();
		float total = (inventario * preuInicial);
		switch(medida){
		case 1:
			if(tipo == 'A') {
				total = total / (20/100);
			} else { total = total * (30/100); }
		case 2:
			if(tipo == 'B') {
				total = total / (30/100);
			} else { total = total * (50/100);
		}
		}
		System.out.println("El total es: " + total + "€");
	}
}
