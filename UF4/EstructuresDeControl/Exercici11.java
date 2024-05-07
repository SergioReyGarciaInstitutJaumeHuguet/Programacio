package UF4.EstructuresDeControl;
import java.util.Scanner;

public class Exercici11 {

	public static void main(String[] args) {
		Scanner text = new Scanner(System.in);

        System.out.print("Introduze la longitud del lado A: ");
        double a = text.nextDouble();

        System.out.print("Introduze la longitud del lado B: ");
        double b = text.nextDouble();

        System.out.print("Introduzca la longitud del lado C: ");
        double c = text.nextDouble();
        
        text.close();
        if((a*a)*(b*b) == c) {
        	System.out.println("Es un triangulo rectángulo");
        }
        else if((a == b && a != c) || (b == c && a != b) || (c == a && b != c)) {
        	System.out.println("El un triangulo isóceles");
        }
        else if(a == b && b == c) {
        	System.out.println("Es un triangulo equilatero");
        }
        else {
        	System.out.println("Es un triangulo escalé");
        }

	}

}
