package UF5.examen;
public abstract class Vaixell {
	
	protected String matricula;
	protected double eslora;
	protected int any;
	
	public Vaixell(String matricula, double eslora, int any) {
		this.matricula = matricula;
		this.eslora = eslora;
		this.any = any;
	};
	public abstract double importAssociatAlVaixell();
	public double preuBase() {
		double preuBase = this.eslora * 10;
		return preuBase;
	}

}
