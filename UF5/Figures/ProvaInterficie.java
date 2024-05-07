package UF5.Figures;

import java.util.ArrayList;

public class ProvaInterficie {

	public static void main(String[] args) {
		
		ArrayList<Figura> fig = new ArrayList<>();
		
		Figura quad = new Quadrat(3.5f);
		Figura circ = new Cercle (3.5f); 
		Figura rect = new Rectangle (2.25f, 2.55f); 
		
		fig.add(rect);
		fig.add(circ);
		fig.add(quad);
		
		for (Figura f : fig) {
			System.out.println(f);
		}
	}
}
