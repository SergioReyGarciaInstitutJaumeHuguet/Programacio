package UF4.Escola;
import java.util.HashSet;
public class main {

	public static void main(String[] args){
		Estudiant e1 = new Estudiant("Sergio", "Carrer Segarra", "DAM", 1);
		HashSet<String> assignatures1 = new HashSet<>();
        assignatures1.add("M1");
        assignatures1.add("M4");
        assignatures1.add("M8");
		Professor p1 = new Professor("Alex", "Carrer Avenir", assignatures1);
		EstudiantInternacional ei1 = new EstudiantInternacional("Adolf", "Carrer Edimburg", "DAW", 2, "Alemania");
		System.out.println(e1);
		System.out.println(p1);
		System.out.println(ei1);

	}

}
