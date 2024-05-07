package InstitutAvansat;

public class Modul {
	
	private String m;
	public Modul(ModulCat m) {
		 switch (m) {
            case M1:
            	this.m = "Sistemes Informàtics";
            	break;
            case M2:
            	this.m = "Base de dades";
            	break;
            case M3:
            	this.m = "Programació";
            	break;
            case M6:
            	this.m = "Accés a dades";
            	break;
            case M7:
            	this.m = "Planificació i administració de xarxes";
            	break;
            default:
            	this.m = "ERROR MODUL";
            	break;
        }
	}
	
	public String toString() {
        return this.m;
    }
	
}
