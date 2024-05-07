
import banco.*;

public class PruebaBanco {
  
  public static void main (String args[]) {
  	Banco b1 = new Banco();
  	
	Titular pedro = new Titular("122","pedro","garcia","Calle pera",123456789);
	Titular pepe = new Titular("123","pepe","garcia","Calle manzana",987654321);
	Titular carlos = new Titular("124","carlos","garcia","Calle sandia",456123789);
	Titular alex = new Titular("125","alex","garcia","Calle dragon",567891234);

	Cuenta c1 = new CompteCorrent(pedro,500);
	Cuenta c2 = new CompteHabitatge(pepe,300);
	Cuenta c3 = new FonsInversio(carlos,1000);
	ComptePunts c4 = new ComptePunts(alex,1000);

	b1.anadirCuenta(c1);
	b1.anadirCuenta(c2);
	b1.anadirCuenta(c3);
	b1.anadirCuenta(c4);

	System.out.println("Saldo de CC: "+c1.getSaldo());
	System.out.println("Saldo de CV: "+c2.getSaldo());
	System.out.println("Saldo de FI: "+c3.getSaldo());
	System.out.println("Saldo de CP: "+c4.getSaldo()+" Punts: "+c4.getPuntos());
    
	System.out.println("Revisió mensual (CC): "+c1.revisionMensual());
	System.out.println("Revisió mensual (CV): "+c2.revisionMensual());
	System.out.println("Revisió mensual (FI): "+c3.revisionMensual());
	System.out.println("Revisió mensual (CP): "+c4.revisionMensual());
	
        try {
            c4.sacarDinero(15);
        } catch (NoHayDinero e) {
            System.out.println("No hay dinero suficiente, falta: "+e.getNegativo()+" €");
        }
        
        try {
            c3.sacarDinero(101000);
        } catch (NoHayDinero e) {
            System.out.println("No hay dinero suficiente, falta: "+e.getNegativo()+" €");
        }
        
        try {
            c3.sacarDinero(101000);
        } catch (NoHayDinero e) {
            System.out.println("No hay dinero suficiente, falta: "+e.getNegativo()+" €");
        }
        
    c4.ingresarDinero(15);

  }

}
