package UF4.Hoteles;

public class Reserva {

	private int nit;
	private int preu;
	private int idFactura;
	private int habitacioID;
	private String dniClient;
	private boolean pagado;
	private boolean uso = true;

	public Reserva(int i) {
		this.idFactura = i;
	}
	
	public void crearReserva(Client cl, Habitacio hb, int nit, boolean pagado) {
		this.habitacioID = hb.getId();
		this.nit = nit;
		this.preu = this.nit * hb.getCatInt();
		hb.setOcupat(true);
		this.dniClient = cl.getDni();
		this.pagado = pagado;
	}
	
	public void cancelarReserva(Habitacio hb) {
		hb.setOcupat(false);
		this.uso = false;
	}
	
	public String toString() {
		if(this.uso == false) {
			return "Esta factura del cliente " + this.dniClient + " alojado en la habitación" + this.habitacioID + " ya no está activa";
		}else {return "Esta factura del cliente " + this.dniClient + " alojado en la habitación" + this.habitacioID + " con un precio de " + this.preu + " está activa";}
	}
	
	public int getNit() {
		return nit;
	}

	public void setNit(int nit) {
		this.nit = nit;
	}

	public int getPreu() {
		return preu;
	}

	public void setPreu(int preu) {
		this.preu = preu;
	}

	public int getIdFactura() {
		return idFactura;
	}

	public void setIdFactura(int idFactura) {
		this.idFactura = idFactura;
	}

	public int getHabitacioID() {
		return habitacioID;
	}

	public void setHabitacioID(int habitacioID) {
		this.habitacioID = habitacioID;
	}

	public String getDniClient() {
		return dniClient;
	}

	public void setDniClient(String dniClient) {
		this.dniClient = dniClient;
	}
	
	
	
	
}
