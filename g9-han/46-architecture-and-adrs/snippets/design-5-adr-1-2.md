## 5. Design decisions

### ADR 1 - Flask with server-rendered pages, not a JavaScript single-page app

- **Options:** (a) Flask + Jinja2 templates · (b) FastAPI backend + React frontend ·
  (c) Node.js / Express + EJS.
- **Chose:** (a) Flask + Jinja2.
- **Why:** The instructor runs our project from `SETUP.md` on a clean machine. Option (b)
  means two toolchains (Python *and* Node 20, `pip` *and* `npm install`), two processes
  and CORS - roughly double the steps that can fail. Every member has written Python in
  earlier courses; only one has used React. None of our 14 screens needs client-side
  state beyond a form - the richest one, the slot grid on `/venues/{id}`, is a table of
  at most 18 cells that can be re-rendered by the server.
- **What would change our mind:** if the owner's schedule screen (US09) needs drag-to-block
  across many days and a full page reload per click tests as too slow at the Sprint 3
  review, we add a small script (or htmx) to that one page - not a framework for the
  whole site.

### ADR 2 - Prevent double booking with one row per booked hour, not a check in code

- **Options:** (a) In `create_booking`, `SELECT` for an overlapping booking, then
  `INSERT` if none · (b) `UNIQUE (venue_id, start_at)` on `booking` · (c) a
  `booking_slot` table with one row per booked hour and `UNIQUE (venue_id, slot_start)`.
- **Chose:** (c).
- **Why:** BR11 is the rule the whole product stands on: customer A at 14:00:00 and
  customer B at 14:00:03 must end with one booking, not two. Option (a) has a gap
  between the `SELECT` and the `INSERT` where both requests see the hour as free. Option
  (b) only catches bookings that *start* at the same hour - A books 18:00-20:00, B books
  19:00-20:00, the start times differ and both are accepted. With (c) B's `INSERT` of the
  19:00 row fails with a constraint error however close together the requests are, and
  the service turns that error into **409 "This time slot is no longer available"**. The
  same rows carry each hour's price, which is exactly what BR12's per-segment split
  needs, and deleting them on cancel releases the hours (BR15).
- **What would change our mind:** if bookings stop being whole hours (for example the
  product owner asks for 30-minute badminton slots), one row per hour becomes one row per
  half-hour; if slots become arbitrary lengths, we would need a database with range
  exclusion constraints (PostgreSQL `EXCLUDE USING gist`).
