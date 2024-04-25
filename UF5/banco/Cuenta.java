
package UF5.banco;

public interface Cuenta {

	public void ingresarDinero(int dinero);

	public void sacarDinero(int n) throws NoHayDinero;

	public int getSaldo();

	public Titular getTitular();
	
	public int revisionMensual();
}
