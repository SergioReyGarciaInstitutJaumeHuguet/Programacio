package UF5.EmpresaTel;

public class Connection{
	private String iniDateTime, endDateTime;

	public Connection(String iniDateTime, String endDateTime) {
		super();
		this.iniDateTime = iniDateTime;
		this.endDateTime = endDateTime;
	}
	
	public long nMinutes() {
		return 5;
	}

}
