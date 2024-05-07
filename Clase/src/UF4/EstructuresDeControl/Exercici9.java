package UF4.EstructuresDeControl;
import java.util.Scanner;
public class Exercici9 {

	public static void main(String[] args) {
		Scanner text = new Scanner (System.in);
		System.out.println("Dime un número");
		int num1 = text.nextInt();
		System.out.println("Ahora otro");
		int num2 = text.nextInt();
		System.out.println("Por último, otro número");
		int num3 = text.nextInt();
		text.close();
		if(num1 > num2) {
			if(num2>num3) {System.out.println("Los números ingresados son: " + num1 + ", " + num2 + ", " + num3);}
			else if(num1>num3){System.out.println("Los números ingresados son: " + num1 + ", " + num3 + ", " + num2);}
			else {System.out.println("Los números ingresados son: " + num3 + ", " + num1 + ", " + num2);}
		}
		else if(num2>num3){
			if(num1>num3) {System.out.println("Los números ingresados son: " + num2 + ", " + num1 + ", " + num3);}
			else {System.out.println(String.format("%a, %b, %c", num2, num3, num1));}
		}
		else {
			{System.out.println("Los números ingresados son: " + num3 + ", " + num2 + ", " + num1);}
		}

	}

}
