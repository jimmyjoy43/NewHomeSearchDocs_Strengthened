# Move Timeline

## Anchor dates
- Search anchor date: 2026-04-05
- Target move-in: 2026-04-15
- Desired latest lease-sign date: 2026-04-15

## Relative rule set
If the move target changes, recalculate every downstream date from the move-in target rather than editing isolated milestones by hand.

Current note:
- The lease-sign date and move-in date now match. This is internally consistent, but it leaves no schedule buffer for approval delays, document churn, or unit-readiness issues.

Recommended order:
1. Set target move-in date.
2. Back into the latest acceptable lease-sign date.
3. Back into the latest safe application date using the building-specific approval timeline.
4. Finish tours and eliminations before the last safe application date.

## Current decision gates
- 2026-04-05: restart breadth scan and refresh current candidate set
- 2026-04-06 to 2026-04-10: complete desk research on serious candidates
- 2026-04-07 to 2026-04-12: tours and same-day tour-note capture
- 2026-04-11 to 2026-04-13: elimination pass and decision-log update
- 2026-04-13 to 2026-04-14: finalist comparison and application prep
- 2026-04-15: target move-in
- 2026-04-15: latest lease-sign date, with effectively zero schedule slack

## Approval-speed rule
A building that cannot state a normal approval timeline, or that usually takes more than 7 business days, should be treated as a schedule risk and normally excluded.

## Biggest schedule risk
The highest schedule risk is not a mediocre building. It is a slow or opaque one.
