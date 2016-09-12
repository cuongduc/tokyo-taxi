CREATE TABLE requests_with_income (
    id INT PRIMARY KEY,
    requested_time INT,
    start_point INT,
    end_point INT,
    forward_time_start INT,
    forward_time_end INT,
    backward_time_start INT,
    backward_time_end INT,
    milc_1 NUMERIC(20, 5),
    milc_2 NUMERIC(20, 5)
);