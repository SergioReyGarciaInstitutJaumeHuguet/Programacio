package UF4.InstitutBasic;

public class UsaInstitut {

	public static void main(String[] args) {
		// Creo y muestro los institutos
		Institut jh = new Institut();
		jh.setInstitut("Jaume Huguet", 1000);
		System.out.println(jh.getInstitut());
		Institut cdm = new Institut();
		cdm.setInstitut("Cor de Maria");
		System.out.println(cdm.getInstitut());
		
		// Creo los alumnos
		Alumne srg = new Alumne();
		srg.setAlumne("Sergio Rey García", "12345678H", "correo@gmail.com", 18);
		Alumne ilv = new Alumne();
		ilv.setAlumne("Ivan Lopez Martinez", "12345678H", "correo@gmail.com", 18);
		Alumne ilg = new Alumne();
		ilg.setAlumne("Isac Lopez García", "12345678H", "correo@gmail.com", 18);
		Alumne mafc = new Alumne();
		mafc.setAlumne("Miguel Angel Francisco Cordoba", "12345678H", "correo@gmail.com", 18);
		Alumne anc = new Alumne();
		anc.setAlumne("Antonio Neruda Calatayud", "12345678H", "correo@gmail.com", 18);
		Alumne egd = new Alumne();
		egd.setAlumne("Elber Galarga Dura", "12345678H", "correo@gmail.com", 18);
		
		// Añado a los alumnos a la lista y los muestro
		jh.afegirAlumne(srg);
		jh.afegirAlumne(ilv);
		jh.afegirAlumne(ilg);
		cdm.afegirAlumne(mafc);
		cdm.afegirAlumne(anc);
		cdm.afegirAlumne(egd);
		jh.verAlumne();
		cdm.verAlumne();
		
		// Vuelvo a mostrar los institutos
		System.out.println(jh.getInstitut());
		System.out.println(cdm.getInstitut());

	}

}
