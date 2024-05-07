package UF5.examen;
public class Velers extends VaixellSenseMotor{

	private int pals;
	
	public Velers(String matricula, double eslora, int any, int pals) {
		super(matricula, eslora, any);
		this.pals = pals;
	}
	
	public double importAssociatAlVaixell() {
		return (preuBase() + this.pals);
	}
	
	public String toString() {
		return "Tipus: Velers";
	};
}
