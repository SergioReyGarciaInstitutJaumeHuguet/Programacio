
package UF5.banco;

public class NoHayDinero extends Exception {
	private int negativo;

	public int getNegativo() {
		return negativo;
	}

	public void setNegativo(int negativo) {
		this.negativo = negativo;
	}

}
