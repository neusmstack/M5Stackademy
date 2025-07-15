
# Goniómetro electrónico con M5Stack

Este proyecto implementa un **goniómetro electrónico educativo** utilizando el módulo **M5Stack Fire**, una unidad IMU, un servomotor, una CardKB y un módulo láser. Permite medir ángulos y calcular alturas mediante principios trigonométricos, con entrada por teclado y visualización integrada en pantalla.

## Componentes utilizados

- M5Stack Fire
- Unidad PAHUB (SKU: U040)
- Unidad IMU (SKU: U095)
- Unidad de 8 servos (SKU: U165)
- Servo SG90 (conectado al canal 7)
- Unidad CardKB (teclado mini)
- Módulo láser con activación mecánica
- Pantalla integrada (M5Stack)

## Funcionalidades

- Calibración del ángulo (ajuste de offset del pitch)
- Movimiento suave del brazo con el servo
- Entrada por teclado para:
  - Longitud medida con el láser
  - Altura desde el suelo hasta la base del dispositivo
- Cálculo de la altura respecto al suelo:
  ```
  angle_radian = |angle_real| * π / 180
  altura_calculada = longitud * sin(angle_radian)
  altura_total = altura_base + altura_calculada
  ```
- Valores redondeados (mm para alturas, rad para ángulos)
- Interfaz clara y guiada paso a paso

## AVISO IMPORTANTE ⚠️

Se ha detectado una **incoherencia crítica** en el funcionamiento de **UiFlow 2.0**:

> Cuando se activa el **modo Custom (edición de código Python)**, el sistema **deja de ejecutar la lógica de los bloques visuales**, aunque sigan visibles.

Esto puede provocar:

- Incoherencias en los cálculos (ej. duplicación de conversión a radianes)
- Datos visuales desactualizados o incorrectos
- Pérdida de funcionalidades programadas con bloques

**Se recomienda:**

1. Desarrollar toda la lógica con bloques y verificar su comportamiento
2. Activar el modo Custom solo al final, para ajustes finales
3. Revisar que el código Python generado no duplique operaciones ya realizadas por los bloques

Este aviso se documentará formalmente y se enviará a los desarrolladores de M5Stack para su revisión y corrección en futuras versiones.

## Créditos

Proyecto de **Neus Morlà Arias**, diseñado para la integración educativa de la trigonometría mediante la tecnología de M5Stack.

## Repositorio

[Proyecto completo en GitHub](https://github.com/neusmstack/goniometre-m5stack)


---

Para más detalles, consulta el archivo principal `Electrogoniometre_Fix.py`.
