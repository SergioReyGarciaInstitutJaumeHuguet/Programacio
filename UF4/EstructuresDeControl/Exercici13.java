package UF4.EstructuresDeControl;
import java.util.Scanner;
public class Exercici13 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		System.out.print("Dime un día: ");
		int day = text.nextInt();
		System.out.print("Dime un mes: ");
		int month = text.nextInt();
		System.out.print("Dime un año: ");
		int year = text.nextInt();
		text.close();
		switch(month) {
		case 2:
			if (((year % 4 == 0) && (year % 100 != 0 || year % 400 == 0)) && year > 0) {
				if(day > 29 || day < 1) {
					System.out.println("La fecha " + day + "/" + month + "/" + year + " no es una fecha válida");
				} else {
					System.out.println("La fecha " + day + "/" + month + "/" + year + " es una fecha válida");
				}
			} else {System.out.println("La fecha " + day + "/" + month + "/" + year + " no es una fecha válida");}
			break;
		default: 
			if(day > 0 && day < 29) {
				if (month < 12 && month > 0) {
					if(year > 0) {
						System.out.println("La fecha " + day + "/" + month + "/" + year + " es un afecha válida");
					} else {System.out.println("La fecha " + day + "/" + month + "/" + year + " no es una fecha válida");}
				} else {System.out.println("La fecha " + day + "/" + month + "/" + year + " no es una fecha válida");}
			} else {System.out.println("La fecha " + day + "/" + month + "/" + year + " no es una fecha válida");}
		}
	}

}
