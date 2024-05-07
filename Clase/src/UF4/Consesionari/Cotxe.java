package UF4.Consesionari;

public class Cotxe {

	private String matricula, marca, model;
	
	public Cotxe(String matricula) {
		this.matricula = matricula;
	}
	
	public void setMarca(String nomMarca){
		this.marca = nomMarca;
	}
	
	public void setModel(String nomModel){
		this.model = nomModel;
	}
	
	public String getMatricula() {
		return this.matricula;
	}
	public String getMarca() {
		return this.marca;
	}
	public String getModel() {
		return this.model;
	}
	
	
	public String toString() {
		return	"Marca: " + marca +
				" Model: " + model +
				" Matricula: " + matricula; 
	}
}
