# 🧾 SQL Practice Set (Topic-wise)

Dataset: `users`, `products`, `orders`, `order_items`, `payments`

---

# 🟢 1. SELECT (10 Questions)

1. Select all columns from `users`.
2. Select only `name` and `email` from users.
3. Select all products.
4. Display product names only.
5. Select `user_id` and `city` from users.
6. Show all orders.
7. Display `order_id` and `status`.
8. Select all payments.
9. Show product `name` and `price`.
10. Select all columns from `order_items`.

---

# 🟢 2. WHERE (10 Questions)

11. Find users from 'India'.
12. Get products with price > 1000.
13. Find orders with status 'shipped'.
14. Get payments with status 'failed'.
15. Find users from 'USA' or 'Canada'.
16. Get products with stock < 50.
17. Find orders placed after a certain date.
18. Get payments above 1000.
19. Find users not from 'India'.
20. Get products with price between 100 and 500.

---

# 🟢 3. ORDER BY & LIMIT (10 Questions)

21. Sort products by price ascending.
22. Sort products by price descending.
23. Get top 5 cheapest products.
24. Get top 10 most expensive products.
25. Sort users by name.
26. Show latest 10 orders.
27. Sort payments by amount.
28. Get top 3 highest payments.
29. Sort users by created_at.
30. Show first 20 products.

---

# 🟢 4. DISTINCT (10 Questions)

31. Get unique countries from users.
32. Get unique cities.
33. Get distinct product categories.
34. Get distinct order statuses.
35. Get unique payment methods.
36. Get distinct user_ids from orders.
37. Get distinct product_ids from order_items.
38. Get distinct payment statuses.
39. Get unique stock values.
40. Get distinct combinations of city and country.

---

# 🟢 5. AGGREGATIONS (10 Questions)

41. Count total users.
42. Count total products.
43. Count total orders.
44. Find average product price.
45. Find max product price.
46. Find min product price.
47. Sum all payment amounts.
48. Count failed payments.
49. Find average order amount.
50. Count total order_items.

---

# 🟢 6. GROUP BY (10 Questions)

51. Count users per country.
52. Count products per category.
53. Count orders per status.
54. Count orders per user.
55. Sum quantity per product.
56. Sum payments per method.
57. Count payments per status.
58. Avg price per category.
59. Max price per category.
60. Count users per city.

---

# 🟢 7. HAVING (10 Questions)

61. Countries with more than 100 users.
62. Categories with more than 50 products.
63. Users with more than 5 orders.
64. Products sold more than 100 times.
65. Payment methods with high total (>10000).
66. Cities with more than 50 users.
67. Categories with avg price > 1000.
68. Users with total orders > 10.
69. Products with low sales (<10).
70. Countries with less than 20 users.

---

# 🟢 8. JOINs (10 Questions)

71. Join users and orders.
72. Join orders and payments.
73. Join order_items and products.
74. Get product names with order quantity.
75. Get user names with order status.
76. Get payment details with user names.
77. Join all tables to show full order info.
78. Find users with no orders (LEFT JOIN).
79. Find products never ordered.
80. Get orders with product names.

---

# 🟢 9. SUBQUERIES (10 Questions)

81. Products above avg price.
82. Users with more orders than average.
83. Orders with amount > avg payment.
84. Products with highest price.
85. Users who made highest payment.
86. Orders with max quantity.
87. Categories with highest avg price.
88. Users with no orders.
89. Products never sold.
90. Payments above avg per user.

---

# 🟢 10. CASE WHEN (10 Questions)

91. Label products as 'Expensive' (>1000) else 'Cheap'.
92. Categorize users by country.
93. Label payments as 'High' (>2000) or 'Low'.
94. Mark orders as 'Completed' or 'Pending'.
95. Categorize stock as 'Low', 'Medium', 'High'.
96. Label users as 'Active' if orders > 5.
97. Categorize categories based on avg price.
98. Label payments as success/failure group.
99. Create order size category (based on items).
100. Categorize cities as Tier 1 / Tier 2.

---

# 🟢 11. WINDOW FUNCTIONS (10 Questions)

101. Rank products by price.
102. Row number for orders per user.
103. Running total of payments.
104. Rank users by total orders.
105. Dense rank products per category.
106. Lag payment amounts.
107. Lead order dates.
108. Cumulative sum of quantity sold.
109. Rank payments by amount per method.
110. Row number partitioned by category.
