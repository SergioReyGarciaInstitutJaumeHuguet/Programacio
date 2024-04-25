
package UF5.Banc;

/**
 * @author NT
 * Una cuenta tiene titular y saldo. Permite ingresar dinero, sacar dinero y ver saldo
 */
public class Cuenta
{
  private int saldo;
  private Titular propietario;

  /**
   * Constructor de Cuenta en el que se especifican tanto el saldo como el Titular
   */
  
  public Cuenta(Titular usuario, int saldo) {
    this.saldo  = saldo;
    this.propietario = usuario;
  }
/**
   * Constructor de Cuenta en el que se especifica el titular siendo el saldo cero por defecto
   */
  public Cuenta(Titular usuario) {
    this.saldo  = 0;
    this.propietario = usuario;
  }

  /**
   * Permite ingresar una cantidad de dinero en la cuenta incrementando el saldo
   */
  public void ingresarDinero(int dinero) {
    this.saldo = this.saldo + dinero;
  }

  /**
   * Permite sacar una cantidad de dinero de la cuenta.
   *@throws NoHaydinero si el saldo es inferior a la cantidad que se pretende sacar.
   *
   */
	public void sacarDinero(int n) throws NoHayDinero {
		if (saldo >= n) {
			saldo = saldo - n;
		} else {
			NoHayDinero nhd = new NoHayDinero();
			nhd.setNegativo(n - saldo);
			throw nhd;
		}
	}

 /**
  * Retorna el saldo actual
  */
  public int getSaldo() {
    return saldo;
  }

  /**
   * Retorna el titular de la cuenta
   */
  public Titular getTitular(){
  	return propietario;
  }	

}
