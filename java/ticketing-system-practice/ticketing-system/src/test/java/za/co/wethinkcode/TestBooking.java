package za.co.wethinkcode;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import za.co.wethinkcode.model.Attendee;
import za.co.wethinkcode.model.Booking;
import za.co.wethinkcode.model.Event;

import static org.junit.jupiter.api.Assertions.*;

class TestBooking {

    private Attendee naledi;
    private Event jazz;

    @BeforeEach
    void setUp() {
        naledi = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        jazz = new Event("EVT-001", "Jazz Night", 150);
    }

    @Test
    void constructor_setsAllFields() {
        Booking booking = new Booking(1, naledi, jazz, 2);
        assertEquals(1, booking.bookingId());
        assertEquals("Naledi Khumalo", booking.attendee().name());
        assertEquals("EVT-001", booking.event().eventId());
        assertEquals(2, booking.seats());
    }

    @Test
    void constructor_defaultsStatusToConfirmed() {
        Booking booking = new Booking(1, naledi, jazz, 2);
        assertEquals(Booking.BookingStatus.CONFIRMED, booking.status(),
                "A new booking should default to CONFIRMED");
    }

    @Test
    void updateStatus_changesTheStatus() {
        Booking booking = new Booking(1, naledi, jazz, 2);
        booking.updateStatus(Booking.BookingStatus.CANCELLED);
        assertEquals(Booking.BookingStatus.CANCELLED, booking.status());
    }

    @Test
    void updateStatus_supportsAttendedStatus() {
        Booking booking = new Booking(2, naledi, jazz, 1);
        booking.updateStatus(Booking.BookingStatus.ATTENDED);
        assertEquals(Booking.BookingStatus.ATTENDED, booking.status());
    }

    @Test
    void toString_containsKeyDetails() {
        Booking booking = new Booking(7, naledi, jazz, 3);
        String result = booking.toString();
        assertNotNull(result, "toString() must be implemented");
        assertTrue(result.contains("7"), "toString() should contain the booking ID");
        assertTrue(result.contains("Naledi Khumalo"), "toString() should contain the attendee name");
        assertTrue(result.contains("Jazz Night"), "toString() should contain the event title");
        assertTrue(result.contains("3"), "toString() should contain the seat count");
    }
}
