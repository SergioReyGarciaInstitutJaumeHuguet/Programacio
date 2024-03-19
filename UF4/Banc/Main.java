package UF4.Banc;
public class Main {

	public static void main(String[] args) {
		Titular jgm = new Titular();
		jgm.Titular("44556677K","Juan", "Garcia Martinez");
		Titular plb = new Titular();
		plb.Titular("44556678L","Pedro", "Lorca Benitez");
		Titular atg = new Titular();
		atg.Titular("44556679J","Ana", "Torres Garriga");
		Compte jgmC = new Compte("435-0-2367800",jgm);
		Compte jgmC2 = new Compte(3000,"435-0-2367805",jgm);
		Compte plbC = new Compte(8200,"207-1-0004572",plb);
		Compte atgC = new Compte(100,"207-1-0004573",atg);
		Banc bbva = new Banc();
		bbva.setCompte(jgmC);
		bbva.setCompte(plbC);
		bbva.setCompte(atgC);
		bbva.setCompte(jgmC2);
		bbva.infoBanc();
		jgmC.setSaldoSumar(2000);
		atgC.setSaldoRestar(1000);
	}

}
