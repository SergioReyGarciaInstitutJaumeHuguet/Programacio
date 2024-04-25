package UF5.banco;

public class ComptePunts implements Cuenta {
	private int saldo;
	private Titular propietario;
	private int puntos;
	
	public ComptePunts(Titular propietario, int saldo) {
		this.saldo = saldo;
		this.propietario = propietario;
		this.puntos = 0;
	}
	
	public void ingresarDinero(int dinero) {
		this.puntos = dinero/6;
	    this.saldo = this.saldo + dinero;
	    System.out.println("Punts: "+puntos);
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
	
	public int getPuntos() {
		return puntos;
	}

	public int revisionMensual() {
		int saldoMens;
		saldoMens = (int) (saldo + (saldo*0.6)-100);
		return saldoMens;
	}
}
