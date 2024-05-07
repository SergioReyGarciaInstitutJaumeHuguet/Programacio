package DatabasePelicules;
import java.sql.*;

public class ConexioDataBase {
	private static Connection connexio;
	public final static String USER = "root";
	public final static String PASSW = "2012";
	
	public static void getValues(String db, String table_name) {
	    try {
	        String Querydb = "USE "+db+";";
	        Statement stdb = connexio.createStatement();
	        stdb.executeUpdate(Querydb);
	        
	        String Query = "SELECT * FROM " + table_name;
	        Statement st = connexio.createStatement();
	        java.sql.ResultSet resultSet;
	        resultSet = st.executeQuery(Query);
	        
	        while(resultSet.next()) {
	            System.out.println("ID: "+resultSet.getString("id_peli") + " "
	            + "Nom: "+resultSet.getString("nom") + " "
	            + "Director: "+resultSet.getString("director") + " "
	            + "Any producit: "+resultSet.getString("any_prod") + " "
	            + "Llogada: "+resultSet.getString("llogada") + " "
	            );
	        }
	    } catch(SQLException ex) {
	        System.out.println(ex.getMessage());
	        System.out.println("error en la adquisicion de datos");
	    }
	}
	
	public static void main(String[] args) {
	try {
	connexio = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/pelicules?serverTimezone=Europe/Madrid", USER, PASSW);
	System.out.println("Server Connectat");
	}catch(SQLException e) {

	e.printStackTrace();
	}
	getValues("pelicules","pelicules");
	}

}
