# SQL Beginner Challenge #8: Join Two Tables with INNER JOIN

**Difficulty:** Beginner  
**Estimated time:** 15–20 minutes  
**Concepts:** `INNER JOIN`, joining tables, relational data  

This challenge introduces how to combine data from multiple tables using an `INNER JOIN`—a core skill when working with real-world relational databases.

---

## 🧠 The Problem

Until now, all queries used a single table.

A product manager now asks:

> “Show me each product along with its supplier name.”

That information is stored in **two related tables**, so you need to join them.

---

## 📊 Table Schemas

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| category | TEXT | Product category |
| price | DECIMAL | Product price |
| supplier_id | INTEGER | References `suppliers.supplier_id` |

---

### `suppliers`

| Column Name | Type | Description |
|------------|------|-------------|
| supplier_id | INTEGER | Unique supplier ID |
| supplier_name | TEXT | Supplier name |

---

## 🧪 Sample Data

### `products`

| product_id | name | category | price | supplier_id |
|-----------:|------|----------|------:|------------:|
| 101 | Wireless Mouse | Accessories | 24.99 | 1 |
| 102 | Mechanical Keyboard | Accessories | 89.00 | 1 |
| 103 | 27-inch Monitor | Displays | 229.99 | 2 |
| 104 | USB-C Hub | Accessories | 34.50 | 3 |
| 105 | Laptop Stand | Workspace | 39.99 | 2 |

---

### `suppliers`

| supplier_id | supplier_name |
|------------:|---------------|
| 1 | TechSource |
| 2 | DisplayWorks |
| 3 | GadgetCo |

---

## ✅ Requirements

Your query must:

- Join `products` and `suppliers`
- Use an `INNER JOIN`
- Match rows using `supplier_id`
- Return only:
  - Product `name`
  - `supplier_name`
- Not use `SELECT *`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

