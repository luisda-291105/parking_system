# PARKING SYSTEM — sefaParkking

Sistema de gestión de parqueadero desarrollado en Python con fines educativos. Permite registrar ingresos y salidas de vehículos, calcular tarifas por hora y consultar el inventario de vehículos parqueados mediante un menú interactivo por consola.

---

## 📋 Estado actual (tras merge de `refactor` en `develop`)

| Característica | Detalle |
|---|---|
| **Rama activa** | `develop` (3 commits por delante de `origin/develop`) |
| **Último commit** | `6b6e189` — merge : se integra la rama refactor en develop |
| **Lenguaje** | Python 3 |
| **Persistencia** | Lista en memoria (se eliminó la capa SQLite: `baseDeDatos.py` / `dataBase`) |
| **Entrada futura prevista** | pandas / archivos CSV (según commits de refactor) |
| **Entorno virtual** | `.venv` |
| **Diagramas** | `doc/arquitecturaParking.drawio` (4 flujogramas) |
| **Estado funcional** | Menú operativo: ingreso, salida, inventario, salir |
| **Dependencias** | Solo librerías estándar (`sqlite3` ya no se usa; `datetime`) |

---

## 🗂️ Estructura del proyecto

```
parking_system/
├── main.py                    # Punto de entrada. Bucle del menú principal
├── README.md                  # Este archivo
├── requirements.txt           # Dependencias (vacío, solo stdlib)
├── .gitignore                 # Ignora venv/
├── mensajes/
│   ├── menu.py                # Menú principal de consola (4 opciones)
│   ├── mostrar.py             # MensajeMostrar: imprime vehículos y tarifas
│   └── validar.py             # Validar: valida espacio y lista de vehículos
├── registro/
│   ├── ingreso.py             # RegistrarIngreso: ingreso de vehículos
│   └── salida.py              # RegistroSalida: salida y cálculo de tarifa
├── doc/
│   └── arquitecturaParking.drawio  # Diagramas de flujo (draw.io / diagrams.net)
└── .venv/                     # Entorno virtual (no se rastrea en git)
```

> La carpeta `almacenamiento/` (con `baseDeDatos.py` y `dataBase`, SQLite) fue eliminada al integrar `refactor`, que migra la persistencia a pandas/CSV.

---

## 🚀 Cómo ejecutar

1. Clona el repositorio o abre la carpeta del proyecto.
2. Activa el entorno virtual (opcional pero recomendado):
   ```bash
   .venv\Scripts\activate     # Windows
   # o
   source .venv/bin/activate  # Linux/Mac
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```

---

## 🧩 Módulos y responsabilidades

### `main.py`
Punto de entrada. Inicia el bucle del menú principal y lo ejecuta hasta que el usuario elige salir.

### `mensajes/menu.py` — `menuOpciones()`
Menú por consola con 4 opciones:
1. **Registrar ingreso** — `ingreso.iniciar_registro_ingreso()`
2. **Registrar salida** — `salida.iniciar_registro_salida()`
3. **Ver inventario** — `MensajeMostrar(...).mostrar_todos_los_vehiculos()`
4. **Salir** — termina el programa

### `registro/ingreso.py` — `RegistrarIngreso`
Gestiona el ingreso de vehículos:
- `__init__(espacios_disponibles=1000)` — capacidad por defecto 1000 espacios.
- `iniciar_registro_ingreso()` — solicita placa, tipo y hora de ingreso.
- `registrar_ingreso_vehiculo(placa, tipo, hora_ingreso, ...)` — valida espacio y datos, crea el diccionario del vehículo y lo agrega a la lista.
- Usa `Validar` y `MensajeMostrar` de `mensajes/`.

### `registro/salida.py` — `RegistroSalida`
Gestiona la salida y el cobro:
- `PAGO_POR_HORA = 1500.0`, `FORMATO_HORA = "%H:%M"`.
- `__init__(vehiculos_parquiados, espacios_disponibles)` — recibe la lista compartida con el ingreso.
- `iniciar_registro_salida()` — solicita placa y busca el vehículo activo.
- `buscar_vehiculo_por_placa(placa)` — valida existencia y que no tenga salida previa.
- `calcular_tarifa_a_pagar(hora_salida_input, vehiculo)` — calcula horas y total, valida que salida > entrada.

### `mensajes/mostrar.py` — `MensajeMostrar`
Imprime el detalle de cada vehículo (tipo, placa, horas ingreso/salida, horas parquiadas, total a pagar) con validación defensiva de claves requeridas.

### `mensajes/validar.py` — `Validar`
- `validar_espacio_disponibles()` — True si quedan cupos.
- `validar_vehiculos_parquiados()` — True si hay al menos un vehículo.

---

## 💾 Modelo de datos (vehículo en memoria)

Cada vehículo es un diccionario con claves en mayúsculas:

| Clave | Tipo | Descripción |
|---|---|---|
| `PLACA` | str | Placa del vehículo |
| `TIPO` | str | Tipo (carro, moto, etc.) |
| `HORA_INGRESO` | str | Hora de entrada (HH:MM) |
| `HORA_SALIDA` | str | Hora de salida (HH:MM) |
| `HORAS_TRABAJADAS` | float | Horas parqueadas |
| `TOTAL_PAGAR` | float | Total a pagar en COP |

---

## 🧮 Tarifa

- **Precio por hora:** 1500 COP
- **Cálculo:** `horas_parqueadas = (hora_salida − hora_entrada) / 3600`
- **Total:** `round(horas_parqueadas × 1500, 2)`

---

## 📈 Diagramas (`doc/arquitecturaParking.drawio`)

Archivo con 4 páginas en diagrams.net:

1. **arquitectura sefaParkking** — Arquitectura general: `main.py` → menú → módulos → base de datos.
2. **registrar ingreso sefaParkking** — Flujo de entrada: validar espacio → leer placa → verificar duplicado → crear registro → abrir barrera → bienvenida.
3. **registrar salida sefaParkking** — Flujo de salida: leer placa → verificar existencia → registrar hora salida → calcular tarifa → validar pago → abrir bloqueo → despedida.
4. **tarifa sefaParkking** — Cálculo de tarifa: traer datos → validar completitud → calcular tiempo/tarifa → procesar pago → éxito/rechazo.

> Nota: los diagramas reflejan una arquitectura planeada (incluye `historial.py`, `movimientos.py`, `inventario.py`, `database.py`, `models.py`) que aún no está implementada en el código actual.

---

## 🛠️ Tecnologías

- **Python 3** (estándar, sin dependencias externas)
- **datetime** — manejo de horas para cálculo de tarifas
- **draw.io / diagrams.net** — diagramas de arquitectura y flujos

---

## ⚠️ Notas tras el merge de `refactor`

- Se eliminó la capa SQLite (`almacenamiento/baseDeDatos.py`, `almacenamiento/dataBase`). Los vehículos viven ahora en una lista en memoria compartida entre `RegistrarIngreso` y `RegistroSalida`.
- La persistencia se planea migrar a **pandas / archivos CSV** (commits de refactor), pero aún no está implementada.
- Los nombres de método cambiaron: `initRegister` → `iniciar_registro_ingreso`, `initExit` → `iniciar_registro_salida`, `mostrarTodosVehiculos` → `MensajeMostrar.mostrar_todos_los_vehiculos`.
- Las claves del diccionario del vehículo pasaron a mayúsculas (`PLACA`, `TIPO`, `HORA_INGRESO`, etc.).

---

## 📝 Licencia / Uso

Proyecto con fines educativos.
