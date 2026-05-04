Thesis: Higher tuition is associated with higher graduation rates across US colelges, this varies by state.

Data Source: US department of education college scoreboard api

How to run: Run python main.py
Data structures: Used list to store school records. Used dictionary to group schools by state. Used set to eliminate duplicate records. Used heap to find top 5 highest tuition schools.

Big O: Correlation calculations O(n), grouping by state O(n), head O(nlog), normalizing O(n).

Findings: Tuition and graduation rate show a weak linear relationship (correlation = 0). Some states have higher average tuitions than others but that does not seem to affect the relationship. High ranking institutions skew the tuition upwards, potentially impacting data.
