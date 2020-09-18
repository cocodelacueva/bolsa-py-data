-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 18-09-2020 a las 03:08:40
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bolsa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `logs`
--

CREATE TABLE `logs` (
  `id` int(10) NOT NULL,
  `error_code` varchar(250) NOT NULL DEFAULT '',
  `extra-data` varchar(250) NOT NULL DEFAULT '',
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `merbal`
--

CREATE TABLE `merbal` (
  `id` int(100) NOT NULL,
  `simbolo` varchar(200) CHARACTER SET utf8 NOT NULL,
  `puntas_cantidad_compra` decimal(10,3) NOT NULL,
  `puntas_precio_compra` decimal(10,3) NOT NULL,
  `puntas_precio_venta` decimal(10,3) NOT NULL,
  `puntas_cantidad_venta` decimal(10,3) NOT NULL,
  `ultimo_precio` decimal(10,3) NOT NULL,
  `variacion_porcentual` decimal(6,2) NOT NULL,
  `apertura` decimal(10,3) NOT NULL,
  `maximo` decimal(10,3) NOT NULL,
  `minimo` decimal(10,3) NOT NULL,
  `ultimo_cierre` decimal(10,3) NOT NULL,
  `volumen` decimal(10,3) NOT NULL,
  `cantidad_operaciones` decimal(10,3) NOT NULL,
  `fecha` varchar(256) CHARACTER SET utf8 NOT NULL,
  `tipo_opcion` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `precio_ejercicio` decimal(10,3) DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `mercado` varchar(100) CHARACTER SET utf8 NOT NULL,
  `moneda` varchar(100) CHARACTER SET utf8 NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `options`
--

CREATE TABLE `options` (
  `id` int(11) NOT NULL,
  `name` varchar(250) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `value` text CHARACTER SET utf8 NOT NULL,
  `extra_value` varchar(250) CHARACTER SET utf8 NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `options`
--

INSERT INTO `options` (`id`, `name`, `value`, `extra_value`) VALUES
(1, 'refresh-token', 'uMIwIOZnmrn2R7ij5ZB2mMnyVTdxtdHZJwxbWlArtmodJF7QV6d5OrH04-2dUsAmVSCzSVShjsxNXyUeK2oII5m9uluatNM62Jd0KLhkEin3YEQUb63psgyrPh6kt_La323prUmbqMPT4VPCUSFPZkWCLtC6xIinIK7Y8oODoIuhPL9r5lyoGUtxs-EKPI07yjgTgM7QGIOB3-XBaY2yK2jz9T937Kwr5mDENrjTGvhMCilGcjcbkOXisZRA5qPSh-8QKF5aj6GrkoNz8_FTHzbm-604RC6MIGJ4eAsswE1630mNDD6cxtR5_4N6f9pazDivCNb40FXxlZGYROgRYYzQEzXs50z66aXT6NIvCNTwtcnRM2_20vb8SN8AaEFG', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `merbal`
--
ALTER TABLE `merbal`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `options`
--
ALTER TABLE `options`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `merbal`
--
ALTER TABLE `merbal`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT de la tabla `options`
--
ALTER TABLE `options`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
