Customer Satisfaction Index is based on feedbacks: positive, negative, neutral.<br><br>
Here are the details of the calculation:<br>
Since there can be a lot of feedbacks following each other, we need to split them into 30 minutes groups first - if next feedback is posted within 30 minutes from the previous one, both these feedbacks fall within the same time goup.<br>
Next we select the most frequent feedback within each time group and take it as the group feedback value. If we cannot select the most frequent feedback because they have the same frequence (ex. there are to feedbacks in a group 1 and -1. their frequency = 1), we take the most recent from them.<br>
Finally, we calculate average by all groups within the same ticket as follows:<br>
- [-1; -0.3) = negative (-1)
- [-0.3; 0.3] = neutral (0)
- (0.3; 1] = positive (1)

Graph displays % of positive feedbacks to all feedbacks.