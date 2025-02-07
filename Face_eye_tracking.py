import cv2
import face_recognition
import dlib
import numpy as np

# Caricamento del rilevatore di landmark per l'eye tracking
predictor_path = "shape_predictor_68_face_landmarks.dat"
face_landmark_predictor = dlib.shape_predictor(predictor_path)

# Apre la webcam
video_capture = cv2.VideoCapture(0)

# Funzione per rilevare gli occhi e il loro stato
def detect_eye_direction(landmarks):
    # Coordinate degli occhi
    left_eye = landmarks[36:42]
    right_eye = landmarks[42:48]

    # Calcolo del centroide per ciascun occhio
    def get_eye_center(eye_points):
        return np.mean(eye_points, axis=0)

    left_eye_center = get_eye_center(left_eye)
    right_eye_center = get_eye_center(right_eye)

    # Verifica se gli occhi sono rivolti verso il centro dello schermo
    # Ottieni la risoluzione effettiva della webcam
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    threshold = 0.18  # Soglia di tolleranza        <-----------------------------------
    screen_center_x = int(frame_width)/2 # basato sulla risoluzione della webcam
    eyes_center_x = (left_eye_center[0] + right_eye_center[0]) / 2

    # Restituisce True se gli occhi sono centrati, False altrimenti
    return abs(eyes_center_x - screen_center_x) < threshold * screen_center_x

while True:
    # Cattura un frame dalla webcam
    ret, frame = video_capture.read()
    if not ret:
        break

    # Converti il frame in RGB
    rgb_frame = frame[:, :, ::-1]

    # Trova i volti nel frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Alert per più di un volto rilevato
    if len(face_locations) > 1:
        cv2.putText(frame, "Diversi volti rilevati!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Se non vengono rilevati volti
    if len(face_locations) == 0:
        cv2.putText(frame, "Nessun volto rilevato!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for face_location in face_locations:
        top, right, bottom, left = face_location

        # Disegna un rettangolo attorno al volto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, "Volto", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Crea un oggetto dlib.rectangle per il rilevamento dei landmark
        dlib_face = dlib.rectangle(left, top, right, bottom)
        landmarks = face_landmark_predictor(rgb_frame, dlib_face)
        landmarks_points = np.array([[p.x, p.y] for p in landmarks.parts()])

        # Disegna i landmark degli occhi
        for i in range(36, 48):
            x, y = landmarks_points[i]
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        cv2.putText(frame, "Occhi", (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


        # Controlla se lo studente guarda lo schermo
        if not detect_eye_direction(landmarks_points):
            cv2.putText(frame, "ATTENZIONE: Guardare lo schermo!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostra il frame
    cv2.imshow("Face Detection with Eye Tracking", frame)

    # Premi 'q' per uscire
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia la webcam e chiudi le finestre
video_capture.release()
cv2.destroyAllWindows()
