package za.co.wethinkcode.service;

import za.co.wethinkcode.model.Attendee;
import za.co.wethinkcode.model.Booking;
import za.co.wethinkcode.model.Event;

import java.util.List;
import java.util.Map;

public abstract class Venue {

    // TODO: declare all private fields here
    //       venueName (String), schedule (Map<String, Event>),
    //       bookings (List<Booking>), bookingCounter (int)


    // TODO: implement constructor — accepts venueName
    //       initialise schedule as a new HashMap
    //       initialise bookings as a new ArrayList


    // TODO: implement addEvent(Event event)
    //       adds the event to the schedule using its event ID as the key


    // TODO: implement findEvent(String eventId)
    //       returns the Event for the given ID, or null if not found


    // TODO: implement getSchedule()
    //       returns an UNMODIFIABLE Map of the schedule


    // TODO: implement quote(String eventId, int seats)
    //       returns seats * pricePerSeat(event)
    //       throws IllegalArgumentException if the event ID is unknown OR seats < 1


    // TODO: implement bookSeats(Attendee attendee, String eventId, int seats)
    //       throws IllegalArgumentException if event not found OR seats < 1
    //           OR fewer than 'seats' seats remain
    //       creates a new Booking (bookingId = ++bookingCounter)
    //       calls event.sellTicket() once per seat
    //       calls attendee.incrementBookings()
    //       adds the booking to bookings
    //       calls onBooking(booking)
    //       returns the booking


    // TODO: implement cancelBooking(int bookingId)
    //       finds the booking by ID, sets status to CANCELLED,
    //       calls event.releaseTicket() once per booked seat,
    //       calls attendee.decrementBookings(), returns the booking
    //       returns null if no matching booking found


    // TODO: implement getBookings()
    //       returns an UNMODIFIABLE list of all bookings


    // TODO: implement venueName()


    // TODO: declare the two abstract methods
    //       protected abstract double pricePerSeat(Event event);
    //       protected abstract void onBooking(Booking booking);
}
