


# Goniómetre electrònic amb M5Stack

Aquest projecte implementa un **goniómetre electrònic educatiu** utilitzant el mòdul **M5Stack Fire**, una unitat IMU, un servomotor, una CardKB i un mòdul làser. Permet mesurar angles i calcular alçades mitjançant principis trigonomètrics, amb entrada per teclat i visualització integrada a la pantalla.

## Components utilitzats

- M5Stack Fire
- Unitat PAHUB (SKU: U040)
- Unitat IMU (SKU: U095)
- Unitat de 8 servos (SKU: U165)
- Servo SG90 (connectat al canal 7)
- Unitat CardKB (teclat mini)
- Mòdul làser amb activació mecànica
- Pantalla integrada (M5Stack)

## Funcionalitats

- Calibratge de l’angle (ajust d’offset del pitch)
- Moviment suau del braç amb el servo
- Entrada per teclat per a:
  - Longitud mesurada amb el làser
  - Alçada des del terra fins a la base del dispositiu
- Càlcul de l’alçada respecte al terra:
  ```
  angle_radian = |angle_real| * π / 180
  alçada_calculada = longitud * sin(angle_radian)
  alçada_total = alçada_base + alçada_calculada
  ```
- Valors arrodonits (mm per a alçades, rad per a angles)
- Interfície clara i guiada pas a pas

## AVÍS IMPORTANT ⚠️

S’ha detectat una **incoherència crítica** en el funcionament de **UiFlow 2.0**:

> Quan s’activa el **mode Custom (edició de codi Python)**, el sistema **deixa d’executar la lògica dels blocs visuals**, tot i que segueixen visibles.

Això pot provocar:

- Incoherències en els càlculs (per exemple, duplicació de la conversió a radians)
- Dades visuals desactualitzades o incorrectes
- Pèrdua de funcionalitats programades amb blocs

**Es recomana:**

1. Desenvolupar tota la lògica amb blocs i verificar-ne el comportament
2. Activar el mode Custom només al final, per fer ajustos finals
3. Revisar que el codi Python generat no dupliqui operacions que ja es fan amb blocs

Aquest avís es documentarà formalment i s’enviarà als desenvolupadors de M5Stack perquè ho revisin i corregeixin en futures versions.

## Crèdits

Projecte de **Neus Morlà Arias**, dissenyat per a la integració educativa de la trigonometria mitjançant la tecnologia de M5Stack.

## Repositori

[Projecte complet a GitHub](https://github.com/neusmstack/goniometre-m5stack)


---

Per a més detalls, consulta el fitxer principal `Electrogoniometre_Fix.py`.
