## W3 School

We'll be playing with the live database available here:

http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

## Questions

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT * FROM Customers WHERE City='Madrid'
```

2) What is the most common city for customers?

```sql
SELECT City, COUNT(*) FROM Customers GROUP BY City
```

3) What category has the most products?

```sql
SELECT CategoryName, COUNT(*) FROM Categories
JOIN Products on (Categories.CategoryID = Products.CategoryID)
GROUP BY CategoryName
```

## Together

1. What customers are from the UK?
2. What is the name of the customer who has the most orders?

## Labwork

1. What supplier has the highest average product price?
2. What category has the most orders?
3. What employee made the most sales (by number of sales)?
4. What employee made the most sales (by value of sales)?
5. What Employees have BS degrees? (Hint: Look at LIKE operator)
6. What supplier has the highest average product price *assuming they have at least 2 products* (Hint: Look at the HAVING operator)

Submit these SQL queries as a .sql file under lab_submissions/lab2/yourname, using SQL comments to have the question referring to each:

```sql
-- What supplier has the highest average product price?
SELECT your_query

-- What category has the most orders?
```

