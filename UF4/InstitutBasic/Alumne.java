package UF4.InstitutBasic;

public class Alumne {
	
	// Creo los objetos de la clase Alumne
	private String name, dni, email;
	private int edat;
	
	// Muestro el nombre del alumno
	public void getAlumne() {
		System.out.println("Nombre: " + this.name);
	}
	
	// Creo al alumno
	public void setAlumne(String name, String dni, String email, int edad) {
		this.name = name;
		this.dni = dni;
		this.email = email;
		this.edat = edad;
	}
	
	// Paso a String el punto de memoria del alumno para mostrarlo
	public String toString() {
		return "Nombre: " + this.name + 
				" Dni: " + dni +
				" Email: " + email + 
				" Edad: " + edat;
	}
	

}
