DROP TABLE IF EXISTS Work;
DROP TABLE IF EXISTS Author;

--####################################################################################--

CREATE TABLE Author (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),           -- Name of the Author
    Birth INT,                  -- Birth Year of the Author
    Death INT                   -- Death Year of the Author
);

CREATE TABLE Work (
    ID INT PRIMARY KEY,
    AuthorID INT,               -- Author Reference
    Name VARCHAR(30),           -- Name of the Work
    Form VARCHAR(20),           -- Form of the Work (Orchestra, Trio, Quartet, etc.)
    Year INT,                   -- Year of Creation
    Opus VARCHAR(10),           -- Opus Number of the Work
    URL VARCHAR(50),            -- URL of the Video
    CONSTRAINT AuthorFK FOREIGN KEY (AuthorID) REFERENCES Author(ID)
);