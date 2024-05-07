package UF4.Consesionari;

public class Concessionari {

	private Cotxe[] llistaCotxes = new Cotxe[100];
	private String a, b = " ", c = "";
	private int num = 0;
	
	public void nouCotxe(Cotxe a) {
		this.llistaCotxes[num] = a;
		this.num++;
	}
	
	
	public String toString() {
		for (int i = 0; i < llistaCotxes.length; i++) {
            if (llistaCotxes[i] != null) {
                this.a = "Marca: " + llistaCotxes[i].getMarca() +
        				" Model: " + llistaCotxes[i].getModel() +
        				" Matricula: " + llistaCotxes[i].getMatricula() + 
        				" "; 
                b = c;
                c = a + b;
            }
        }
		return c;
	}
	
	public Cotxe buscaCotxe(String matricula) {
        for (int i = 0; i < llistaCotxes.length; i++) {
            if (llistaCotxes[i] != null && llistaCotxes[i].getMatricula().equals(matricula)) {
                return llistaCotxes[i];
            }
        }
        return null;
    }
	
}
