-- BINARY(16) refers to the use of uuid for id.
-- BOOLEAN is an alias for TINYINT(1), which allows TRUE or FALSE, represented by 1 and 0.
-- TIMESTAMP is used to record any changes for the record.
-- ON UPDATE CURRENT_TIMESTAMP means the column value will be updated automatically when a record is updated.

-- special_view expects values such as NULL, "Mountain", and "Harbour", in which the prices increase by HKD around 100 (150) and 150 (200).
-- The special_view also has less NULL values in better rooms.

USE fyp_project_default;

CREATE TABLE hotel_rooms (
  id BINARY(16) NOT NULL PRIMARY KEY,
  room_number INT(11) NOT NULL,
  room_type VARCHAR(255) NOT NULL,
  special_view VARCHAR(255) DEFAULT NULL,
  room_capacity INT(11) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  availability BOOLEAN NOT NULL DEFAULT 1,
  remark VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert 100 Standard rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 1, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 2, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 3, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 4, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 5, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 6, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 7, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 8, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 9, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 10, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 11, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 12, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 13, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 14, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 15, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 16, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 17, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 18, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 19, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 20, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 21, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 22, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 23, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 24, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 25, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 26, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 27, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 28, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 29, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 30, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 31, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 32, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 33, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 34, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 35, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 36, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 37, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 38, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 39, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 40, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 41, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 42, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 43, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 44, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 45, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 46, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 47, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 48, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 49, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 50, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 51, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 52, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 53, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 54, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 55, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 56, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 57, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 58, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 59, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 60, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 61, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 62, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 63, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 64, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 65, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 66, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 67, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 68, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 69, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 70, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 71, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 72, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 73, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 74, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 75, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 76, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 77, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 78, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 79, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 80, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 81, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 82, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 83, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 84, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 85, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 86, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 87, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 88, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 89, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 90, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 91, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 92, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 93, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 94, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 95, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 96, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 97, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 98, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 99, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 100, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW());

-- Insert 80 Standard rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 101, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 102, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 103, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 104, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 105, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 106, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 107, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 108, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 109, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 110, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 111, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 112, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 113, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 114, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 115, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 116, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 117, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 118, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 119, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 120, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 121, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 122, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 123, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 124, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 125, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 126, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 127, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 128, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 129, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 130, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 131, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 132, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 133, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 134, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 135, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 136, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 137, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 138, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 139, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 140, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 141, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 142, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 143, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 144, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 145, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 146, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 147, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 148, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 149, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 150, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 151, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 152, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 153, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 154, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 155, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 156, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 157, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 158, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 159, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 160, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 161, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 162, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 163, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 164, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 165, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 166, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 167, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 168, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 169, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 170, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 171, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 172, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 173, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 174, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 175, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 176, 'Standard', 'Harbour', 2, 900.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 177, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 178, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 179, 'Standard', 'Mountain', 2, 750.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 180, 'Standard', NULL, 2, 650.00, 1, "", NOW(), NOW());

-- Insert 80 Deluxe rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 181, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 182, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 183, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 184, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 185, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 186, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 187, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 188, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 189, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 190, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 191, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 192, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 193, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 194, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 195, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 196, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 197, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 198, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 199, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 200, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 201, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 202, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 203, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 204, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 205, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 206, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 207, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 208, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 209, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 210, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 211, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 212, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 213, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 214, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 215, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 216, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 217, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 218, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 219, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 220, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 221, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 222, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 223, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 224, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 225, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 226, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 227, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 228, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 229, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 230, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 231, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 232, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 233, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 234, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 235, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 236, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 237, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 238, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 239, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 240, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 241, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 242, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 243, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 244, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 245, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 246, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 247, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 248, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 249, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 250, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 251, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 252, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 253, 'Deluxe', 'Mountain', 2, 1100.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 254, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 255, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 256, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 257, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 258, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 259, 'Deluxe', NULL, 2, 1000.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 260, 'Deluxe', 'Harbour', 2, 1250.00, 1, "", NOW(), NOW());

-- Insert 40 Grand Deluxe rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 261, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 262, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 263, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 264, 'Grand Deluxe', 'Harbour', 2, 1600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 265, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 266, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 267, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 268, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 269, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 270, 'Grand Deluxe', 'Harbour', 2, 1600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 271, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 272, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 273, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 274, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 275, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 276, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 277, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 278, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 279, 'Grand Deluxe', 'Harbour', 2, 1600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 280, 'Grand Deluxe', 'Harbour', 2, 1600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 281, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 282, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 283, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 284, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 285, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 286, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 287, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 288, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 289, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 290, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 291, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 292, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 293, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 294, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 295, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 296, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 297, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 298, 'Grand Deluxe', NULL, 2, 1350.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 299, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 300, 'Grand Deluxe', 'Mountain', 2, 1450.00, 1, "", NOW(), NOW());

-- Insert 25 Junior Suite rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 301, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 302, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 303, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 304, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 305, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 306, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 307, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 308, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 309, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 310, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 311, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 312, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 313, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 314, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 315, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 316, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 317, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 318, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 319, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 320, 'Junior Suite', 'Mountain', 3, 2400.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 321, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 322, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 323, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 324, 'Junior Suite', NULL, 3, 2250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 325, 'Junior Suite', 'Harbour', 3, 2600.00, 1, "", NOW(), NOW());

-- Insert 10 Junior Suite rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 326, 'Executive Suite', 'Harbour', 4, 3950.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 327, 'Executive Suite', 'Harbour', 4, 3950.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 328, 'Executive Suite', NULL, 4, 3500.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 329, 'Executive Suite', 'Mountain', 4, 3700.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 330, 'Executive Suite', 'Harbour', 4, 3950.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 331, 'Executive Suite', NULL, 4, 3500.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 332, 'Executive Suite', 'Mountain', 4, 3700.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 333, 'Executive Suite', 'Mountain', 4, 3700.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 334, 'Executive Suite', 'Mountain', 4, 3700.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 335, 'Executive Suite', 'Harbour', 4, 3950.00, 1, "", NOW(), NOW());

-- Insert 2 Presidential Suite rooms.
INSERT INTO hotel_rooms (id, room_number, room_type, special_view, room_capacity, price, availability, remark, created_at, updated_at)
VALUES
(UNHEX(REPLACE(UUID(),'-','')), 336, 'Presidential Suite', 'Harbour', 5, 9250.00, 1, "", NOW(), NOW()),
(UNHEX(REPLACE(UUID(),'-','')), 337, 'Presidential Suite', 'Harbour', 5, 9250.00, 1, "", NOW(), NOW());