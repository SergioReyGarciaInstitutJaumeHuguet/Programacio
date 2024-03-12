package UF4.InstitutBasic;

public class UsaInstitut {

	public static void main(String[] args) {
		Institut jh = new Institut();
		jh.setInstitut("Jaume Huguet", 1000);
		System.out.println(jh.getInstitut());
		Institut cdm = new Institut();
		cdm.setInstitut("Cor de Maria");
		System.out.println(cdm.getInstitut());
		Alumne srg = new Alumne();
		srg.setAlumne("Sergio Rey García", "12345678H", "correo@gmail.com", 18);
		srg.getAlumne();
		Alumne ilv = new Alumne();
		ilv.setAlumne("Ivan Lopez Martinez", "12345678H", "correo@gmail.com", 18);
		ilv.getAlumne();
		Alumne ilg = new Alumne();
		ilg.setAlumne("Isac Lopez García", "12345678H", "correo@gmail.com", 18);
		ilg.getAlumne();
		Alumne mafc = new Alumne();
		mafc.setAlumne("Miguel Angel Francisco Cordoba", "12345678H", "correo@gmail.com", 18);
		mafc.getAlumne();
		Alumne anc = new Alumne();
		anc.setAlumne("Antonio Neruda Calatayud", "12345678H", "correo@gmail.com", 18);
		anc.getAlumne();
		Alumne egd = new Alumne();
		egd.setAlumne("Elber Galarga Dura", "12345678H", "correo@gmail.com", 18);
		egd.getAlumne();
		jh.afegirAlumne(srg);
		jh.afegirAlumne(ilv);
		jh.afegirAlumne(ilg);
		cdm.afegirAlumne(mafc);
		cdm.afegirAlumne(anc);
		cdm.afegirAlumne(egd);
		jh.verAlumne();
		cdm.verAlumne();
		

	}

}
