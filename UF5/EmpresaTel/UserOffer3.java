package UF5.EmpresaTel;

public class UserOffer3 extends UserWithOffer{
	public UserOffer3(String name, String dni, double priceMinute) {
		super(name,dni,priceMinute);
	}
	
	public double billAmount() {
		return 5;
	}

}
