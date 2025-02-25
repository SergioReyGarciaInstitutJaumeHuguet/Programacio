package UF5.examen;
public class IotLuxe extends VaixellAmbMotor{

	private int nCambrots;
	
	public IotLuxe(String matricula, double eslora, int any, int potenciaCV, int nCamrots) {
		super(matricula, eslora, any, potenciaCV);
		this.nCambrots = nCamrots;
	}

	public double importAssociatAlVaixell() {
		return (preuBase() + this.potenciaCV + this.nCambrots);
	}
	
	public String toString() {
		return "Tipus: Iot Luxe";
	};
}
