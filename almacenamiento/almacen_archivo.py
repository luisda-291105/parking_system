"""
Módulo de almacenamiento persistente de registros del parqueadero.
Guarda y lee los datos en formato CSV usando Pandas.
"""

import pandas as pd
import os


class Almacenamiento:
    """
    Clase encargada de persistir los registros de vehículos en un archivo CSV.

    Attributes:
        ruta_csv (str): Ruta del archivo CSV donde se guardan los registros.
        columnas (list): Columnas esperadas en el archivo CSV.
    """

    COLUMNAS = ["PLACA", "TIPO", "HORA_INGRESO", "HORA_SALIDA",
                "HORAS_TRABAJADAS", "TOTAL_PAGAR"]

    def __init__(self, ruta_csv: str = "registro_vehiculos_parquiados.csv"):
        self.ruta_csv = ruta_csv

    def escribir(self, vehiculo: dict) -> bool:
        """
        Guarda un vehículo en el archivo CSV.
        Si el archivo no existe, lo crea con encabezados.
        Si ya existe, agrega la fila sin repetir encabezados.

        Args:
            vehiculo (dict): Diccionario con los datos del vehículo.

        Returns:
            bool: True si se guardó correctamente, False si hubo error.
        """
        try:
            # Convertimos el diccionario en un DataFrame de una sola fila
            df_nuevo = pd.DataFrame([vehiculo], columns=self.COLUMNAS)

            archivo_existe = os.path.exists(self.ruta_csv)

            # mode="a" agrega, header solo si el archivo NO existía antes
            df_nuevo.to_csv(
                self.ruta_csv,
                mode="a",
                header=not archivo_existe,   # ← encabezado solo la primera vez
                index=False,
                encoding="utf-8"
            )

            print(f"✅ Vehículo {vehiculo.get('PLACA', '?')} guardado en {self.ruta_csv}")
            return True

        except PermissionError:
            print(f"❌ Sin permiso para escribir en '{self.ruta_csv}'. ¿Está abierto en Excel?")
            return False
        except Exception as e:
            print(f"❌ Error al guardar el registro: {e}")
            return False

    def leer(self) -> pd.DataFrame:
        """
        Lee el archivo CSV y retorna un DataFrame con todos los registros.

        Returns:
            pd.DataFrame: Todos los vehículos guardados.
                          DataFrame vacío si el archivo no existe o está vacío.
        """
        try:
            if not os.path.exists(self.ruta_csv):
                print(f"⚠️  El archivo '{self.ruta_csv}' aún no existe.")
                return pd.DataFrame(columns=self.COLUMNAS)  # ← DataFrame vacío pero con estructura

            df = pd.read_csv(self.ruta_csv, encoding="utf-8")

            if df.empty:
                print("⚠️  El archivo CSV está vacío.")
                return df

            print(f"✅ {len(df)} registro(s) cargado(s) desde '{self.ruta_csv}'")
            return df

        except pd.errors.EmptyDataError:
            print("⚠️  El archivo CSV existe pero no tiene datos.")
            return pd.DataFrame(columns=self.COLUMNAS)
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")
            return pd.DataFrame(columns=self.COLUMNAS)

    def leer_como_lista(self) -> list:
        """
        Lee el CSV y retorna una lista de diccionarios (compatible con el resto del sistema).

        Returns:
            list: Lista de diccionarios con los registros, o lista vacía si hay error.
        """
        df = self.leer()
        return df.to_dict(orient="records")  # ← cada fila se convierte en un diccionario