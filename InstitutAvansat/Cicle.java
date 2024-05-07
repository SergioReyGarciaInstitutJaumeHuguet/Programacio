package InstitutAvansat;

import java.util.ArrayList;

public class Cicle {
	private CicleCat cicle;
	private String nomCicle;
	ArrayList<Modul> moduls = new ArrayList<>();
	ArrayList<String> sortModuls = new ArrayList<>();
	private Modul m1 = new Modul(ModulCat.M1);
    private Modul m2 = new Modul(ModulCat.M2);
    private Modul m3 = new Modul(ModulCat.M3);
    private Modul m6 = new Modul(ModulCat.M6);
    private Modul m7 = new Modul(ModulCat.M7);
	public Cicle(CicleCat c) {
		this.cicle = c;
		moduls.add(m1);
		sortModuls.add("M1");
	    moduls.add(m2);
	    sortModuls.add("M2");
	    moduls.add(m3);
	    sortModuls.add("M3");
	    if (c == CicleCat.ASIX) {
	        this.nomCicle = "Administració de Sistemes Microinformàtics i Xarxes";
	        moduls.add(m6);
	        sortModuls.add("M6");
	    } else if (c == CicleCat.DAM) {
	    	this.nomCicle = "Desenvolupament d'aplicacions multiplataforma";
	    	moduls.add(m7);
	    	sortModuls.add("M7");
	    } else {
	    	System.out.println("ERROR CICLE");
	    }
	}
	
	public String toString() {
	    String modulsInfo = "";
	    int a = -1;
	    if (this.cicle == CicleCat.ASIX) {
	    	for(String i : sortModuls) {
	    		a += 1;
		        modulsInfo = modulsInfo + i + ": " + moduls.get(a) + "\n";
	    	}
	    } else if (this.cicle == CicleCat.DAM) {
	    	for(String i : sortModuls) {
	    		a += 1;
		        modulsInfo = modulsInfo + i + ": " + moduls.get(a) + "\n";
	    	}
	    } else {
	        modulsInfo = "ERROR CICLE";
	    }
	    
	    return "El cicle " + this.cicle + " " + this.nomCicle + " te els moduls " + "\n" + modulsInfo;
	}

}
