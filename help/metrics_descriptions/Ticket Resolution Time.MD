The average time taken (in hours) to communicate a solution to users is calculated based on iterations focused on delivering solutions, excluding those awaiting user responses. This excludes iterations where tickets are marked as Closed and only includes those marked as Active For Support or Active For Developers.

Important notes:

- Tickets managed by Ray are excluded from the calculation.
- Tickets that do not involve user interaction are not considered.
- Tickets with unusually long handling times exceeding 192 hours, such as long-term bugs, are also excluded.
- This metric is specifically targeted at a segment of the complete ticket life cycle. Unlike Ticket Lifetime, it excludes iterations involving Closed ticket statuses where we are waiting for user responses.
- For bugs, it is defined as the duration (in hours) of 'Active For Developers' period after the date the bug was created or converted from question.