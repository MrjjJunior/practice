package za.co.wethinkcode;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.model.Attendee;

import static org.junit.jupiter.api.Assertions.*;

class TestAttendee {

    @Test
    void constructor_setsAllFields() {
        Attendee attendee = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        assertEquals(1, attendee.attendeeId());
        assertEquals("Naledi Khumalo", attendee.name(),
                "name() must return the NAME, not the email");
        assertEquals("naledi@email.com", attendee.email(),
                "email() must return the EMAIL, not the name");
    }

    @Test
    void constructor_defaultsActiveBookingsToZero() {
        Attendee attendee = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        assertEquals(0, attendee.activeBookings(),
                "A new attendee should have zero active bookings");
    }

    @Test
    void incrementBookings_increasesCountByOne() {
        Attendee attendee = new Attendee(2, "Kabelo Mothibi", "kabelo@email.com");
        attendee.incrementBookings();
        assertEquals(1, attendee.activeBookings());
    }

    @Test
    void incrementBookings_canBeCalledMultipleTimes() {
        Attendee attendee = new Attendee(2, "Kabelo Mothibi", "kabelo@email.com");
        attendee.incrementBookings();
        attendee.incrementBookings();
        attendee.incrementBookings();
        assertEquals(3, attendee.activeBookings());
    }

    @Test
    void decrementBookings_decreasesCountByOne() {
        Attendee attendee = new Attendee(3, "Zanele Sithole", "zanele@email.com");
        attendee.incrementBookings();
        attendee.incrementBookings();
        attendee.decrementBookings();
        assertEquals(1, attendee.activeBookings());
    }

    @Test
    void decrementBookings_throwsIllegalStateWhenAlreadyZero() {
        Attendee attendee = new Attendee(3, "Zanele Sithole", "zanele@email.com");
        assertThrows(IllegalStateException.class, attendee::decrementBookings,
                "decrementBookings() should throw IllegalStateException (wrong STATE) when already 0");
    }

    @Test
    void toString_containsIdNameAndEmail() {
        Attendee attendee = new Attendee(1, "Naledi Khumalo", "naledi@email.com");
        String result = attendee.toString();
        assertNotNull(result, "toString() must be implemented");
        assertTrue(result.contains("Naledi Khumalo"),
                "toString() should contain the attendee's name");
        assertTrue(result.contains("1"),
                "toString() should contain the attendee's ID");
        assertTrue(result.contains("naledi@email.com"),
                "toString() should contain the attendee's email");
    }
}
