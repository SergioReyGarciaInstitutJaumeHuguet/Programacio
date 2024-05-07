package UF4.Escola;
public class main {

	public static void main(String[] args){
		Estudiant e1 = new Estudiant("Sergio", "Carrer Segarra", "DAM", 1);
		Professor p1 = new Professor("Alex", "Carrer Avenir");
		p1.afegirAssignatura("M1");
		p1.afegirAssignatura("M2");
		p1.afegirAssignatura("M6");
		EstudiantInternacional ei1 = new EstudiantInternacional("Adolf", "Carrer Edimburg", "DAW", 2, "Alemania");
		System.out.println(e1);
		System.out.println(p1);
		System.out.println(ei1);
		p1.treureAssignatura("M1");
		System.out.println(p1);

	}

}
