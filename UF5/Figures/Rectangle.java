package UF5.Figures;

public class Rectangle implements Figura{
	private float longitud;
    private float amplada;

    public Rectangle(float longitud, float amplada) {
        this.longitud = longitud;
        this.amplada = amplada;
    }

    public float area() {
        return longitud * amplada;
    }

    public float perimetre() {
        return 2 * (longitud + amplada);
    }
    
    @Override
	public String toString() {
		return "Rectangle\nArea: " + area() + " Perimetre: " + perimetre();
	}
}