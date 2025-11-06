-- Criação da procedure no MySQL
DELIMITER //
CREATE PROCEDURE sp_extrato_cliente(IN id_cliente INT, IN data_inicio DATE, IN data_fim DATE)
BEGIN
  SELECT SUM(CASE WHEN tipo = 'C' THEN valor ELSE -valor END) AS saldo
  FROM transacoes WHERE cliente_id = id_cliente;
  
  SELECT * FROM transacoes
  WHERE cliente_id = id_cliente
  AND data BETWEEN data_inicio AND data_fim
  ORDER BY data DESC
  LIMIT 10;
END //
DELIMITER ;
