CSI is a key measure of customer satisfaction with a support service. It is determined by analyzing feedback received from customers in the Support Center after they have received a response from the support team. The feedback can be categorized as positive, negative, or neutral. The CSI metric graph displays the percentage of positive feedbacks out of all feedbacks received. This graph provides a visual representation of customer satisfaction levels.<br><br>
To calculate the CSI, the following steps are taken:<br>
1. Duplicate feedback that occurs within 30 minutes of each other is grouped together. This is because users may click the feedback icon multiple times, resulting in duplicate feedback. By grouping them, we can avoid counting duplicates multiple times.
2. Within each time group, the most frequently occurring feedback is selected as the group feedback value. In cases where multiple feedbacks have the same frequency, the most recent feedback is chosen.
3. Finally, the average value of all groups within the same ticket is calculated and rounded according to the following criteria:<br>
    - Feedback scores ranging from [-1 to -0.3) are considered negative and rounded to -1.
    - Feedback scores ranging from [-0.3 to 0.3] are considered neutral and rounded to 0.
    - Feedback scores ranging from (0.3 to 1] are considered positive and rounded to 1.