The Customer Satisfaction Index (CSI) is a crucial indicator of customer satisfaction with a support service. It is determined by analyzing feedback from customers in the Support Center after they have received a response from the support team. The feedback is categorized as positive, negative, or neutral. The CSI metric graph visually represents the percentage of positive feedback out of all feedback received, providing a clear indication of customer satisfaction levels.<br><br>
To calculate the CSI, the following steps are followed:<br>
1. Duplicate feedback occurring within 30 minutes of each other is grouped to avoid counting duplicates multiple times.
2. Within each time group, the most frequently occurring feedback is selected as the group feedback value. In cases where multiple feedbacks have the same frequency, the most recent feedback is chosen.
3. The average value of all groups within the same ticket is calculated and rounded according to the following criteria:
   - Feedback scores ranging from [-1 to -0.3) are considered negative and rounded to -1.
   - Feedback scores ranging from [-0.3 to 0.3] are considered neutral and rounded to 0.
   - Feedback scores ranging from (0.3 to 1] are considered positive and rounded to 1.
<br>
Notes:<br>
The feedback is anonymous and linked to a specific ticket. As a result, we are unable to identify the customers who submitted the feedback, making it impossible for us to filter by feedback properties such as their owners. Our current filters are only applicable to tickets for this particular metric and do not extend to feedback or their owners due to the limited information available, which is solely based on the ticket ID.
