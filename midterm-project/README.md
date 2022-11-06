# Credit Card Default Payment

## Data Set Information:

This research aimed at the case of customers default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel Sorting Smoothing Method to estimate the real probability of default. 

- You can access data on https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
- You can also find it in the dataset folder.

## Attribute Information:

- This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables:
---
- Limit Balance: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.
- Sex: Gender (1 = male; 2 = female).
- Education: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).
- Mariage: Marital status (1 = married; 2 = single; 3 = others).
- Age: Age (year).
---
- Pay1 - Pay6: History of past payment.
- pay 1 = the repayment status in September, 2005
- pay 2 = the repayment status in August, 2005
- pay 3 = the repayment status in July, 2005
- pay 4 = the repayment status in June, 2005
- pay 5 = the repayment status in May, 2005
- pay 6 = the repayment status in April, 2005
- The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.
---
- Bill 1- Bill 6: Amount of bill statement (NT dollar). 
- bill 1 = amount of bill statement in September, 2005
- bill 2 = amount of bill statement in August, 2005
- bill 3 = amount of bill statement in July, 2005
- bill 4 = amount of bill statement in June, 2005
- bill 5 = amount of bill statement in May, 2005
- bill 6 = amount of bill statement in April, 2005
---

- Pay amt 1 - Pay amt 6: Amount of previous payment (NT dollar). 
- pay amt 1 = amount paid in September, 2005
- pay amt 2 = amount paid in August, 2005
- pay amt 3 = amount paid in July, 2005
- pay amt 4 = amount paid in June, 2005
- pay amt 5 = amount paid in May, 2005
- pay amt6 = amount paid in April, 2005

---

- I used random forest classifier to solve the problem

Model outputs
- score = 0.796
- auc = 0.785