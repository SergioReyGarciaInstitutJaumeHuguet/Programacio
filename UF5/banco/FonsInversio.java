package UF5.banco;
public class FonsInversio implements Cuenta {
	private int saldo;
	private Titular propietario;
	
	public FonsInversio(Titular propietario, int saldo) {
		this.saldo = saldo;
		this.propietario = propietario;
	}
	
	public void ingresarDinero(int dinero) {
	    this.saldo = this.saldo + dinero;
	}
	
	public void sacarDinero(int n) throws NoHayDinero {
		if (saldo > -100000) {
			saldo = saldo - n;
		} else {
			NoHayDinero nhd = new NoHayDinero();
			nhd.setNegativo(n - saldo);
			throw nhd;
		}
	}
	
	public int getSaldo() {
	    return saldo;
	}
	
	public Titular getTitular() {
	  	return propietario;
	}
	
	public int revisionMensual() {
		int saldoMens;
		saldoMens = (int) (saldo + (saldo*0.34)-100);
		return saldoMens;
	}
	
}
