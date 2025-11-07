CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO users (name, email) VALUES
('Ivan', 'ivan@example.com'),
('Olga', 'olga@example.com'),
('Stepan', 'stepan@example.com');
