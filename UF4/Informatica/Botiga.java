package UF4.Informatica;

import java.util.ArrayList;

public class Botiga {
	private ArrayList<Articles> lista = new ArrayList<Articles>();
	private float cpu = 0, discDur = 0;
	
	public void afegirArticle(Articles a) {
		lista.add(a);
	}
	
	public void llistarEstoc() {
		System.out.println("CODI" + "	" + "DESCRIPCIÓ" + "	" + "UNI" + "	" + " CAP/VEL" + "	" + "PREU");
		System.out.println("----" + "	" + "----------" + "	" + "---" + "	" + "---------" + "	" + "----");
		for(int i = 0; i < lista.size(); i++) {
			System.out.println(lista.get(i));
			if(lista.get(i) instanceof CPU) {
				cpu += lista.get(i).preuTotal();
			} else {
				discDur += lista.get(i).preuTotal();
			}
		}
		System.out.println();
		System.out.println("Nombre total de disc durs en estoc: " + discDur);
		System.out.println("Nombre total de CPUs en estoc: " + cpu);
		System.out.println();
		System.out.println("Valor total de l'estoc: " + (discDur + cpu));
	}

}
