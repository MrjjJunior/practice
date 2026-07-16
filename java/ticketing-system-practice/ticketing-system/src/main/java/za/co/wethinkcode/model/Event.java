package za.co.wethinkcode.model;

public class Event {

    // TODO: declare all private fields here
    //       eventId (String), title (String), capacity (int),
    //       ticketsSold (int, defaults to 0)


    // TODO: implement constructor — accepts eventId, title, capacity
    //       set ticketsSold to 0


    // TODO: implement accessors
    //       eventId(), title(), capacity(), ticketsSold()


    // TODO: implement seatsRemaining()
    //       returns capacity - ticketsSold


    // TODO: implement hasCapacity()
    //       returns true if at least one seat remains


    // TODO: implement sellTicket()
    //       increases ticketsSold by 1
    //       throws IllegalStateException if the event is sold out


    // TODO: implement releaseTicket()
    //       decreases ticketsSold by 1
    //       throws IllegalStateException if ticketsSold is already 0


    // TODO: override toString()
    //       Example: "EVT-001: Jazz Night (12/150 sold)"
    @Override
    public String toString() {
        return null; // replace with real implementation
    }
}
