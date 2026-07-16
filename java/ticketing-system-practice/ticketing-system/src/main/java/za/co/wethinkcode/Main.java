package za.co.wethinkcode;

import za.co.wethinkcode.model.Attendee;
import za.co.wethinkcode.model.Event;
import za.co.wethinkcode.service.StadiumVenue;
import za.co.wethinkcode.service.Venue;

public class Main {

    public static void main(String[] args) {
        // Optional smoke test — uncomment once your classes are implemented:
        //
        // Venue venue = new StadiumVenue("FNB Stadium");
        // Event jazz = new Event("EVT-001", "Jazz Night", 150);
        // venue.addEvent(jazz);
        //
        // Attendee naledi = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        // System.out.println("Quote for 2 seats: R" + venue.quote("EVT-001", 2));
        // venue.bookSeats(naledi, "EVT-001", 2);
        // System.out.println(jazz);
        System.out.println("Ticketing system — run 'mvn clean compile test' to check your progress.");
    }
}
