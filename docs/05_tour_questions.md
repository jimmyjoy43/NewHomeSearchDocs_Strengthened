# Tour Questions

Bring this list to every tour. Record the answers and also whether the answer felt direct, evasive, or overly rehearsed.

## 1. Approval and timing
1. How long does approval usually take from submission to final answer?
2. What documents usually slow an application down here?
3. Is there any known delay right now due to staffing, renovation, or portfolio changes?

## 2. Exact unit and exposure
4. Is this the exact unit I would sign, not just a model or comparable?
5. What direction does the unit face?
6. What are the nearest recurring noise sources: street, loading area, pool, gym, trash room, elevator, alley, bar, venue, or active construction?
7. Is there a unit above and below, and what is the floor/ceiling construction type?

## 3. Costs and concessions
8. What is the all-in recurring monthly cost: rent, parking, pet rent, utilities estimate, and any mandatory service fees?
9. What one-time charges are due at application, approval, and move-in?
10. If there is a concession, what is the exact dollar value and when does it expire?
11. Are there any fees or pass-throughs not visible on the current listing page?

## 4. Operations and maintenance
12. Who handles maintenance on site, and what is the average response time for non-emergency requests?
13. Is there 24-hour emergency maintenance coverage?
14. Is there a real 24x7 on-site human presence here: concierge, security desk, overnight staff, or equivalent?
15. How are packages handled after hours and during overflow periods?
16. How long has the current property manager and leasing manager been in place?
17. What issue generates the most resident complaints here today?

## 5. Quiet and enforcement
18. What are the quiet hours, and how are complaints documented and enforced?
19. Are there any building areas or stacks that are known to be louder than others?
20. Are furnished short-term stays, corporate units, or hotel-like occupancy allowed anywhere in the building?
21. Have there been any active construction, renovation, or major system-repair noise issues in the last 12 months?

## 6. Security and access
22. Has the building had recent issues with package theft, garage break-ins, tailgating, or unsecured entries?
23. Is the primary parking solution assigned, gated, monitored, or open-access, and can it realistically work as the daily default?
24. What is the guest parking policy in practice, not just on paper?

## 7. Unit condition
25. Test the HVAC.
26. Test the water pressure.
27. Check for odors, pests, water damage, warped flooring, window gaps, or unusual hums.
28. Confirm that every promised appliance is actually present and working.

## 8. Renewal and stability
29. What is the most common lease term here?
30. Roughly how often do residents renew versus move after one year?
31. Has the building changed ownership, management platform, or operating model recently?
32. Are there any planned changes that would affect residents in the next 12 months?

## Observe without asking directly
- How long did it take to reach a human before the tour?
- Are hallways clean, lit, and odor-free?
- Are amenities operational or staged?
- Does the team answer the actual question or pivot to selling points?
- Do residents seem relaxed and unhurried, or annoyed and on edge?

## Important guardrail
Do not ask demographic questions about who lives in the building. Ask about operational facts instead: quiet-hours enforcement, turnover, short-term-rental presence, renewal patterns, and after-hours support.

## After the tour
Map the visit back into the repo immediately while details are still fresh.

- Add a row to `data/tours.csv` using:
  - `tour_id`: a stable ID such as `{building_id}--{unit_id or tour_date}`
  - `building_id`: exact ID from `data/buildings.csv`
  - `unit_id`: exact ID from `data/units.csv` if you toured a specific listed unit
  - `tour_date`: `YYYY-MM-DD`
  - `tour_type`: for example `in_person` or `self_guided`
  - `approval_speed_business_days`: numeric string if learned on tour
  - `first_impression_score`: your quick overall visit score as a numeric string
  - `noise_observation`, `unit_condition`, `common_area_condition`, `staff_responsiveness`, `questions_answered`, `red_flags`, `follow_up_needed`, `notes`
- Update the toured unit in `data/units.csv`:
  - `tour_status = scheduled` before the visit
  - `tour_status = completed`, `skipped`, or `rejected` after the visit
- Update `data/buildings.csv` only if the tour changed a building-level view:
  - `status`
  - `approval_speed_business_days`
  - `open_questions`
  - `notes`
  - any building-level score or risk field you now have better evidence for
- Add a row to `data/decisions.csv` if the tour produced a real decision such as `advance_to_tour`, `backup`, `finalist`, `hold`, or `reject`.
