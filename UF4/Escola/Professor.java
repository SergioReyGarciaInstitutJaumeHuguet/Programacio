package UF4.Escola;
import java.util.HashSet;

public class Professor extends Persona{

	protected HashSet<String> assignatures = new HashSet<String>();
	
	public HashSet<String> getAssignatures() {
		return assignatures;
	}

	public void setAssignatures(HashSet<String> assignatures) {
		this.assignatures = assignatures;
	}

	public Professor(String nom, String adreca, HashSet<String> assignatures) {
		super(nom, adreca);
		this.assignatures = assignatures;
	}

	@Override
	public String toString() {
		return nom + " es un profesor que viu en " + adreca + " i cursa aquestes asignatures: " + assignatures;
	}
	
	
}
