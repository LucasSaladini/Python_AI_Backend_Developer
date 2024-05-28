CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de email do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do cliente'
  );
  
  INSERt INTO usuarios_nova (id, nome, email, endereco, data_nascimento)
  SELECT id, nome, email, endereco, data_nascimento 
  FROM usuarios;
  
DROP TABLE usuarios;

ALTER TABLE usuarios_nova RENAME usuarios;

ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);
