package UF4.Hoteles;
import java.util.ArrayList;
public class Hotel {

	private String nom;
	private float estrelles;
	private ArrayList<Habitacio> habitacio = new ArrayList<Habitacio>();
	private ArrayList<Reserva> reserva = new ArrayList<Reserva>();
	
	public ArrayList<Reserva> getReserva() {
		return reserva;
	}

	public void setReserva(ArrayList<Reserva> reserva) {
		this.reserva = reserva;
	}

	public void crearHotel(String nom, float estrelles) {
		this.nom = nom;
		this.estrelles = estrelles;
	}
	
	public String toString() {
		return "El hotel " + this.nom + " con " + this.estrelles + " estrellas tiene " + this.habitacio.size() + " habitaciones.";
	}
	
	public String getNom() {
		return nom;
	}
	public void setNom(String nom) {
		this.nom = nom;
	}
	public float getEstrelles() {
		return estrelles;
	}
	public void setEstrelles(float estrelles) {
		this.estrelles = estrelles;
	}
	public ArrayList<Habitacio> getHabitacio() {
		return habitacio;
	}
	public void setHabitacio(ArrayList<Habitacio> habitacio) {
		this.habitacio = habitacio;
	}
	public void addRoom(Habitacio h) {
		habitacio.add(h);
	}
	public void addReserva(Reserva r) {
		reserva.add(r);
	}
	public void habitacionDisponible() {
		System.out.print("Las habitaciones disponibles son: ");
		for (int i = 0; i < habitacio.size(); i++) {
		      if(habitacio.get(i).isOcupat() == true) {
		    	  System.out.print(habitacio.get(i).getId() + " ");
		      }
		    }
	}
	
	
	
}
