package UF5.EmpresaTel;

public class UserOffer2 extends UserWithOffer{
	public UserOffer2(String name, String dni, double priceMinute, double discount) {
		super(name,dni,priceMinute);
	}
	
	public double billAmount() {
		return 5;
	}
	
}
