from deepface import DeepFace
from pymongo import MongoClient
import cv2
import numpy as np

# Conexión
client = MongoClient("mongodb://localhost:27017/")
db = client["ReconocimientoFacial"]
col = db["estudiantes"]

def reconocer():
    print("🔍 Cargando datos desde MongoDB...")
    # Traemos todos los documentos (incluyendo tus descripciones nuevas)
    estudiantes = list(col.find()) 
    
    cap = cv2.VideoCapture(0)
    print("📸 Cámara lista. Presiona ESC para salir.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        try:
            # Usamos el detector de OpenCV por ser el más rápido para video
            results = DeepFace.represent(frame, model_name="Facenet", 
                                       enforce_detection=False, 
                                       detector_backend="opencv")

            for face in results:
                area = face["facial_area"]
                x, y, w, h = area["x"], area["y"], area["w"], area["h"]
                emb_actual = face["embedding"]

                mejor_match = None
                min_dist = 999

                # Comparar con los datos de Mongo
                for e in estudiantes:
                    # Buscamos el vector (puede llamarse embedding o encoding)
                    db_vec = e.get("embedding") or e.get("encoding")
                    
                    if db_vec:
                        dist = np.linalg.norm(np.array(db_vec) - np.array(emb_actual))
                        if dist < min_dist:
                            min_dist = dist
                            mejor_match = e

                # Umbral: si la distancia es menor a 10, es un match positivo
                if mejor_match and min_dist < 10:
                    color = (0, 255, 0) # Verde
                    nombre = mejor_match.get("nombre", "Sin Nombre")
                    codigo = mejor_match.get("codigo_utpl", "S/C")
                    # AQUÍ SE LEE TU DESCRIPCIÓN DE MONGO:
                    desc = mejor_match.get("descripcion", "Estudiante UTPL")
                    
                    txt_1 = f"{nombre} - {codigo}"
                    txt_2 = desc
                else:
                    color = (0, 0, 255) # Rojo
                    txt_1 = "Desconocido"
                    txt_2 = "No registrado en sistema"

                # Dibujar en pantalla
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                # Nombre y código
                cv2.putText(frame, txt_1, (x, y - 35), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                # Tu descripción personalizada
                cv2.putText(frame, txt_2, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        except: pass

        cv2.imshow("Sistema de Seguridad UTPL", frame)
        if cv2.waitKey(1) & 0xFF == 27: break # ESC para salir

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    reconocer()