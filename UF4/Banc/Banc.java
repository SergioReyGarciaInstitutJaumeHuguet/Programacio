package UF4.Banc;

public class Banc {
	private Compte[] compte = new Compte[100];
	private int i = 0;

	public void getCompte() {
		for(Compte i: compte) {
			if(i != null) {
				System.out.println(i.getTitularDni());
			}
		}
	}

	public void setCompte(Compte compteBanc) {
		this.compte[i] = compteBanc;
		i++;
	}
	
	public void infoBanc() {
		for(Compte i: compte) {
			if(i != null) {
				System.out.println(i);
			}
		}
	}
	
	
}
