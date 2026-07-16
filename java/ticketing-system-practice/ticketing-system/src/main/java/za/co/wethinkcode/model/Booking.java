package za.co.wethinkcode.model;

public class Booking {

    public enum BookingStatus {
        CONFIRMED,
        CANCELLED,
        ATTENDED
    }

    // TODO: declare all private fields here
    //       bookingId (int), attendee (Attendee), event (Event),
    //       seats (int), status (BookingStatus, defaults to CONFIRMED)


    // TODO: implement constructor — accepts bookingId, attendee, event, seats
    //       set status to BookingStatus.CONFIRMED


    // TODO: implement accessors
    //       bookingId(), attendee(), event(), seats(), status()


    // TODO: implement updateStatus(BookingStatus status)


    // TODO: override toString()
    //       must contain bookingId, attendee name, event title, seats and status
    @Override
    public String toString() {
        return null; // replace with real implementation
    }
}
