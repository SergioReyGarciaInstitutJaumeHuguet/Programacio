package UF5.EmpresaTel;

public class UserOffer1 extends UserWithOffer{

	public UserOffer1(String name, String dni, double priceMinute) {
		super(name,dni,priceMinute);
	}
	
	public double billAmount() {
		return 5;
	}
}
