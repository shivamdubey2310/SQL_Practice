# SQL Practice

A hands-on SQL practice project built around a realistic e-commerce style dataset.

This repository includes:
- Generated CSV data for five related tables
- 110 topic-wise SQL practice questions
- SQL solutions in markdown and notebook formats
- A Python data generator to create fresh datasets

## What You Will Practice

The question set is organized into 11 core SQL topics (10 questions each):
- SELECT
- WHERE
- ORDER BY and LIMIT
- DISTINCT
- Aggregations
- GROUP BY
- HAVING
- JOINs
- Subqueries
- CASE WHEN
- Window Functions

Total: 110 questions.

## Repository Structure

```text
SQL_Practice/
├── Data/
│   ├── users.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── payments.csv
├── DataGenerator.py
├── Questions.md
├── Solutions.md
├── ingestion.ipynb
├── Solutions.ipynb
└── README.md
```

## Data Model

The dataset follows a simple commerce flow:
- `users` -> customer details
- `orders` -> one order belongs to one user
- `order_items` -> line items for each order
- `products` -> product catalog
- `payments` -> payment records for orders

Typical joins you will use:
- `orders.user_id = users.user_id`
- `order_items.order_id = orders.order_id`
- `order_items.product_id = products.product_id`
- `payments.order_id = orders.order_id`

## Quick Start

### 1. Prerequisites

- Python 3.9+
- A SQL engine (SQLite, DuckDB, PostgreSQL, or MySQL)
- Optional: Jupyter Notebook support in VS Code

### 2. Install Python Dependencies

```bash
pip install pandas faker tqdm
```

### 3. Generate Data

If you want fresh CSV files, run:

```bash
python DataGenerator.py
```

Note: the script currently writes CSVs in the current working directory. Run it from the project root, then move files into `Data/` if needed.

### 4. Load Data Into Your SQL Engine

Use the CSV files inside `Data/` to create and populate tables in your preferred SQL engine.

If you are using notebooks, `ingestion.ipynb` can be used as the import and setup workflow.

## How To Use This Repository

Recommended learning flow:
1. Open `Questions.md` and solve topic by topic.
2. Write and run your own queries against the dataset.
3. Compare your answers with `Solutions.md`.
4. Use `Solutions.ipynb` when you want to execute and inspect results interactively.

## Notes

- Questions and solutions are written in generic SQL style.
- Minor syntax differences may appear across SQL engines.
- Some queries may need small adjustments depending on your engine (for example date functions or alias handling in `HAVING`).
