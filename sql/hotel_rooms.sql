-- BINARY(16) refers to the use of uuid for id.
-- BOOLEAN is an alias for TINYINT(1), which allows TRUE or FALSE, represented by 1 and 0.
-- TIMESTAMP is used to record any changes for the record.
-- ON UPDATE CURRENT_TIMESTAMP means the column value will be updated automatically when a record is updated.

-- special_view expects values such as NULL, "Mountain", and "Harbour", in which the prices gradually increases by HKD 100.

CREATE TABLE hotel_rooms (
  id BINARY(16) NOT NULL PRIMARY KEY,
  room_number INT(11) AUTO_INCREMENT NOT NULL,
  room_type VARCHAR(255) NOT NULL,
  special_view VARCHAR(255) DEFAULT NULL,
  room_capacity INT(11) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  availability BOOLEAN NOT NULL DEFAULT 1,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);