package UF4.EstructuresDeControl;

import java.util.Scanner;

public class Exercici8 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);
		int Age;
		float Nota;
		char Sex;
		System.out.print("Dime la nota: ");
		Nota = text.nextFloat();
		System.out.print("Dime tu edad: ");
		Age = text.nextInt();
		while(true) {
			System.out.print("Dime tu sexo (F o M): ");
			Sex = text.next().charAt(0);
	        Sex = Character.toUpperCase(Sex);
	        if(Sex=='F' || Sex=='M'){break;}
	        else {System.out.println("Solo puedes poner 'F' (Female) o 'M' (Male)");}
		}
		text.close();
		if(Nota >= 5 && Age >= 18) {
			if(Sex == 'F') {System.out.println("ACCEPTADA");}
			else {System.out.println("POSSIBLE");}
		}
		else {System.out.println("NO ACCEPTADA");}
	}

}

