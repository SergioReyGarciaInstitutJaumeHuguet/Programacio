package UF4.Hoteles;

public class main {

	public static void main(String[] args) {
		// Creo el hotel
		Hotel Hotel_1 = new Hotel();
		Hotel_1.crearHotel("Viva la vida", 3);
		System.out.println(Hotel_1);
		// Creo la habitación
		Habitacio h1 = new Habitacio(Hotel_1.getHabitacio().size()+1);
		h1.crearHabitacio(2, Categoria.NORMAL);
		// Añado la habitación al listado de hotel
		Hotel_1.addRoom(h1);
		System.out.println(Hotel_1);
		System.out.println(h1);
		// Creo el cliente
		Client c1 = new Client();
		c1.crearClient("Sergio", "77771127P", 789458765);
		System.out.println(c1);
		// Reservo la habitación para el cliente
		Reserva r1 = new Reserva(Hotel_1.getReserva().size()+1);
		r1.crearReserva(c1, h1, 3, false);
		System.out.println(r1);
		System.out.println(h1);
		// Cancelo la reserva
		r1.cancelarReserva(h1);
		System.out.println(r1);
		System.out.println(h1);
		// Creo tres habitaciones más, reservo dos para dos clientes diferentes y muestro las habitaciones que están disponibles
		Habitacio h2 = new Habitacio(Hotel_1.getHabitacio().size()+1);
		h2.crearHabitacio(2, Categoria.NORMAL);
		Hotel_1.addRoom(h2);
		Habitacio h3 = new Habitacio(Hotel_1.getHabitacio().size()+1);
		h3.crearHabitacio(2, Categoria.LUXE);
		Hotel_1.addRoom(h3);
		Habitacio h4 = new Habitacio(Hotel_1.getHabitacio().size()+1);
		h4.crearHabitacio(2, Categoria.SUPERLUXE);
		Hotel_1.addRoom(h4);
		Client c2 = new Client();
		c1.crearClient("Ivan", "88891827P", 789458765);
		Client c3 = new Client();
		c1.crearClient("Joel", "99991827P", 789458765);
		Client c4 = new Client();
		c1.crearClient("Sebastian", "10791827P", 789458765);
		Reserva r2 = new Reserva(Hotel_1.getReserva().size()+1);
		r2.crearReserva(c2, h2, 4, true);
		Reserva r3 = new Reserva(Hotel_1.getReserva().size()+1);
		r3.crearReserva(c3, h3, 2, false);
		Hotel_1.habitacionDisponible();
		
	}

}
