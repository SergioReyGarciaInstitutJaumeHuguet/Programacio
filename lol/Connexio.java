package lol;
import java.sql.*;
import javax.swing.*;

public class Connexio {
    
    private static Connection connexio;
    public final static String USER = "root";
    public final static String PASSW = "2012";
    public final static String DB = "pelicules";
    
    public static void connexio() {
        try {
            connexio = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/" + DB + "?serverTimezone=Europe/Madrid", USER, PASSW);
            System.out.println("Server connectat");
        } catch(SQLException e) {
            System.out.println("No s'ha pogut connectar a la meva base de dades");
            e.printStackTrace();
        }
    }
    
    public static ResultSet llistarCampions() {
        try {
            String Querydb = "USE "+DB+";";
            Statement stdb = connexio.createStatement();
            stdb.executeUpdate(Querydb);
            
            String Query = "SELECT * FROM champions";
            Statement st = connexio.createStatement();
            java.sql.ResultSet resultSet;
            resultSet = st.executeQuery(Query);
            
            return resultSet;
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
            System.out.println("Error en el retorn de dades");
            return null;
        }
    }

    public static String demanarNomOIdCampio() {
        String nomCampio = JOptionPane.showInputDialog("Introdueix el nom o id del campió: ");
        return nomCampio;
    }

    public static Object[] veureInformacioCampio(String nomCampio) {
        try {
            String Querydb = "USE " + DB + ";";
            Statement stdb = connexio.createStatement();
            stdb.executeUpdate(Querydb);

            String Query = "SELECT name, title, tags, lore FROM champions WHERE name LIKE ? OR id = ?";
            PreparedStatement st = connexio.prepareStatement(Query);
            st.setString(1, "%" + nomCampio + "%");
            st.setString(2, nomCampio);
            ResultSet resultSet = st.executeQuery();

            String[] columnNames = {"Name", "Title", "Tags", "Lore"};
            return new Object[] {columnNames, resultSet};
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
            System.out.println("Error en la adquisicio de dades");
            return null;
        }
    }
    
    public static void afegirCampio() {
        String name = JOptionPane.showInputDialog("Introdueix el nom del campió:");
        String title = JOptionPane.showInputDialog("Introdueix el títol del campió:");
        String tags = JOptionPane.showInputDialog("Introdueix les etiquetes del campió:");
        String lore = JOptionPane.showInputDialog("Introdueix la història del campió:");

        if (name != null && title != null && tags != null && lore != null) {
            guardarCampio(name, title, lore, tags);
        } else {
            System.out.println("Entrada no vàlida.");
        }
    }

    private static void guardarCampio(String name, String title, String lore, String tags) {
        try {
            String queryCheck = "SELECT COUNT(*) FROM champions WHERE name = ?";
            PreparedStatement pstCheck = connexio.prepareStatement(queryCheck);
            pstCheck.setString(1, name);
            ResultSet rs = pstCheck.executeQuery();
            rs.next();
            if (rs.getInt(1) > 0) {
                JOptionPane.showMessageDialog(null, "El campió ja existeix.");
                return;
            }

            String queryLastId = "SELECT MAX(id) FROM champions";
            Statement stLastId = connexio.createStatement();
            ResultSet rsLastId = stLastId.executeQuery(queryLastId);
            int newId = 1;
            if (rsLastId.next()) {
                newId = rsLastId.getInt(1) + 1;
            }

            String queryInsert = "INSERT INTO champions(id, name, title, lore, tags) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement pstInsert = connexio.prepareStatement(queryInsert);
            pstInsert.setInt(1, newId);
            pstInsert.setString(2, name);
            pstInsert.setString(3, title);
            pstInsert.setString(4, lore);
            pstInsert.setString(5, tags);
            pstInsert.executeUpdate();

            System.out.println("Dades emmagatzemades correctament");
            JOptionPane.showMessageDialog(null, "Campió afegit correctament");
        } catch (SQLException ex) {
            System.out.println("Error en l'emmagatzematge: " + ex.getMessage());
            JOptionPane.showMessageDialog(null, "Error en l'emmagatzematge: " + ex.getMessage());
        }
    }
}
