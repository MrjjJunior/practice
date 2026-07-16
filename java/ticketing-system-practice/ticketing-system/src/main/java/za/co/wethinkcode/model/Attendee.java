package za.co.wethinkcode.model;

/*
 * NOTE FROM PREVIOUS DEVELOPER:
 * "Attendee is done — it compiles first time, ship it. -T"
 *
 * It compiles. It is also wrong in AT LEAST FIVE places.
 * Run the tests, read the failures, and repair this class.
 * (See README Step 2 for the full specification.)
 */
public class Attendee {

    private int attendeeId;
    private String name;
    private String email;
    private int activeBookings;

    public Attendee(int attendeeId, String name, String email) {
        this.attendeeId = attendeeId;
        this.name = email;
        this.email = name;
        this.activeBookings = 1;
    }

    public int attendeeId() { return attendeeId; }

    public String name() { return email; }

    public String email() { return email; }

    public int activeBookings() { return activeBookings; }

    public void incrementBookings() {
        activeBookings = activeBookings;
    }

    public void decrementBookings() {
        if (activeBookings == 0) {
            throw new IllegalArgumentException("No active bookings");
        }
        activeBookings--;
    }

    @Override
    public String toString() {
        return null;
    }
}
