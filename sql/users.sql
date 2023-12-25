-- BINARY(16) refers to the use of uuid for id.
-- BOOLEAN is an alias for TINYINT(1), which allows TRUE or FALSE, represented by 1 and 0.
-- TIMESTAMP is used to record any changes for the record.
-- ON UPDATE CURRENT_TIMESTAMP means the column value will be updated automatically when a record is updated.

-- loyalty points refer to the measurement of their membership level, if yes.

CREATE TABLE users (
  id BINARY(16) NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  password VARCHAR(255) NOT NULL,
  birth_date DATE NOT NULL,
  loyalty_points INT(11) DEFAULT 0,
  payment_method VARCHAR(255),
  payment_card_number VARCHAR(20),
  payment_card_expiry VARCHAR(10),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);