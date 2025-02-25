package UF5.examen;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
public class Port {
	private String ciutat;
	private ArrayList <Lloguer> lloguers;
	
	public Port(String ciutat) {
		this.ciutat = ciutat;
		this.lloguers = new ArrayList<Lloguer>();
	}
	
	public boolean afegirLloguer(Lloguer r) {
		lloguers.add(r);
		return true;
	}
	
	public double calcularImportMes(int mes, int any) {
		DateTimeFormatter form = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		int importMes = 0;
		for (Lloguer lloguer:lloguers) {
			String dataFi = lloguer.getDataFi();
			LocalDate data = LocalDate.parse(dataFi,form);
			int month = data.getMonthValue();
			int year = data.getYear();
			if((month != mes) && (year != any)) {
				importMes += lloguer.importTotal();
			}
		}
		return importMes;
	}
	
	public double calcularImportTotal() {
		int importTotal = 0;
		for (Lloguer lloguer:lloguers) {
			importTotal += lloguer.importTotal();
		}
		return importTotal;
	}
	
	public void informe() {
		System.out.println("Port: " + this.ciutat + "\n");
		for (Lloguer lloguer:lloguers) {
			System.out.println(lloguer);
		}
	}

}
