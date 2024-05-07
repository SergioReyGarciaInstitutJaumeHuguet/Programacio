
package UF5.banco;

import java.util.ArrayList;

/**
 * @author NT
 */
public class Banco {
  private ArrayList<Cuenta> cuentas;
  private int numCuenta;
  private final int MAX_CUENTAS = 10;

  public Banco() {
    this.cuentas = new ArrayList<Cuenta>();
    this.numCuenta = 0;
  }  

  public void anadirCuenta(Cuenta nuevaCuenta) {
	if (numCuenta < MAX_CUENTAS){
		cuentas.add(nuevaCuenta);
		numCuenta++;
	}   
  }

  public Cuenta buscarCuenta(Titular propietario) {
  	for (Cuenta cuenta:cuentas) {
		if (cuenta.getTitular().equals(propietario))
			return cuenta;
	}
	return null;
  } 

  public Cuenta buscarCuentaDNI(String dni) {
  	for (Cuenta cuenta:cuentas) {
		if (cuenta.getTitular().getDni().equals(dni))
			return cuenta;
	}
	return null;
  } 

}
