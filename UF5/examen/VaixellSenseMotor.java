package UF5.examen;
public class VaixellSenseMotor extends Vaixell{
	
	public VaixellSenseMotor(String matricula, double eslora, int any) {
		super(matricula, eslora, any);
	};

	public double importAssociatAlVaixell() {
		return preuBase();
	}
	
	public String toString() {
		return "Tipus: Vaixell sense motor";
	};
}
