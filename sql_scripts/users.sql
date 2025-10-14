CREATE TABLE users(
  id INT IDENTITY(1,1) PRIMARY KEY,
  username NVARCHAR(50) NOT NULL,
  password NVARCHAR(255) NOT NULL,
  name NVARCHAR(100) NULL
);

INSERT INTO users (username, password, name) VALUES ('admin','pass','Administrator');
