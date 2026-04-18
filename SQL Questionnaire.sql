create database ecommerce_sales;
use ecommerce_sales;

select * from sales;

-- 1. Which products generate the highest total revenue?
select product_name, max(revenue) from sales group by product_name;

-- 2. Which product category contributes the most to overall sales?
select product_category, sum(revenue) from sales group by product_category;

-- 3. How has total revenue changed year by year from 2022 to 2025?
select purchase_date, sum(revenue) from sales group by purchase_date;

-- 4. Which region generates the highest sales revenue?
select region, max(revenue) from sales group by region;

-- 5. What is the average order value across all transactions?
select order_id, avg(revenue) from sales group by order_id;

-- 6. Which payment method is used the most by customers?
select max(payment_method) from sales;

-- 7. Do certain payment methods lead to higher average order values?
select payment_method, avg(revenue) from sales group by payment_method;

-- 8. Which products have the highest and lowest customer ratings?
select product_name, min(customer_rating), max(customer_rating) from sales group by product_name;

-- 9. Which product category has the highest average customer rating?
select product_category, max(customer_rating) from sales group by product_category;

-- 10. Which region has the highest number of orders?
select region, count(order_id) from sales group by region;