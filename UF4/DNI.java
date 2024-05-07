package UF4;

public class DNI {

	public static void main(String[] args) {
		final int DNI = 77791827;
		switch(DNI%23) {
		case 0: System.out.println(DNI + "T");
		case 1: System.out.println(DNI + "S");
		case 2: System.out.println(DNI + "H");
		default: System.out.println(DNI + "K");
		}

	}

}
