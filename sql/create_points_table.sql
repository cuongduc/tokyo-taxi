--
-- Create `points` table
--
CREATE TABLE points (
    id INT PRIMARY KEY,
    geometry geography(POINT; 4326) -- 2D point
);