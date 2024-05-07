
package UF5.banco;

public class Titular {
  private String dni;
  private String nombre;
  private String apellidos;
  private String direccion;
  private int telefono;

  public Titular(String dni, String nombre, String apellidos, String direccion, int telefono) {
    this.dni = dni;
    this.nombre = nombre;
    this.apellidos = apellidos;
    this.direccion = direccion;
    this.telefono = telefono;
  }


  public String getDni() {
    return dni;
  }

  public String getNombre() {
    return nombre;
  }
  
  public String getApellidos() {
    return apellidos;
  }
}
