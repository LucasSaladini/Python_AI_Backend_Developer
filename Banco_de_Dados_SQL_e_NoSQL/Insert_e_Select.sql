INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES
	(1, "Lucas Saladini", "test@test.com", "1993-09-28", "Rua 1, 10 - Bairro Novo São Paulo/SP");

INSERT INTO destinos (id, nome, descricao) VALUES
	(1, 'Praia do Rosa', 'Linda Praia');

INSERT INTO reservas (id, id_usuario, id_destino, status, data) VALUES
	(1, 1, 1, 'Pendente', '2024,05-28');

INSERT INTO reservas (id, id_usuario, id_destino, status, data) VALUES
	(2, 3, 3, 'Confirmada', '2024,05-28');

INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES
    (1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
    (2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
    (3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenica C, 789, Cidade X, Estado Y');
    
 INSERT INTO destinos (id, nome, descricao) VALUES
    (1, 'Praia das Tartarugas', 'Uma bela praia com areais brancas e mar cristalino'),
    (2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
    (3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');
        
INSERT INTO reservas (id, id_usuario,  id_destino, data, status) VALUES
    (1, 1, 2, '2023-07-10', 'Confirmada'),
    (2, 2, 1, '2023-08-05', 'Pendente'),
    (3, 3, 3, '2023-09-20', 'Cancelada');













SELECT * FROM usuarios;
SELECT * FROM reservas;
SELECT * FROM destinos;

SELECT * FROM usuarios
WHERE id = 1 AND nome LIKE "%Lucas%";

SELECT * FROM usuarios
WHERE id = 1 OR nome LIKE "%Maria%";
