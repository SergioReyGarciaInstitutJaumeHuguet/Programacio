package UF4.PruebaClasesYObjetos.Video1;

public class Vehiculo {
	public int peso;
	public String modelo;
	
	public Vehiculo() {
	
	}
	public Vehiculo(String modelo, int peso) {
		this.modelo = modelo;
		this.peso = peso;

	}

	public void conducir() {
		System.out.println("Estoy conduciendo un " + modelo + " que pesa " + peso + "Kg");
	}

}
