SELECT COUNT(*) AS total_usuarios FROM usuarios;

SELECT COUNT(*) AS total_usuarios FROM usuarios us
INNER JOIN reservas rs ON us.id = rs.id_usuario;

SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios;

SELECT COUNT(*),
	id_destino
FROM reservas
GROUP BY id_destino;

SELECT COUNT(*) AS qtd_reservas,
	id_destino
FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas, id_destino;
