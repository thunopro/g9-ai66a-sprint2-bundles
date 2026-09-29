## Story → Screen → Endpoint → Table

One row per P0 story. Endpoints are the ones in [`docs/design.md`](design.md) section 3;
tables are the ones in section 2. When an endpoint or a table changes, this row changes in
the same pull request.

| Story | Issue | Screen | Endpoint(s) | Tables read / written |
|-------|-------|--------|-------------|-----------------------|
| US01 Customer registration | #14 | `/register` | `POST /api/auth/register`, `GET /api/auth/verify` | `user` |
| US02 User login | #15 | `/login` | `POST /api/auth/login` | `user` |
| US03 Customer searches for venues | #16 | `/search` | `GET /search` (walking skeleton), `GET /api/venues` | `venue`, `blocked_slot` |
| US04 Customer views venue details and availability | #17 | `/venues/{id}` | `GET /api/venues/{id}` | `venue`, `booking_slot`, `blocked_slot`, `review` |
| US05 Customer books a venue | #18 | `/booking/{venueId}` | `POST /api/bookings` | `booking`, `booking_slot`, `pricing_rule`, `blocked_slot`, `user` |
| US06 Venue owner adds a new venue | #21 | `/owner/venues/new` | `POST /api/owner/venues` | `venue`, `user` |
