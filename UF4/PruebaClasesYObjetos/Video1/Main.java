package UF4.PruebaClasesYObjetos.Video1;

public class Main {

	public static void main(String[] args) {
		Vehiculo miVehiculo = new Vehiculo("Mercedes", 352);
		miVehiculo.conducir();
		miVehiculo.modelo = "BMW";
		miVehiculo.conducir();
		
		Vehiculo otroVehiculo = new Vehiculo();
		otroVehiculo.conducir();
	}
}
