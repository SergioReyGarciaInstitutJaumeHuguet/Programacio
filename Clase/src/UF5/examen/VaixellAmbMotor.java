package UF5.examen;
public class VaixellAmbMotor extends Vaixell{

	protected int potenciaCV;
	
	public VaixellAmbMotor(String matricula, double eslora, int any, int potenciaCV) {
		super(matricula, eslora, any);
		this.potenciaCV = potenciaCV;
	}
	public double importAssociatAlVaixell() {
		return (preuBase() + this.potenciaCV);
	}
	
	public String toString() {
		return "Tipus: Vaixell amb motor";
	};

}
