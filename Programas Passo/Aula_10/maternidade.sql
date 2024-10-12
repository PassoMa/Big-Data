CREATE DATABASE maternidade;

CREATE TABLE mae (
    cpf INTEGER NOT NULL,
    nome VARCHAR(50),
    endereco VARCHAR(100),
    telefone VARCHAR(10),
    PRIMARY KEY (cpf)
    );

CREATE TABLE equipe_medica (
    codigo_eq INTEGER NOT NULL,
    nome VARCHAR(50),
    PRIMARY KEY (codigo_eq)
    );

CREATE TABLE profissional (
    crm INTEGER NOT NULL,
    nome VARCHAR(50),
    telefone VARCHAR(10),
    especialidade VARCHAR(20),
    codigo_eq INTEGER,
    PRIMARY KEY (crm),
    FOREIGN KEY (codigo_eq) REFERENCES equipe_medica(codigo_eq)
    )

CREATE TABLE bebe (
    codigo INTEGER NOT NULL,
    nome VARCHAR(50),
    data VARCHAR(10),
    especialidade VARCHAR(20),
    peso FLOAT,
    altura FLOAT,
    codigo_eq INTEGER,
    cpf INTEGER,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codigo_eq) REFERENCES equipe_medica(codigo_eq),
    FOREIGN KEY (cpf) REFERENCES mae(cpf)
    )