package UF5.ConversorDeMonedas;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Main extends JFrame {    
	private JTextField quantitat;
	private JTextField resultat;
	//Accion si pulsa de Euro a Dolar
	class Resultado1 implements ActionListener  {       
		public void actionPerformed(ActionEvent e) {  
			float cantEuros = Float.parseFloat(quantitat.getText());
			float cantDolares = cantEuros * 1.12f;
			resultat.setText(String.valueOf(cantDolares + "$"));;        
		}    
	}
	//Accion si pulsa de Euro a Libra
	class Resultado2 implements ActionListener  {       
		public void actionPerformed(ActionEvent e) {  
			float cantEuros = Float.parseFloat(quantitat.getText());
			float cantLibras = cantEuros * 0.86f;
			resultat.setText(String.valueOf(cantLibras + "£"));;        
		}    
	}
	//Accion si pulsa de Dolar a Euro
	class Resultado3 implements ActionListener  {       
		public void actionPerformed(ActionEvent e) {  
			float cantDolares = Float.parseFloat(quantitat.getText());
			float cantEuros = cantDolares / 1.12f;
			resultat.setText(String.valueOf(cantEuros + "€"));;        
		}    
	}
	//Accion si pulsa de Libras a Euro
	class Resultado4 implements ActionListener  {       
		public void actionPerformed(ActionEvent e) {  
			float cantLibras = Float.parseFloat(quantitat.getText());
			float cantEuros = cantLibras / 0.86f;
			resultat.setText(String.valueOf(cantEuros + "€"));;        
		}    
	}
	
	public Main() {        
		// Propiedades de la ventana
		super("Titulo de ventana");        
		setSize(400, 150);        
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// propiedades del panel
		JPanel panelDatos = new JPanel();        
		GridLayout gl = new GridLayout(2,2,2,4);  
		panelDatos.setLayout(gl);     
		panelDatos.add(new JLabel("Quantitat:"));   
		quantitat = new JTextField(10);  
		panelDatos.add(quantitat);  
		panelDatos.add(new JLabel("Resultat:"));  
		resultat = new JTextField(10); 
		resultat.setEditable(false);
		panelDatos.add(resultat);
		// Accion de los botones
		JPanel panelBotones = new JPanel();      
		panelBotones.setLayout(new FlowLayout()); 
		JButton bot1 = new JButton("€->$");
		panelBotones.add(bot1);      
		JButton bot2 = new JButton("€->£");
		panelBotones.add(bot2);  
		JButton bot3 = new JButton("$->€");
		panelBotones.add(bot3);  
		JButton bot4 = new JButton("£->€");
		panelBotones.add(bot4);  
		// Lo meto al contenedor
		Container cp = getContentPane();     
		cp.add(panelDatos, BorderLayout.CENTER);     
		cp.add(panelBotones, BorderLayout.SOUTH);
		
		bot1.addActionListener(new Resultado1());
		bot2.addActionListener(new Resultado2());
		bot3.addActionListener(new Resultado3());
		bot4.addActionListener(new Resultado4());
	} 
	

}