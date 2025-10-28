-- Questão 1
SELECT * FROM Aluno;

-- Questão 2
SELECT nome, nota1 FROM Aluno;

-- Questão 3

SELECT * FROM Aluno
WHERE nota2 >8;

-- Questão 4
SELECT * FROM Aluno
WHERE data_nascimento >'2000-12-31';

-- Questão 5
SELECT nome, mensalidade
FROM Curso
WHERE mensalidade >600;

-- Questão 6
SELECT nome, ano FROM Turma
ORDER BY ano ASC;

-- Questão 7
SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano;

-- Questão 8
SELECT id_turma, ROUND(AVG(nota1), 2) AS media_nota1
FROM Aluno
GROUP BY id_turma;

-- Questão 9
SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;

-- Questão 10
SELECT nome, mensalidade 
FROM Curso
ORDER BY mensalidade DESC;


