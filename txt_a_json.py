import json
import os

# Definimos la ruta de tu carpeta
ruta_carpeta = r'C:\Users\Fernando\Desktop\Funda.IA\jsons'
archivo_entrada = os.path.join(ruta_carpeta, 'jsons.txt') # Cambia a 'text.json' si ese es el nombre real del txt
archivo_salida = os.path.join(ruta_carpeta, 'convertido.json')

def transformar_archivo():
    datos = {}
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f):
                linea = linea.strip()
                if not linea:
                    continue
                
                # Si el archivo tiene formato Clave: Valor
                if ":" in linea:
                    clave, valor = linea.split(":", 1)
                    datos[clave.strip()] = valor.strip()
                else:
                    # Si no tiene ":" lo guarda con un índice numérico
                    datos[f"linea_{i+1}"] = linea

        # Crear el archivo JSON final
        with open(archivo_salida, 'w', encoding='utf-8') as f_json:
            json.dump(datos, f_json, indent=4, ensure_ascii=False)
            
        print(f"Proceso completado. Archivo creado en: {archivo_salida}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {archivo_entrada}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    transformar_archivo()