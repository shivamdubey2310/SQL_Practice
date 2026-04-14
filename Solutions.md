# 🟢 1. SELECT (1–10)

```sql
-- 1
SELECT * FROM users;

-- 2
SELECT name, email FROM users;

-- 3
SELECT * FROM products;

-- 4
SELECT name FROM products;

-- 5
SELECT user_id, city FROM users;

-- 6
SELECT * FROM orders;

-- 7
SELECT order_id, status FROM orders;

-- 8
SELECT * FROM payments;

-- 9
SELECT name, price FROM products;

-- 10
SELECT * FROM order_items;
```

---

# 🟢 2. WHERE (11–20)

```sql
-- 11
SELECT * FROM users
WHERE country = 'India';

-- 12
SELECT * FROM products
WHERE price > 1000;

-- 13
SELECT * FROM orders
WHERE status = 'shipped';

-- 14
SELECT * FROM payments
WHERE payment_status = 'failed';

-- 15
SELECT * FROM users
WHERE country IN ('USA', 'Canada');

-- 16
SELECT * FROM products
WHERE stock < 50;

-- 17
SELECT * FROM orders
WHERE order_date > '2024-01-01';

-- 18
SELECT * FROM payments
WHERE amount > 1000;

-- 19
SELECT * FROM users
WHERE country != 'India';

-- 20
SELECT * FROM products
WHERE price BETWEEN 100 AND 500;
```

---

# 🟢 3. ORDER BY & LIMIT (21–30)

```sql
-- 21
SELECT * FROM products
ORDER BY price ASC;

-- 22
SELECT * FROM products
ORDER BY price DESC;

-- 23
SELECT * FROM products
ORDER BY price ASC
LIMIT 5;

-- 24
SELECT * FROM products
ORDER BY price DESC
LIMIT 10;

-- 25
SELECT * FROM users
ORDER BY name;

-- 26
SELECT * FROM orders
ORDER BY order_date DESC
LIMIT 10;

-- 27
SELECT * FROM payments
ORDER BY amount;

-- 28
SELECT * FROM payments
ORDER BY amount DESC
LIMIT 3;

-- 29
SELECT * FROM users
ORDER BY created_at;

-- 30
SELECT * FROM products
LIMIT 20;
```

---

# 🟢 4. DISTINCT (31–40)

```sql
-- 31
SELECT DISTINCT country FROM users;

-- 32
SELECT DISTINCT city FROM users;

-- 33
SELECT DISTINCT category FROM products;

-- 34
SELECT DISTINCT status FROM orders;

-- 35
SELECT DISTINCT payment_method FROM payments;

-- 36
SELECT DISTINCT user_id FROM orders;

-- 37
SELECT DISTINCT product_id FROM order_items;

-- 38
SELECT DISTINCT payment_status FROM payments;

-- 39
SELECT DISTINCT stock FROM products;

-- 40
SELECT DISTINCT city, country FROM users;
```

---

# 🟢 5. AGGREGATIONS (41–50)

```sql
-- 41
SELECT COUNT(*) FROM users;

-- 42
SELECT COUNT(*) FROM products;

-- 43
SELECT COUNT(*) FROM orders;

-- 44
SELECT AVG(price) FROM products;

-- 45
SELECT MAX(price) FROM products;

-- 46
SELECT MIN(price) FROM products;

-- 47
SELECT SUM(amount) FROM payments;

-- 48
SELECT COUNT(*) FROM payments
WHERE payment_status = 'failed';

-- 49
SELECT AVG(amount) FROM payments;

-- 50
SELECT COUNT(*) FROM order_items;
```

---

# 🟢 6. GROUP BY (51–60)

```sql
-- 51
SELECT country, COUNT(*) 
FROM users
GROUP BY country;

-- 52
SELECT category, COUNT(*) 
FROM products
GROUP BY category;

-- 53
SELECT status, COUNT(*) 
FROM orders
GROUP BY status;

-- 54
SELECT user_id, COUNT(*) 
FROM orders
GROUP BY user_id;

-- 55
SELECT product_id, SUM(quantity) 
FROM order_items
GROUP BY product_id;

-- 56
SELECT payment_method, SUM(amount) 
FROM payments
GROUP BY payment_method;

-- 57
SELECT payment_status, COUNT(*) 
FROM payments
GROUP BY payment_status;

-- 58
SELECT category, AVG(price) 
FROM products
GROUP BY category;

-- 59
SELECT category, MAX(price) 
FROM products
GROUP BY category;

-- 60
SELECT city, COUNT(*) 
FROM users
GROUP BY city;
```

---

# 🟢 7. HAVING (61–70)

```sql
-- 61
SELECT country, COUNT(*) AS total_users
FROM users
GROUP BY country
HAVING total_users > 100;

-- 62
SELECT category, COUNT(*) AS total_products
FROM products
GROUP BY category
HAVING total_products > 50;

-- 63
SELECT user_id, COUNT(*) AS total_orders
FROM orders
GROUP BY user_id
HAVING total_orders > 5;

-- 64
SELECT product_id, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product_id
HAVING total_sold > 100;

-- 65
SELECT payment_method, SUM(amount) AS total_amount
FROM payments
GROUP BY payment_method
HAVING total_amount > 10000;

-- 66
SELECT city, COUNT(*) AS total_users
FROM users
GROUP BY city
HAVING total_users > 50;

-- 67
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING avg_price > 1000;

-- 68
SELECT user_id, COUNT(*) AS total_orders
FROM orders
GROUP BY user_id
HAVING total_orders > 10;

-- 69
SELECT product_id, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product_id
HAVING total_sold < 10;

-- 70
SELECT country, COUNT(*) AS total_users
FROM users
GROUP BY country
HAVING total_users < 20;
```

---

# 🟢 8. JOINs (71–80)

```sql
-- 71
SELECT u.name, o.order_id
FROM users u
JOIN orders o ON u.user_id = o.user_id;

-- 72
SELECT o.order_id, p.amount
FROM orders o
JOIN payments p ON o.order_id = p.order_id;

-- 73
SELECT oi.order_item_id, p.name
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

-- 74
SELECT p.name, oi.quantity
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;

-- 75
SELECT u.name, o.status
FROM users u
JOIN orders o ON u.user_id = o.user_id;

-- 76
SELECT u.name, pay.amount
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN payments pay ON o.order_id = pay.order_id;

-- 77
SELECT u.name, o.order_id, p.name, oi.quantity
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;

-- 78
SELECT u.*
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

-- 79
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;

-- 80
SELECT o.order_id, p.name
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```

---

# 🟢 9. SUBQUERIES (81–90)

```sql
-- 81
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- 82
SELECT user_id
FROM orders
GROUP BY user_id
HAVING COUNT(*) > (
    SELECT AVG(order_count)
    FROM (
        SELECT COUNT(*) AS order_count
        FROM orders
        GROUP BY user_id
    ) t
);

-- 83
SELECT * FROM payments
WHERE amount > (SELECT AVG(amount) FROM payments);

-- 84
SELECT * FROM products
WHERE price = (SELECT MAX(price) FROM products);

-- 85
SELECT user_id
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE p.amount = (SELECT MAX(amount) FROM payments);

-- 86
SELECT * FROM order_items
WHERE quantity = (SELECT MAX(quantity) FROM order_items);

-- 87
SELECT category
FROM products
GROUP BY category
HAVING AVG(price) = (
    SELECT MAX(avg_price)
    FROM (
        SELECT AVG(price) AS avg_price
        FROM products
        GROUP BY category
    ) t
);

-- 88
SELECT * FROM users
WHERE user_id NOT IN (SELECT DISTINCT user_id FROM orders);

-- 89
SELECT * FROM products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM order_items);

-- 90
SELECT * FROM payments p1
WHERE amount > (
    SELECT AVG(amount)
    FROM payments p2
    WHERE p1.order_id = p2.order_id
);
```

---

# 🟢 10. CASE WHEN (91–100)

```sql
-- 91
SELECT name, price,
CASE 
    WHEN price > 1000 THEN 'Expensive'
    ELSE 'Cheap'
END AS category
FROM products;

-- 92
SELECT name, country,
CASE 
    WHEN country = 'India' THEN 'Local'
    ELSE 'International'
END AS type
FROM users;

-- 93
SELECT payment_id, amount,
CASE 
    WHEN amount > 2000 THEN 'High'
    ELSE 'Low'
END AS payment_level
FROM payments;

-- 94
SELECT order_id, status,
CASE 
    WHEN status = 'delivered' THEN 'Completed'
    ELSE 'Pending'
END AS order_state
FROM orders;

-- 95
SELECT name, stock,
CASE 
    WHEN stock < 20 THEN 'Low'
    WHEN stock < 100 THEN 'Medium'
    ELSE 'High'
END AS stock_level
FROM products;

-- 96
SELECT user_id,
CASE 
    WHEN COUNT(*) > 5 THEN 'Active'
    ELSE 'Inactive'
END AS user_status
FROM orders
GROUP BY user_id;

-- 97
SELECT category,
CASE 
    WHEN AVG(price) > 1000 THEN 'Premium'
    ELSE 'Budget'
END AS category_type
FROM products
GROUP BY category;

-- 98
SELECT payment_id,
CASE 
    WHEN payment_status = 'success' THEN 'Successful'
    ELSE 'Failed/Pending'
END AS result
FROM payments;

-- 99
SELECT order_id,
CASE 
    WHEN COUNT(*) > 3 THEN 'Large'
    ELSE 'Small'
END AS order_size
FROM order_items
GROUP BY order_id;

-- 100
SELECT city,
CASE 
    WHEN COUNT(*) > 100 THEN 'Tier 1'
    ELSE 'Tier 2'
END AS city_type
FROM users
GROUP BY city;
```

---

# 🟢 11. WINDOW FUNCTIONS (101–110)

```sql
-- 101
SELECT name, price,
RANK() OVER (ORDER BY price DESC) AS price_rank
FROM products;

-- 102
SELECT order_id, user_id,
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date) AS rn
FROM orders;

-- 103
SELECT payment_id, amount,
SUM(amount) OVER (ORDER BY payment_date) AS running_total
FROM payments;

-- 104
SELECT user_id,
COUNT(*) AS total_orders,
RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_users
FROM orders
GROUP BY user_id;

-- 105
SELECT name, category, price,
DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC) AS rank_in_category
FROM products;

-- 106
SELECT payment_id, amount,
LAG(amount) OVER (ORDER BY payment_date) AS prev_payment
FROM payments;

-- 107
SELECT order_id, order_date,
LEAD(order_date) OVER (ORDER BY order_date) AS next_order
FROM orders;

-- 108
SELECT product_id, quantity,
SUM(quantity) OVER (PARTITION BY product_id ORDER BY quantity) AS cumulative_qty
FROM order_items;

-- 109
SELECT payment_method, amount,
RANK() OVER (PARTITION BY payment_method ORDER BY amount DESC) AS rank_method
FROM payments;

-- 110
SELECT category, name,
ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS row_num
FROM products;
```

----
