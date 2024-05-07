package UF5.NotesAlumnes;
import java.util.HashMap;
import java.util.Map;

public class main {
	private static HashMap<String, Float> alumnesNota = new HashMap<String, Float>();
	private static void veureAlumnes() {
	    for (Map.Entry<String, Float> entry : alumnesNota.entrySet()) {
	        String nombre = entry.getKey();
	        Float nota = entry.getValue();
	        System.out.println("Alumno: " + nombre + ", Nota: " + nota);
	    }
	}
	
	public static void main(String[] args) {
		Alumne a1 = new Alumne("Sergio",9);
		alumnesNota.put(a1.getNom(),a1.getNota());
		Alumne a2 = new Alumne("Pol",7);
		alumnesNota.put(a2.getNom(),a2.getNota());
		Alumne a3 = new Alumne("Ainhoa",6);
		alumnesNota.put(a3.getNom(),a3.getNota());
		Alumne a4 = new Alumne("Alejandro",5);
		alumnesNota.put(a4.getNom(),a4.getNota());
		Alumne a5 = new Alumne("Zaida",3);
		alumnesNota.put(a5.getNom(), a5.getNota());
		
		veureAlumnes();

	}

}
