# 🎟️ Ticketing System — Java OOP Practice Assessment #2

## Overview

In this assessment you will complete an event-ticketing simulation in Java. The system
registers events at a venue, manages attendees, and processes seat bookings.

**This is a brownfield exercise.** A previous developer "finished" `Attendee.java` and
moved on. It compiles — but it is riddled with logic bugs that the test suite exposes
immediately. The remaining classes are skeletons. Your job is to repair the existing
code and complete the rest, following the principles of **Encapsulation** and
**Inheritance**, until **all unit tests pass**.

The test suite is **read-only**. Do not modify any file under `src/test`.

### Learning Outcomes

- Testing (unit testing, black-box thinking)
- Brownfield Development
- Agile Methodology
- OOP (Encapsulation, Inheritance, Abstraction, Polymorphism)
- Systems Design

---

## Time Limit

**2 hours**

---

## Assessment Structure

| Component         | Weight  | Recommended Time |
|-------------------|---------|------------------|
| Implementation    | **60%** | 70 minutes       |
| UML Class Diagram | **25%** | 30 minutes       |
| Written Questions | **15%** | 20 minutes       |

### Scoring

```
Coding Score   = (tests passed / total tests) × 60%
UML Score      = (marks earned / total UML marks) × 25%
Written Score  = (marks earned / 15) × 15%

Final Score    = Coding Score + UML Score + Written Score
```

To pass, your Final Score must be **60% or higher**. Your target is 90%+.

---

## Project Structure

```
ticketing-system/
├── pom.xml
├── README.md
├── answer.txt
└── src/
    ├── main/
    │   └── java/
    │       └── za/co/wethinkcode/
    │           ├── Main.java
    │           ├── model/
    │           │   ├── Event.java
    │           │   ├── Attendee.java    <-- BROKEN: repair it (Step 2)
    │           │   └── Booking.java
    │           └── service/
    │               ├── Venue.java
    │               ├── StadiumVenue.java
    │               └── TheatreVenue.java
    └── test/
        └── java/
            └── za/co/wethinkcode/
                ├── TestEvent.java
                ├── TestAttendee.java
                ├── TestBooking.java
                └── TestVenue.java
```

Run the full test suite at any time with:

```bash
mvn clean compile test
```

Your goal is **100% of tests passing** before submission.

---

## Implementation Steps

Work through the steps **in order** — later classes depend on earlier ones.

---

### Step 1 — Implement `Event`

**File:** `src/main/java/za/co/wethinkcode/model/Event.java`

An `Event` is a single show with a fixed seating capacity.

#### Fields

| Field         | Type     | Details                                                    |
|---------------|----------|-------------------------------------------------------------|
| `eventId`     | `String` | Unique identifier, e.g. `"EVT-001"`. Must be **private**.  |
| `title`       | `String` | The event title. Must be **private**.                       |
| `capacity`    | `int`    | Total seats available. Must be **private**.                 |
| `ticketsSold` | `int`    | Seats sold so far. Defaults to `0`. Must be **private**.    |

#### Constructor

Accepts `eventId` (String), `title` (String), `capacity` (int). Sets `ticketsSold` to `0`.

#### Methods

| Method            | Details                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `eventId()`       | Returns the event ID.                                                   |
| `title()`         | Returns the title.                                                      |
| `capacity()`      | Returns the capacity.                                                   |
| `ticketsSold()`   | Returns the number of tickets sold.                                     |
| `seatsRemaining()`| Returns `capacity - ticketsSold`.                                       |
| `hasCapacity()`   | Returns `true` if at least one seat remains.                            |
| `sellTicket()`    | Increases `ticketsSold` by 1. Throws `IllegalStateException` if the event is sold out. |
| `releaseTicket()` | Decreases `ticketsSold` by 1. Throws `IllegalStateException` if `ticketsSold` is already 0. |
| `toString()`      | Returns e.g. `"EVT-001: Jazz Night (12/150 sold)"`                      |

---

### Step 2 — Repair `Attendee` (brownfield)

**File:** `src/main/java/za/co/wethinkcode/model/Attendee.java`

An `Attendee` is a registered customer who books seats. The previous developer's version
**compiles cleanly** but contains **at least five logic bugs**. Do not trust code just
because it compiles — run the tests, read the failures, and repair the class until it
meets this specification:

#### Fields

| Field            | Type     | Details                                                    |
|------------------|----------|-------------------------------------------------------------|
| `attendeeId`     | `int`    | Unique ID. Must be **private**.                             |
| `name`           | `String` | Attendee's full name. Must be **private**.                  |
| `email`          | `String` | Contact email. Must be **private**.                         |
| `activeBookings` | `int`    | Bookings currently held. Defaults to `0`. Must be **private**. |

#### Constructor

Accepts `attendeeId` (int), `name` (String), `email` (String). Sets `activeBookings` to `0`.

#### Methods

| Method                  | Details                                                                     |
|-------------------------|------------------------------------------------------------------------------|
| `attendeeId()`          | Returns the attendee ID.                                                     |
| `name()`                | Returns the name.                                                            |
| `email()`               | Returns the email.                                                           |
| `activeBookings()`      | Returns the current number of active bookings.                               |
| `incrementBookings()`   | Increases `activeBookings` by 1.                                             |
| `decrementBookings()`   | Decreases `activeBookings` by 1. Throws `IllegalStateException` if already 0. |
| `toString()`            | Must contain the attendee's name, ID and email, e.g. `"[A001] Naledi Khumalo <naledi@email.com> — Bookings: 2"` |

---

### Step 3 — Implement `Booking`

**File:** `src/main/java/za/co/wethinkcode/model/Booking.java`

A `Booking` links an `Attendee` to an `Event` for a number of seats.

#### Enum (provided — do not remove)

```java
public enum BookingStatus {
    CONFIRMED,
    CANCELLED,
    ATTENDED
}
```

#### Fields

| Field        | Type            | Details                                                 |
|--------------|-----------------|----------------------------------------------------------|
| `bookingId`  | `int`           | Unique booking ID. Must be **private**.                 |
| `attendee`   | `Attendee`      | The booking attendee. Must be **private**.              |
| `event`      | `Event`         | The booked event. Must be **private**.                  |
| `seats`      | `int`           | Number of seats booked. Must be **private**.            |
| `status`     | `BookingStatus` | Current status. Defaults to `CONFIRMED`. Must be **private**. |

#### Constructor

Accepts `bookingId` (int), `attendee` (Attendee), `event` (Event), `seats` (int).
Sets `status` to `BookingStatus.CONFIRMED`.

#### Methods

| Method                        | Details                                                  |
|-------------------------------|----------------------------------------------------------|
| `bookingId()`                 | Returns the booking ID.                                  |
| `attendee()`                  | Returns the attendee.                                    |
| `event()`                     | Returns the event.                                       |
| `seats()`                     | Returns the number of seats.                             |
| `status()`                    | Returns the current status.                              |
| `updateStatus(BookingStatus)` | Updates the booking status.                              |
| `toString()`                  | A summary containing the bookingId, attendee name, event title, seat count and status. |

---

### Step 4 — Implement `Venue` (Abstract Class)

**File:** `src/main/java/za/co/wethinkcode/service/Venue.java`

`Venue` is an **abstract base class** that manages the event schedule and all bookings.
It delegates pricing and the booking announcement to its subclasses through **two
abstract methods**.

#### Fields

| Field            | Type                 | Details                                             |
|------------------|----------------------|------------------------------------------------------|
| `venueName`      | `String`             | The venue's display name. Must be **private**.      |
| `schedule`       | `Map<String, Event>` | Maps eventId → Event. Must be **private**.          |
| `bookings`       | `List<Booking>`      | All current and past bookings. Must be **private**. |
| `bookingCounter` | `int`                | Starts at `0`; incremented each time a booking is created. Must be **private**. |

#### Constructor

Accepts `venueName`. Initialises `schedule` as a new `HashMap` and `bookings` as a new
`ArrayList`.

#### Concrete Methods

| Method                                   | Details                                                                   |
|-------------------------------------------|----------------------------------------------------------------------------|
| `addEvent(Event)`                         | Adds the event to the schedule using its event ID as the key.             |
| `findEvent(String eventId)`               | Returns the `Event` for the given ID, or `null` if not found.             |
| `getSchedule()`                           | Returns an **unmodifiable** Map of the schedule.                          |
| `quote(String eventId, int seats)`        | Returns `seats × pricePerSeat(event)`. Throws `IllegalArgumentException` if the event ID is unknown OR `seats < 1`. |
| `bookSeats(Attendee, String eventId, int seats)` | Creates a new `Booking` (`bookingId = ++bookingCounter`), calls `event.sellTicket()` once per seat, calls `attendee.incrementBookings()`, adds the booking to `bookings`, calls `onBooking(booking)`, and returns the booking. Throws `IllegalArgumentException` if the event is not found OR `seats < 1` OR fewer than `seats` seats remain. |
| `cancelBooking(int bookingId)`            | Finds the booking by ID, sets status to `CANCELLED`, calls `event.releaseTicket()` once per booked seat, calls `attendee.decrementBookings()`, and returns the booking. Returns `null` if no matching booking found. |
| `getBookings()`                           | Returns an **unmodifiable** list of all bookings.                         |
| `venueName()`                             | Returns `venueName`.                                                      |

#### Abstract Methods

```java
protected abstract double pricePerSeat(Event event);

protected abstract void onBooking(Booking booking);
```

Subclasses must override both. `pricePerSeat` is called by `quote()`; `onBooking` is
called automatically inside `bookSeats()`.

---

### Step 5 — Implement `StadiumVenue` & `TheatreVenue`

**Files:** `service/StadiumVenue.java` and `service/TheatreVenue.java`

Both extend `Venue` and provide venue-specific pricing and booking messages.

#### StadiumVenue

|                          | Details                                                                                        |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Extends                  | `Venue`                                                                                        |
| Constructor              | Accepts `venueName`, passes it to `super()`.                                                   |
| `pricePerSeat(Event e)`  | Returns `180.0`.                                                                               |
| `onBooking(Booking b)`   | Prints: `"[venueName] — Gates open 2 hours early! [attendeeName] booked [seats] seat(s) for [eventTitle]."` |

#### TheatreVenue

|                          | Details                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------|
| Extends                  | `Venue`                                                                                          |
| Constructor              | Accepts `venueName`, passes it to `super()`.                                                     |
| `pricePerSeat(Event e)`  | Returns `320.0`.                                                                                 |
| `onBooking(Booking b)`   | Prints: `"[venueName] — Curtain at 19:30 sharp. [attendeeName] booked [seats] seat(s) for [eventTitle]."` |

---

## UML Class Diagram

Produce a UML class diagram for this project using **draw.io** (no other tool allowed).

Your diagram must include all six classes plus the enum and show:

- Class names (abstract class in *italics* or marked `<<abstract>>`)
- All fields with types and access modifiers (`+` public, `-` private, `#` protected)
- All methods with return types and parameters (abstract methods in *italics*)
- **Inheritance arrows** where one class extends another
- **Association arrows** where one class holds a reference to another, with multiplicities

Export as **PNG or PDF** and place it in the project root named `uml.pdf`.

---

## Written Questions

Answer in `answer.txt`. **Do not remove the comments. Do not change the format.**
Each question is worth 5 marks. Aim for 5–8 sentences each.

### Question 1 — OOP & Systems Design

A teammate says: *"StadiumVenue and TheatreVenue only differ in a price and a printed
message — an abstract Venue class is over-engineering. Two separate classes with the
booking logic copy-pasted would be simpler."* Respond. Cover: what an abstract class is,
why the shared booking/cancellation logic must not be duplicated (DRY / technical debt),
what the two abstract methods achieve that regular methods could not (mention the
Template Method idea and polymorphism), and how a third venue type (e.g. `ArenaVenue`)
would be added.

### Question 2 — Unit Testing

A junior developer says: *"I ran Main.java, the output looked right, so the code works —
tests are a waste of time."* Explain why unit testing matters. Cover: what a unit test
is and why it is objective, the Arrange–Act–Assert structure, what a regression is and
how a suite prevents one, and write TWO example JUnit 5 tests for `Event.sellTicket()`
(one happy path, one that asserts the sold-out exception).

### Question 3 — Black-Box Testing

Without looking at any implementation, design a black-box test plan for
`bookSeats(attendee, eventId, seats)` on an event with capacity 10 that already has
7 tickets sold (3 seats remain). Use equivalence partitioning and boundary value
analysis on the `seats` parameter: list your partitions, the boundary cases around the
remaining capacity, and concrete inputs with expected outcomes (including every failure
case the specification defines).

---

**NOTE:** Before pushing for grading, make sure it compiles: `mvn clean compile`

*Good luck — the show must go on! 🎭*
