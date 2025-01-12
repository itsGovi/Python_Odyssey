SELECT
  Warehouse.warehouse_ID,
  CONCAT(Warehouse.state, ':', Warehouse.warehouse_alias) AS warehouse_name,
  COUNT(Orders.order_id) AS number_of_orders,
  (SELECT COUNT(*) FROM warehouse.Orders AS Orders) AS total_Orders
FROM warehouse.warehouse AS Warehouse
LEFT JOIN warehouse.orders AS Orders
  ON Warehouse.warehouse_ID = Orders.warehouse_ID
GROUP BY 
  Warehouse.warehouse_ID,
  warehouse_name
HAVING (Orders.order_id) > 0