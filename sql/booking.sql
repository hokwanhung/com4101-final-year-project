-- BINARY(16) refers to the use of uuid for id.
-- BOOLEAN is an alias for TINYINT(1), which allows TRUE or FALSE, represented by 1 and 0.
-- TIMESTAMP is used to record any changes for the record.
-- ON UPDATE CURRENT_TIMESTAMP means the column value will be updated automatically when a record is updated.

CREATE TABLE bookings (
  id BINARY(16) NOT NULL PRIMARY KEY,
  user_id BINARY(16) NOT NULL,
  room_id BINARY(16) NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (room_id) REFERENCES hotel_rooms(id)
);