package UF4.Hoteles;

public class Habitacio {

	private int id = 0, llits;
	private Categoria cat;
	private boolean ocupat = false;
	
	public Habitacio(int i) {
		this.id = i;
	}

	public void crearHabitacio(int llits, Categoria cat) {
		this.llits = llits;
		this.cat = cat;
	}
	
	public String toString(){
		if(this.ocupat == true) {
			return "La habitación " + this.id + " está ocupada. Tiene " + this.llits + " camas y es de categoría " + this.cat;
		} else {return "La habitación " + this.id + " no está ocupada. Tiene " + this.llits + " camas y es de categoría " + this.cat;}
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getLlits() {
		return llits;
	}
	public void setLlits(int llits) {
		this.llits = llits;
	}
	public Categoria getCat() {
		return cat;
	}
	public int getCatInt() {
		if(this.cat == Categoria.NORMAL) {
			return 60;
		}else if(this.cat == Categoria.LUXE) {
			return 100; 
		}else {return 200;}
	}
	public void setCat(Categoria cat) {
		this.cat = cat;
	}
	public boolean isOcupat() {
		return ocupat;
	}
	public void setOcupat(boolean ocupat) {
		this.ocupat = ocupat;
	}
	
	
}
