package UF4.InstitutBasic;

public class Main {

	public static void main(String[] args) {
		Institut jh = new Institut();
		jh.setInstitut("Jaume Huguet", 1000);
		System.out.println(jh.getInstitut());
		Institut cdm = new Institut();
		cdm.setInstitut("Cor de Maria");
		System.out.println(cdm.getInstitut());
		Alumnes srg = new Alumnes();
		srg.setAlumne("Sergio Rey García", "12345678H", "correo@gmail.com", 18);
		srg.getAlumne();
		Alumnes ilv = new Alumnes();
		ilv.setAlumne("Ivan Lopez Martinez", "12345678H", "correo@gmail.com", 18);
		ilv.getAlumne();
		Alumnes ilg = new Alumnes();
		ilg.setAlumne("Isac Lopez García", "12345678H", "correo@gmail.com", 18);
		ilg.getAlumne();
		Alumnes mafc = new Alumnes();
		mafc.setAlumne("Miguel Angel Francisco Cordoba", "12345678H", "correo@gmail.com", 18);
		mafc.getAlumne();
		Alumnes anc = new Alumnes();
		anc.setAlumne("Antonio Neruda Calatayud", "12345678H", "correo@gmail.com", 18);
		anc.getAlumne();
		Alumnes egd = new Alumnes();
		egd.setAlumne("Elber Galarga Dura", "12345678H", "correo@gmail.com", 18);
		egd.getAlumne();
		jh.afegirAlumne();
		

	}

}
