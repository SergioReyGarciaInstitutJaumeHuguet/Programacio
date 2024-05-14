package lol;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.table.*;
import java.sql.*;

@SuppressWarnings("serial")
public class Menu extends JFrame implements ActionListener {
    
    private JTable campionsTable;
    private JTable campioInfoTable;
    private DefaultTableModel campionsTableModel;
    private DefaultTableModel campioInfoTableModel;
    private JScrollPane campionsScrollPane;
    private JScrollPane campioInfoScrollPane;
    private String[] campionsColumnNames;
    private String[] campioInfoColumnNames;

    public Menu() {
        super("LoL");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container cp = getContentPane();
        cp.setLayout(new BorderLayout(5, 5));
        
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));
        JButton b0 = new JButton("Llistar Campions");
        JButton b1 = new JButton("Veure Campió");
        JButton b2 = new JButton("Afegir Campió");
        b0.addActionListener(this);
        b1.addActionListener(this);
        b2.addActionListener(this);
        buttonPanel.add(b0);
        buttonPanel.add(b1);
        buttonPanel.add(b2);
        cp.add(buttonPanel, BorderLayout.NORTH);
        
        campionsColumnNames = new String[] {"Id", "Name", "Title", "Tags"};
        campioInfoColumnNames = new String[] {"Name", "Title", "Tags", "Lore"};
        
        campionsTableModel = new DefaultTableModel(campionsColumnNames, 0);
        campionsTable = new JTable(campionsTableModel);
        campionsScrollPane = new JScrollPane(campionsTable);
        campionsScrollPane.setVisible(false);
        
        campioInfoTableModel = new DefaultTableModel(campioInfoColumnNames, 0);
        campioInfoTable = new JTable(campioInfoTableModel);
        campioInfoScrollPane = new JScrollPane(campioInfoTable);
        campioInfoScrollPane.setVisible(false);
        
        JPanel tablePanel = new JPanel(new GridLayout(2, 1, 10, 10));
        tablePanel.add(campionsScrollPane);
        tablePanel.add(campioInfoScrollPane);
        cp.add(tablePanel, BorderLayout.CENTER);
    }
    
    public void actionPerformed(ActionEvent e) {
        JButton boton = (JButton) e.getSource();
        switch(boton.getText()) {
            case "Llistar Campions":
                Connexio.connexio();
                ResultSet resultSet = Connexio.llistarCampions();
                plenaTaula(resultSet, campionsTableModel, campionsColumnNames);
                campionsScrollPane.setVisible(true);
                campioInfoScrollPane.setVisible(false);
                break;
            case "Veure Campió":
                Connexio.connexio();
                String nomCampio = Connexio.demanarNomOIdCampio();
                Object[] resultadoVeure = Connexio.veureInformacioCampio(nomCampio);
                if (resultadoVeure != null) {
                    String[] columnNames = (String[]) resultadoVeure[0];
                    ResultSet resultSetCampio = (ResultSet) resultadoVeure[1];
                    plenaTaula(resultSetCampio, campioInfoTableModel, columnNames);
                    campionsScrollPane.setVisible(false);
                    campioInfoScrollPane.setVisible(true);
                }
                break;
            case "Afegir Campió":
                Connexio.connexio();
                Connexio.afegirCampio();
                break;
        }
    }
    
    private void plenaTaula(ResultSet resultSet, DefaultTableModel tableModel, String[] columnNames) {
        try {
            tableModel.setColumnIdentifiers(columnNames);
            tableModel.setRowCount(0);
            while (resultSet.next()) {
                Object[] fila = new Object[columnNames.length];
                for (int i = 0; i < columnNames.length; i++) {
                    fila[i] = resultSet.getObject(columnNames[i]);
                }
                tableModel.addRow(fila);
            }
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
            System.out.println("Error al llenar la tabla");
        }
    }
}
