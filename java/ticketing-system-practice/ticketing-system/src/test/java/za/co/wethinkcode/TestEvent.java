package za.co.wethinkcode;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.model.Event;

import static org.junit.jupiter.api.Assertions.*;

class TestEvent {

    @Test
    void constructor_setsAllFields() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        assertEquals("EVT-001", event.eventId());
        assertEquals("Jazz Night", event.title());
        assertEquals(150, event.capacity());
    }

    @Test
    void constructor_defaultsTicketsSoldToZero() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        assertEquals(0, event.ticketsSold(),
                "A new event should have zero tickets sold");
    }

    @Test
    void seatsRemaining_isCapacityMinusSold() {
        Event event = new Event("EVT-002", "Comedy Gala", 100);
        event.sellTicket();
        event.sellTicket();
        assertEquals(98, event.seatsRemaining());
    }

    @Test
    void hasCapacity_trueWhileSeatsRemain() {
        Event event = new Event("EVT-003", "Poetry Slam", 2);
        assertTrue(event.hasCapacity());
        event.sellTicket();
        assertTrue(event.hasCapacity(),
                "One seat left should still count as capacity");
    }

    @Test
    void hasCapacity_falseWhenSoldOut() {
        Event event = new Event("EVT-003", "Poetry Slam", 2);
        event.sellTicket();
        event.sellTicket();
        assertFalse(event.hasCapacity(),
                "An event with all tickets sold has no capacity");
    }

    @Test
    void sellTicket_incrementsTicketsSold() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        event.sellTicket();
        assertEquals(1, event.ticketsSold());
    }

    @Test
    void sellTicket_throwsWhenSoldOut() {
        Event event = new Event("EVT-003", "Poetry Slam", 1);
        event.sellTicket();
        assertThrows(IllegalStateException.class, event::sellTicket,
                "sellTicket() should throw when the event is sold out");
    }

    @Test
    void releaseTicket_decrementsTicketsSold() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        event.sellTicket();
        event.sellTicket();
        event.releaseTicket();
        assertEquals(1, event.ticketsSold());
    }

    @Test
    void releaseTicket_throwsWhenNoneSold() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        assertThrows(IllegalStateException.class, event::releaseTicket,
                "releaseTicket() should throw when ticketsSold is already 0");
    }

    @Test
    void toString_showsIdTitleAndSalesProgress() {
        Event event = new Event("EVT-001", "Jazz Night", 150);
        for (int i = 0; i < 12; i++) {
            event.sellTicket();
        }
        assertEquals("EVT-001: Jazz Night (12/150 sold)", event.toString());
    }
}
