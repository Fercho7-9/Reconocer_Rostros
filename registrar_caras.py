from deepface import DeepFace
from pymongo import MongoClient
import os

# Configuración de MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ReconocimientoFacial"]
col = db["estudiantes"]

ruta_fotos = r"C:\Users\Fernando\Desktop\Funda.IA\fotos"

def registrar():
    print("🚀 Sincronizando fotos con la base de datos...")

    for archivo in os.listdir(ruta_fotos):
        if archivo.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(ruta_fotos, archivo)
            nombre = os.path.splitext(archivo)[0].capitalize()
            
            try:
                # Generar vector facial
                res = DeepFace.represent(img_path=path, model_name="Facenet")[0]
                
                # Actualizamos solo el embedding y la ruta, SIN tocar la descripcion que ya pusiste
                col.update_one(
                    {"nombre": nombre}, 
                    {"$set": {
                        "embedding": res["embedding"],
                        "ruta_foto": path
                    }}, 
                    upsert=True
                )
                print(f"✅ Embedding actualizado para: {nombre}")
                
            except Exception as e:
                print(f"❌ Error en {archivo}: {e}")

if __name__ == "__main__":
    registrar()