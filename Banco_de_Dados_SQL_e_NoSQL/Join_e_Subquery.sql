-- Joins
SELECT * FROM usuarios AS us
INNER JOIN reservas rs ON us.id = rs.id_usuario
INNER JOIN destinos ds ON rs.id_destino = ds.id;

SELECT * FROM usuarios as us
LEFT JOIN reservas rs ON us.id = rs.id_usuario;

SELECT * FROM reservas rs
RIGHT JOIN destinos ds ON rs.id = ds.id;

-- Subquery
SELECT * FROM destinos
WHERE id NOT IN (
  SELECT id_destino FROM reservas
);

SELECT * FROM usuarios
where id NOT IN (
  SELECT id_usuario FROM reservas
);

SELECT nome, 
	(SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios;
