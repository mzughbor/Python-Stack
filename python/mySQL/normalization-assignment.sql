-- Drop tables if they exist (clean start)
DROP TABLE IF EXISTS StudentInterest;
DROP TABLE IF EXISTS Interest;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Address;

-- Address table
CREATE TABLE Address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    street VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip VARCHAR(20)
);

-- Student table
CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(150) UNIQUE,
    address_id INT,
    CONSTRAINT fk_student_address FOREIGN KEY (address_id) REFERENCES Address(address_id)
);

-- Interest table
CREATE TABLE Interest (
    interest_id INT AUTO_INCREMENT PRIMARY KEY,
    interest_name VARCHAR(100) UNIQUE NOT NULL
);

-- Junction table for many-to-many Student <-> Interest
CREATE TABLE StudentInterest (
    student_id INT,
    interest_id INT,
    PRIMARY KEY (student_id, interest_id),
    CONSTRAINT fk_si_student FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_si_interest FOREIGN KEY (interest_id) REFERENCES Interest(interest_id) ON DELETE CASCADE
);

-- Example inserts (optional)
INSERT INTO Address (street, city, state, zip) VALUES
('123 Main St', 'Cairo', 'Cairo Gov', '11511'),
('456 Elm St', 'Giza', 'Giza Gov', '12411');

INSERT INTO Student (first_name, last_name, phone, email, address_id) VALUES
('Ali', 'Hassan', '01012345678', 'ali@example.com', 1),
('Sara', 'Omar', '01098765432', 'sara@example.com', 2);

INSERT INTO Interest (interest_name) VALUES
('Mathematics'),
('Programming'),
('Football'),
('Music');

INSERT INTO StudentInterest (student_id, interest_id) VALUES
(1, 2), -- Ali likes Programming
(1, 3), -- Ali likes Football
(2, 1), -- Sara likes Mathematics
(2, 4); -- Sara likes Music
