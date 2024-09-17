# Write your MySQL query statement below
SELECT
ROUND(100*SUM(imm_orders)/COUNT(*), 2) AS immediate_percentage FROM
(SELECT
customer_id
,SUM(CASE WHEN customer_pref_delivery_date = order_date AND order_date = 
(SELECT MIN(order_date) FROM Delivery d WHERE d.customer_id = d1.customer_id) THEN 1 ELSE 0 END) AS imm_orders
,MIN(order_date) AS first_order
FROM Delivery d1
GROUP BY customer_id
) a