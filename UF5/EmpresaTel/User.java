package UF5.EmpresaTel;
import java.util.HashSet;

public abstract class User{
	private String dni, name;
	protected double priceminute;
	protected HashSet<Connection> connections = new HashSet<Connection>();
	public User(String dni, String name, double priceminute) {
		super();
		this.dni = dni;
		this.name = name;
		this.priceminute = priceminute;
	}
	
	public boolean add(Connection c) {
		connections.add(c);
		return true;
	}
	
	public double totalMinutes() {
		return 5;
	}
	
	
}
