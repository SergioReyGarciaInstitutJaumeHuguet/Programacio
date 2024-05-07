package UF5.Figures;

public class Quadrat implements Figura{

  private float costat;

    public Quadrat(float costat) {
        this.costat = costat;
    }

    public float area() {
        return costat * costat;
    }

    public float perimetre() {
        return 4 * costat;
    }
    
    @Override
	public String toString() {
		return "Quadrat\nArea: " + area() + " Perimetre: " + perimetre();
	}
}