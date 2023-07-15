DELIMITER //
-- Create a trigger that activates after a new order is placed
CREATE TRIGGER after_insert_orders
AFTER INSERT ON orders  -- The trigger is activated after a new row is inserted in the 'orders' table
FOR EACH ROW
BEGIN
  -- Decreases the quantity of the item in the 'items' table
  UPDATE items
  SET quantity = quantity - NEW.number  -- 'NEW.number' is the quantity of the item in the new order
  WHERE name = NEW.item_name; -- 'NEW.item_name' is the name of the item in the new order
END;//
DELIMITER ;
