package UF4.Aquari;
import java.util.ArrayList;
public class AquariTest {

	public static void main(String[] args) {
		ArrayList<Organisme> organismes = new ArrayList<Organisme>();
		Peix peix1 = new Peix("peix","peixos",'A',12,14,6,7,"Mediterrani",'A',34);
		organismes.add(peix1);
		Peix peix2 = new Peix("peix","peixos",'B',11,13,4,6,"Mediterrani",'O',34);
		organismes.add(peix2);
		Peix peix3 = new Peix("peix","peixos",'M',2,10,3,5,"Mediterrani",'F',34);
		organismes.add(peix3);
		Planta planta1 = new Planta("planta","plantes",'B',18,19,6,9,'T');
		organismes.add(planta1);
		Planta planta2 = new Planta("planta","plantes",'M',15,17,7,8,'B');
		organismes.add(planta2);
		Planta planta3 = new Planta("planta","plantes",'A',20,23,3,5,'A');
		organismes.add(planta3);

		for (int i = 0; i <= organismes.size() - 1; i++) {
			System.out.println(organismes.get(i));
		}
	}

}
