package UF5.banco;

public class CompteHabitatge implements Cuenta {
	private int saldo;
	private Titular propietario;
	
	public CompteHabitatge(Titular propietario, int saldo) {
		this.saldo = saldo;
		this.propietario = propietario;
	}
	
	public void ingresarDinero(int dinero) {
	    this.saldo = this.saldo + dinero;
	}
	
	public void sacarDinero(int n) throws NoHayDinero {
		System.out.println("ERROR: No es poden treure diners en CompteHabitatge.");
	}
	
	public int getSaldo() {
	    return saldo;
	}
	
	public Titular getTitular() {
	  	return propietario;
	}
	
	public int revisionMensual() {
		int saldoMens;
		saldoMens = (int) (saldo + (saldo*0.2));
		return saldoMens;
	}
	
	
}
