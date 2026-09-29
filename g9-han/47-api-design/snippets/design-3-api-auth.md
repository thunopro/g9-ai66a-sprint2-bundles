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
