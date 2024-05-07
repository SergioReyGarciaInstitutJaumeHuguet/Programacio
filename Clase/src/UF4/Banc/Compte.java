package UF4.Banc;

public class Compte {
	
	private float saldo;
	private String compte;
	private Titular titular;
	
	public Compte(String compte, Titular titular) {
		this.saldo = 0;
		this.compte = compte;
		this.titular = titular;
	}
	
	public Compte(float saldo, String compte, Titular titular) {
		this.saldo = saldo;
		this.compte = compte;
		this.titular = titular;
	}
	
	
	public String getTitularDni() {
		return this.titular.getDni();
	}



	public void setTitular(Titular titular) {
		this.titular = titular;
	}

	
	public String getCompte() {
		return this.compte;
	}
	
	public void setSaldoSumar(int diners) {
		this.saldo += diners;
		System.out.println("Dinero ingresado");
	}
	
	public void setSaldoRestar(int diners) {
		try {
			float a = this.saldo;
			a -= diners;
			if (a < 0) {
				throw new ArithmeticException();
			} else {
			System.out.println("Dinero sacado");}
			
		} catch (Exception e) {
			System.out.println("No tienes suficiente dinero");
		}
	}
	
	public float getValorSaldo() {
		return saldo;
	}
	
	public String getValorCompte() {
		return compte;
	}
	
	public String toString() {
		return titular.toString() + "Numero de compte: " + this.compte + "\n" + "Saldo: " + this.saldo + "\n";
	}
}
