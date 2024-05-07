package UF4;

public class ExempleClase {
	public static void main (String args[]) {
		// I make the PI code
		final double PI = 3.14159265848989845649865479865;
		System.out.println("El número PI con double es: " + PI);
		// I convert to float
		float piFloat = (float) PI;
		System.out.println("El número PI con float pasado de double es: " + piFloat);
		// I pass to int
		int piInt = (int) piFloat; 
		System.out.println("El número PI con int pasado de float es: " + piInt);
		// I check if it is 10 or 5
		switch(piInt) {
		case 10: System.out.println("El valor de PI es 10");
		case 5: System.out.println("El valor de PI es 5");
		default: System.out.println("El valor de PI no es ni 10 ni 5");
		}
	}
}
