INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES
	(1, "Lucas Saladini", "test@test.com", "1993-09-28", "Rua 1, 10 - Bairro Novo São Paulo/SP");

INSERT INTO destinos (id, nome, descricao) VALUES
	(1, 'Praia do Rosa', 'Linda Praia');

INSERT INTO reservas (id, id_usuario, id_destino, status, data) VALUES
	(1, 1, 1, 'Pendente', '2024,05-28');
