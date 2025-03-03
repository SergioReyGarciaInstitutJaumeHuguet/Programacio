package UF5.examen;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Lloguer {
	private String dni, dataIni, dataFi;
	private static double valor_Fix = 2;
	private Vaixell vaixell;
	
	public Lloguer(String dni, String dataIni, String dataFi) {
		this.dni = dni;
		this.dataIni = dataIni;
		this.dataFi = dataFi;
	}
	
	public void setVaixell(Vaixell vaixell) {
		this.vaixell = vaixell;
	}
	
	public long dies() {
		DateTimeFormatter form = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		LocalDate data1 = LocalDate.parse(this.dataIni,form);
		LocalDate data2 = LocalDate.parse(this.dataFi,form);
		long dies = ChronoUnit.DAYS.between(data1, data2);
		if (dies == 0) {return 1;}
		else{return dies;}
	}
	
	public double importTotal() {
		double preuBase = this.vaixell.preuBase();
		double preuTotal = (preuBase * dies() * this.valor_Fix);
		return preuTotal;
	}
	
	public double importPerDia() {
		double importDia = importTotal()/dies();
		return importDia;
	}

	public String getDataFi() {
		return dataFi;
	}

	@Override
	public String toString() {
		return "DNI:" + dni + "\nData d'inici: " + dataIni + "\nData final: " + dataFi + "\n" + vaixell + "\n";
	}

}
