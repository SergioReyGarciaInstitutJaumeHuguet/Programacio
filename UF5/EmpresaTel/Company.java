package UF5.EmpresaTel;
import java.util.HashSet;

public class Company {
	private HashSet<User> users = new HashSet<User>();

	public Company(HashSet<User> users) {
		super();
		this.users = users;
	}
	
	public boolean add(User u) {
		users.add(u);
		return true;
	}
	
	public void listUsers() {
		for (User usuari : users) {
            System.out.println(usuari);
        }
	}

}
