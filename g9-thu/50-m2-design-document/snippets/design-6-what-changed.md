## 6. What changed since M1

### Change 1 - A booking is 1 to 4 whole hours, starting on the hour

M1 implied one-hour slots - BR10's example counts 16 slots between 06:00 and 22:00, and
every booking example in US05 is whole hours - but no rule said so, and nothing capped
how long one booking could be. Designing `booking_slot` (ADR 2) forced the question: one
row per *what*? **BR11 now reads: "a booking covers 1 to 4 consecutive whole hours, each
starting on the hour; each hour holds exactly one active booking".** US05 gains
acceptance criterion 5: *Given a venue open 06:00-22:00, when I choose a start time,
then only 06:00, 07:00 … 21:00 are offered, and I cannot choose more than 4 hours.*
The 4-hour cap is a Product Owner decision, so that one account cannot hold a pitch for
a whole evening.
<!-- TODO @thunopro: confirm the 4-hour cap with the team at Sprint 2 Planning. -->

### Change 2 - The owner now gives each venue a sport and an area, from fixed lists

US03 searches by sport **and** area (BR9), but in M1 US06 the owner entered only a name,
an address, a price and photos - so no venue would ever carry the sport or the area a
customer searches for. Drawing the ERD exposed the gap: `venue` needs `sport` and
`area` columns, and the search needs something to match. Typed text would not be
enough - "Cầu Giấy", "Cau Giay" and "Q. Cau Giay" would be three different areas and
Minh's search would miss two of them. **US06 gains acceptance criterion 5:** *Given I
add a venue, when I choose its sport and area, then both come from drop-down lists
(Football / Badminton / Tennis / Pickleball; the districts of Hanoi) and cannot be
typed.* BR9 now says sport and area are chosen from fixed lists; `venue.sport` enforces
it with a `CHECK`.

### Change 3 - Email verification is stubbed for Sprint 2

BR4 (unverified accounts cannot book) is unchanged, but sending real email needs an SMTP
account and a password in `.env`, which would add a step to `SETUP.md` that the
instructor cannot complete. Until Sprint 3 the verification link is printed to the
console; the data model already has `email_verified_at`, so nothing else changes.

<!-- TODO @thunopro: add what the Milestone 1 feedback from the instructor asked for
     once it is returned, and cite it here. -->
