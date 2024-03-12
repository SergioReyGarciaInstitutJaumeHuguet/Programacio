package UF4.InstitutBasic;

public class Alumne {
	
	private String name, dni, email;
	private int edat;
	
	public void getAlumne() {
		System.out.println(this.name);
	}
	
	public void setAlumne(String name, String dni, String email, int edad) {
		this.name = name;
		this.dni = dni;
		this.email = email;
		this.edat = edad;
	}
	
	public String toString() {
		return "Nombre: " + this.name + 
				" Dni: " + dni +
				" Email: " + email + 
				" Edad: " + edat;
	}
	

}
