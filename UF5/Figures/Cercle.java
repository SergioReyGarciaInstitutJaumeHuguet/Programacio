package UF5.Figures;

public class Cercle implements Figura{
 private float radi;

    public Cercle(float radi) {
        this.radi = radi;
    }

    public float area() {
        return (float) (Math.PI * radi * radi);
    }

    public float perimetre() {
        return (float) (2 * Math.PI * radi);
    }

	@Override
	public String toString() {
		return "Cercle\nArea: " + area() + " Perimetre: " + perimetre();
	}
}