# foreignExchangeRatesAPI

*Project Overview*
Este proyecto es una implementación técnica de consulta de tasas de cambio para la región de Latinoamérica y el Caribe (LAC) utilizando la Visa Developer Platform (VDP). El objetivo es demostrar la capacidad de integración segura, manejo de protocolos financieros y resolución de problemas técnicos complejos en arquitecturas de pagos.

El proyecto demuestra la integración exitosa con arquitecturas bancarias modernas, cumpliendo con los estándares de "Error Cero" y rigor analítico aprendidos en el campo de la bioinformática clínica.

## Tecnologías y Estándares
- Lenguaje: Python 3.x (Requests, JSON processing).
- Protocolo: RESTful API.
- Seguridad (Mutual SSL): Implementación de Two-Way SSL mediante certificados X.509 (.pem / .key).
- Metodología: Desarrollo bajo marco de trabajo Agile (Scrum).
- Documentación: Trilingüe (EN/ES/PT) para soporte regional LAC.

## Arquitectura de Integración
La aplicación sigue el modelo de arquitectura oficial de Visa, posicionándose como el Client App Infra Middleware:

1. Client App: Interfaz de usuario/App que solicita la conversión
2. Middleware (Este proyecto): Procesa la lógica, gestiona los encabezados de seguridad y la firma de mensajes.
3. Visa API Gatewway: Valida las credenciales y redigirige la solicitud al Backend de Visa Direct.
4. Mutual SSL: Capa de seguridad que asegura que la comunicación solo ocurra entre servidores autorizados.

## Log de Troubleshooting
Uno de los pilares de este proyecto es la capacidad de resolución de problemas complejos. A continuación, se detallan los desafíos técnicos superados durante la fase de integración:

| **Escenario** | **Error HTTP** | **Causa Raíz** | **Resolución Técnica** |
| :--- | :--- | :--- | :--- |
| **Autenticación** | `401 Unauthorized` | Fallo en la validación de credenciales del Gateway. | Validación de `User ID` alfanumérico y ajuste de **Basic Auth** en el header de autorización. |
| **Sintaxis JSON** | `400 Bad Request` | Caracteres no permitidos (comentarios `#`) en el payload. | Limpieza del cuerpo de la solicitud para cumplir estrictamente con el estándar RFC 7159 de JSON. |
| **Validación de Esquema** | `400 Bad Request` | Diferencia de *Case-Sensitivity* entre versiones v1 y v2. | Análisis del esquema **OpenAPI 3.1.0**; ajuste de `markupRate` (v2) a `markUpRate` (v1). |

## Cómo Ejecutar

1. Clona el repositorio y asegúrate de tener Python instalado.
2. Descarga tus llaves desde el portal de Visa Developer y colócalas en la carpeta del proyecto.
3. El script consultará automáticamente las tasas para el par USD/COP (o el que desees configurar).

Nota: Este proyecto utiliza el entorno Sandbox de Visa y datos ficticios para fines de demostración técnica.
