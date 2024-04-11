package UF4.Informatica;

public class CPU extends Articles{

	private float mhz, preuTotal;

	public CPU(String codi, String descripcio, int unitats, float preuBase, float mhz) {
		super(codi, descripcio, unitats, preuBase);
		this.mhz = mhz;
		this.preuTotal = preuBase * mhz;
	}
	
	public float preuTotal() {
		return preuTotal;
	}

	@Override
	public String toString() {
		return codi + "	" + descripcio + "	" + unitats + "	" + mhz + " " + "MHz" + "	" + preuTotal;
	}
	
	
	
	
}
