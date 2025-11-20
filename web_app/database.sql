-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS flask_login;

-- Usar la base de datos
USE flask_login;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Verificar que la tabla se creó correctamente
DESCRIBE users;
