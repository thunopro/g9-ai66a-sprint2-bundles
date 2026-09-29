"""Update BR9 and BR11 after design.md section 6. Run from the repository root."""
from pathlib import Path

EDITS = {
    "docs/requirements.md": [
        ("| **BR9** | Search results must match the sport **and** the area at the same time; no match returns an explicit empty-state message |",
         "| **BR9** | Search results must match the sport **and** the area at the same time; sport and area are chosen from fixed lists, never typed; no match returns an explicit empty-state message |"),
        ("| **BR11** | A venue time slot holds exactly one active booking; the system re-checks availability immediately before confirming |",
         "| **BR11** | A booking covers 1 to 4 consecutive whole hours, each starting on the hour; each hour holds exactly one active booking; the system re-checks availability immediately before confirming |"),
        ("   the standard rate**, displayed as two separate lines and not rounded up (BR12).\n",
         "   the standard rate**, displayed as two separate lines and not rounded up (BR12).\n"
         "5. Given a venue open 06:00-22:00, when I choose a start time, then only 06:00, 07:00 ...\n"
         "   21:00 are offered, and I cannot choose more than 4 hours (BR11).\n"),
        ("   system returns **403** with **\"You do not have permission to access this page\"** (BR14).\n",
         "   system returns **403** with **\"You do not have permission to access this page\"** (BR14).\n"
         "5. Given I add a venue, when I choose its sport and area, then both come from drop-down\n"
         "   lists (Football / Badminton / Tennis / Pickleball; the districts of Hanoi) and cannot\n"
         "   be typed (BR9).\n"),
    ],
    "docs/traceability.md": [
        ("| BR9 | Search matches sport and area at the same time; no match returns an explicit message |",
         "| BR9 | Search matches sport and area at the same time, both chosen from fixed lists; no match returns an explicit message |"),
        ("| BR11 | A slot holds exactly one active booking; availability is re-checked before confirming |",
         "| BR11 | A booking is 1-4 whole hours; each hour holds exactly one active booking; availability is re-checked before confirming |"),
    ],
}
for file, pairs in EDITS.items():
    p = Path(file)
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in s:
            raise SystemExit(f"Not found in {file}: {old[:50]}...")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("Updated", file)
