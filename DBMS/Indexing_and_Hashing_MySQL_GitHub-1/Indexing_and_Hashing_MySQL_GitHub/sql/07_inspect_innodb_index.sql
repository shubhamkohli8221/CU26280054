-- Experiment 7: Inspect an InnoDB index
USE IndexHashLab;

CREATE TABLE Students_InnoDB (
    Student_ID INT PRIMARY KEY,
    Student_Name VARCHAR(50),
    Department VARCHAR(30)
) ENGINE = InnoDB;

CREATE INDEX idx_innodb_name
ON Students_InnoDB(Student_Name);

SHOW INDEX FROM Students_InnoDB;

-- Do not execute this statement; ordinary InnoDB indexes
-- do not support explicit USING HASH:
-- CREATE INDEX idx_hash_name
-- ON Students_InnoDB(Student_Name) USING HASH;
