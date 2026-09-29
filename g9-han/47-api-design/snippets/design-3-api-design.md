## 3. API design

Pages are rendered by Flask; each page's data comes from, or is submitted to, the
endpoints below. Errors return JSON `{"error": "<message>", "rule": "BR<n>"}` with the
code listed; the message is exactly the sentence in the acceptance criterion.

**Authentication:** a signed session cookie set by `POST /api/auth/login`. An endpoint
marked *customer*, *owner* or *any user* returns **401** without a valid session and
**403** for the wrong role (BR14).

| # | Method | Path | Who | Input | Success | Error codes | Story |
|---|--------|------|-----|-------|---------|-------------|-------|
| 1 | POST | `/api/auth/register` | guest | `email`, `password`, `full_name`, `phone` | **201** `{user_id}`; verification link sent | **400** "Password must be at least 8 characters" (BR2) or "Phone number must be 10 digits" (BR3) · **409** "This email is already in use" (BR1) | US01 #14 |
| 2 | GET | `/api/auth/verify` | guest | `token` (query) | **200** account verified | **410** link older than 24 h (BR4) · **404** unknown token | US01 #14 |
| 3 | POST | `/api/auth/login` | guest | `email`, `password` | **200** `{role, redirect}`: `/dashboard`, `/owner/venues` or `/admin` (BR7) | **401** "Email or password is incorrect" - same text whether or not the email exists (BR6) · **423** "Account temporarily locked. Try again in 15 minutes" (BR5) | US02 #15 |
| 4 | GET | `/api/venues` | anyone | `sport`, `area` (query, both optional) | **200** list of `{id, name, sport, area, hourly_price}`; empty list plus `message: "No venues found"` (BR9) | **400** unknown sport or area | US03 #16 |
| 5 | GET | `/api/venues/{id}` | anyone | `date` (query, `YYYY-MM-DD`) | **200** venue detail plus 1-hour slots for that date, each `free` / `booked` / `blocked` (BR10, BR16) | **400** date malformed or in the past · **404** venue not found | US04 #17 |
| 6 | POST | `/api/bookings` | customer | `venue_id`, `date`, `start_hour`, `hours` | **201** `{code, total_price, segments:[{from, to, price}]}` (BR12) | **401** not signed in · **403** "Please verify your email before booking" (BR4) · **409** "This time slot is no longer available" (BR11) · **422** outside opening hours or blocked (BR16) | US05 #18 |
| 7 | POST | `/api/owner/venues` | owner | `name`, `sport`, `area`, `address`, `hourly_price`, `open_hour`, `close_hour` | **201** `{venue_id}` | **403** "You do not have permission to access this page" (BR14) · **422** "Hourly price must be at least 1,000 VND" or name length (BR13) | US06 #21 |
| 8 | GET | `/api/me/bookings` | customer | `status` (query: `upcoming` / `past`) | **200** own bookings only, newest first | **401** not signed in | US08 #20 |
| 9 | POST | `/api/bookings/{code}/cancel` | customer | - | **200** `{refund_amount}` - 100% or 50% (BR15) | **403** "You do not have permission to cancel this booking" (BR14) · **404** unknown code · **422** "A booking cannot be cancelled less than 2 hours before it starts" (BR15) | US07 #19 |
| 10 | POST | `/api/owner/venues/{id}/blocks` | owner | `from_date`, `to_date`, `start_hour`, `end_hour` | **201** `{blocked, skipped:[...]}` (BR17 bulk) | **403** not your venue (BR14) · **409** single hour already booked (BR17) | US09 #22 |
| 11 | DELETE | `/api/owner/venues/{id}/blocks/{slot}` | owner | - | **204** hour free again within 5 s (BR16) | **403** (BR14) · **404** not blocked | US09 #22 |
| 12 | GET | `/api/owner/bookings` | owner | `date` (query) | **200** bookings across the owner's venues for that day | **403** (BR14) · **400** date malformed | US10 #23 |
| 13 | PUT | `/api/owner/venues/{id}/pricing` | owner | list of `{weekday, start_hour, end_hour, price_per_hour}` | **200** rules saved | **403** (BR14) · **409** rules overlap (BR12) · **422** price out of range (BR13) | US11 #24 |
| 14 | POST | `/api/bookings/{code}/review` | customer | `rating`, `comment` | **201** `{review_id}`; venue average recalculated | **403** not your booking (BR14) · **409** already reviewed (BR18) · **422** booking not completed, rating not 1-5, comment > 1,000 characters (BR18) | US12 #25 |

Every P0 story (US01-US06) has at least one endpoint (rows 1-7). Rows 8-14 cover the P1
and P2 stories so Sprint 3 does not have to redesign the API.
