package za.co.wethinkcode;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import za.co.wethinkcode.model.Attendee;
import za.co.wethinkcode.model.Booking;
import za.co.wethinkcode.model.Event;
import za.co.wethinkcode.service.StadiumVenue;
import za.co.wethinkcode.service.TheatreVenue;
import za.co.wethinkcode.service.Venue;

import static org.junit.jupiter.api.Assertions.*;

class TestVenue {

    private StadiumVenue stadium;
    private TheatreVenue theatre;
    private Event jazz;
    private Event slam;
    private Attendee naledi;
    private Attendee kabelo;

    @BeforeEach
    void setUp() {
        stadium = new StadiumVenue("FNB Stadium");
        theatre = new TheatreVenue("Market Theatre");

        jazz = new Event("EVT-001", "Jazz Night", 150);
        slam = new Event("EVT-002", "Poetry Slam", 3);

        naledi = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        kabelo = new Attendee(2, "Kabelo Mothibi", "kabelo@email.com");
    }

    // --- Schedule tests ---

    @Test
    void addEvent_canBeFoundByEventId() {
        stadium.addEvent(jazz);
        Event found = stadium.findEvent("EVT-001");
        assertNotNull(found, "Should find an event that was added");
        assertEquals("Jazz Night", found.title());
    }

    @Test
    void findEvent_returnsNullForUnknownEventId() {
        assertNull(stadium.findEvent("EVT-999"),
                "findEvent() should return null for an event ID that was never added");
    }

    @Test
    void getSchedule_returnsAllAddedEvents() {
        stadium.addEvent(jazz);
        stadium.addEvent(slam);
        assertEquals(2, stadium.getSchedule().size());
    }

    @Test
    void getSchedule_returnsUnmodifiableMap() {
        stadium.addEvent(jazz);
        assertThrows(UnsupportedOperationException.class,
                () -> stadium.getSchedule().put("Hack", jazz),
                "getSchedule() should return an unmodifiable map");
    }

    // --- Quote tests (polymorphism) ---

    @Test
    void quote_stadiumUsesStadiumPricing() {
        stadium.addEvent(jazz);
        assertEquals(360.0, stadium.quote("EVT-001", 2),
                "Stadium quote should be 2 * 180.0 = 360.0");
    }

    @Test
    void quote_theatreUsesTheatrePricing() {
        theatre.addEvent(jazz);
        assertEquals(960.0, theatre.quote("EVT-001", 3),
                "Theatre quote should be 3 * 320.0 = 960.0");
    }

    @Test
    void quote_isPolymorphicThroughBaseReference() {
        Venue venue = new TheatreVenue("Market Theatre");
        venue.addEvent(slam);
        assertEquals(320.0, venue.quote("EVT-002", 1),
                "A Venue reference must dispatch to the ACTUAL object's pricing (1 * 320.0)");
    }

    @Test
    void quote_throwsForUnknownEventId() {
        assertThrows(IllegalArgumentException.class,
                () -> stadium.quote("EVT-999", 2),
                "quote() should throw when the event ID does not exist");
    }

    @Test
    void quote_throwsForZeroSeats() {
        stadium.addEvent(jazz);
        assertThrows(IllegalArgumentException.class,
                () -> stadium.quote("EVT-001", 0),
                "quote() should throw when seats < 1");
    }

    // --- Booking tests ---

    @Test
    void bookSeats_createsBookingWithCorrectDetails() {
        stadium.addEvent(jazz);
        Booking booking = stadium.bookSeats(naledi, "EVT-001", 2);

        assertNotNull(booking);
        assertEquals("Naledi Khumalo", booking.attendee().name());
        assertEquals("Jazz Night", booking.event().title());
        assertEquals(2, booking.seats());
        assertEquals(Booking.BookingStatus.CONFIRMED, booking.status());
    }

    @Test
    void bookSeats_sellsOneTicketPerSeat() {
        stadium.addEvent(jazz);
        stadium.bookSeats(naledi, "EVT-001", 4);
        assertEquals(4, jazz.ticketsSold(),
                "Booking 4 seats should sell exactly 4 tickets");
    }

    @Test
    void bookSeats_incrementsAttendeeActiveBookings() {
        stadium.addEvent(jazz);
        stadium.bookSeats(naledi, "EVT-001", 2);
        assertEquals(1, naledi.activeBookings(),
                "One booking (regardless of seat count) adds ONE active booking");
    }

    @Test
    void bookSeats_assignsIncrementingBookingIds() {
        stadium.addEvent(jazz);
        Booking b1 = stadium.bookSeats(naledi, "EVT-001", 1);
        Booking b2 = stadium.bookSeats(kabelo, "EVT-001", 1);
        assertNotEquals(b1.bookingId(), b2.bookingId(),
                "Each booking should have a unique ID");
        assertEquals(b1.bookingId() + 1, b2.bookingId(),
                "Booking IDs should increment by 1");
    }

    @Test
    void bookSeats_throwsWhenEventIdNotFound() {
        assertThrows(IllegalArgumentException.class,
                () -> stadium.bookSeats(naledi, "EVT-999", 1),
                "Should throw when the event ID does not exist");
    }

    @Test
    void bookSeats_throwsForZeroSeats() {
        stadium.addEvent(jazz);
        assertThrows(IllegalArgumentException.class,
                () -> stadium.bookSeats(naledi, "EVT-001", 0),
                "Should throw when seats < 1");
    }

    @Test
    void bookSeats_throwsWhenNotEnoughSeatsRemain() {
        stadium.addEvent(slam);                    // capacity 3
        stadium.bookSeats(naledi, "EVT-002", 2);   // 1 seat left
        assertThrows(IllegalArgumentException.class,
                () -> stadium.bookSeats(kabelo, "EVT-002", 2),
                "Should throw when fewer seats remain than requested");
    }

    @Test
    void bookSeats_allowsBookingExactlyTheRemainingSeats() {
        stadium.addEvent(slam);                    // capacity 3
        stadium.bookSeats(naledi, "EVT-002", 2);   // 1 seat left
        Booking booking = stadium.bookSeats(kabelo, "EVT-002", 1);
        assertNotNull(booking,
                "Booking exactly the remaining seats (boundary) must succeed");
        assertEquals(3, slam.ticketsSold());
    }

    @Test
    void bookSeats_addsBookingToBookings() {
        stadium.addEvent(jazz);
        stadium.bookSeats(naledi, "EVT-001", 2);
        assertEquals(1, stadium.getBookings().size());
    }

    // --- Cancellation tests ---

    @Test
    void cancelBooking_setsStatusToCancelled() {
        stadium.addEvent(jazz);
        Booking booking = stadium.bookSeats(naledi, "EVT-001", 2);
        Booking cancelled = stadium.cancelBooking(booking.bookingId());

        assertNotNull(cancelled);
        assertEquals(Booking.BookingStatus.CANCELLED, cancelled.status());
    }

    @Test
    void cancelBooking_releasesAllBookedSeats() {
        stadium.addEvent(jazz);
        Booking booking = stadium.bookSeats(naledi, "EVT-001", 4);
        stadium.cancelBooking(booking.bookingId());
        assertEquals(0, jazz.ticketsSold(),
                "Cancelling a 4-seat booking should release all 4 tickets");
    }

    @Test
    void cancelBooking_decrementsAttendeeActiveBookings() {
        stadium.addEvent(jazz);
        Booking booking = stadium.bookSeats(naledi, "EVT-001", 2);
        stadium.cancelBooking(booking.bookingId());
        assertEquals(0, naledi.activeBookings());
    }

    @Test
    void cancelBooking_returnsNullForUnknownBookingId() {
        assertNull(stadium.cancelBooking(9999),
                "cancelBooking() should return null when the booking ID does not exist");
    }

    // --- getBookings ---

    @Test
    void getBookings_returnsUnmodifiableList() {
        stadium.addEvent(jazz);
        stadium.bookSeats(naledi, "EVT-001", 1);
        assertThrows(UnsupportedOperationException.class,
                () -> stadium.getBookings().clear(),
                "getBookings() should return an unmodifiable list");
    }

    // --- Inheritance tests ---

    @Test
    void stadiumVenue_isSubclassOfVenue() {
        assertTrue(stadium instanceof Venue,
                "StadiumVenue must extend Venue");
    }

    @Test
    void theatreVenue_isSubclassOfVenue() {
        assertTrue(theatre instanceof Venue,
                "TheatreVenue must extend Venue");
    }

    @Test
    void venueName_returnsCorrectName() {
        assertEquals("FNB Stadium", stadium.venueName());
        assertEquals("Market Theatre", theatre.venueName());
    }

    @Test
    void theatreVenue_canBookAndCancelSeats() {
        theatre.addEvent(slam);
        Booking booking = theatre.bookSeats(kabelo, "EVT-002", 2);

        assertNotNull(booking);
        assertEquals(Booking.BookingStatus.CONFIRMED, booking.status());
        assertEquals(2, slam.ticketsSold());
        assertEquals(1, kabelo.activeBookings());

        theatre.cancelBooking(booking.bookingId());
        assertEquals(Booking.BookingStatus.CANCELLED, booking.status());
        assertEquals(0, slam.ticketsSold());
        assertEquals(0, kabelo.activeBookings());
    }
}
