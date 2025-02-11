# PMP-Face-eye-tracking
Progetto di "Principi e modelli della percezione", inerente a Face and eye tracking
Face Detection & Eye Tracking
N.B.: Tutti i comandi terminale indicati sono pensati per Ubuntu, se non diversamente specificato.

Questo progetto utilizza OpenCV, dlib e face_recognition per rilevare i volti e monitorare la direzione dello sguardo attraverso l'eye tracking.

## Prerequisiti
Prima di eseguire il codice, assicurati di avere installati i seguenti pacchetti e strumenti:

### 0. Installare il sistema python compatibile con il proprio OS e averlo aggiornato alla ultima versione (3.10 al tempo della creazione dello script)
Richiede anche i seguenti pacchetti/librerie: build-essential, cmake, libgtk-3-dev, liblapack-dev, libx11-dev, python3-dev.
Installabili con un solo comando: sudo apt install build-essential cmake libgtk-3-dev liblapack-dev libx11-dev python3-dev
Installare anche il pacchetto pip: sudo apt install python3-pip

### 1. Installare i pacchetti necessari
Il codice utilizza le seguenti librerie Python: opencv-python, dlib, face-recognition, numpy.
Si possono installare con il seguente comando: pip install opencv-python dlib face-recognition numpy.
(si possono anche installare uno alla volta)

### 2. File dei landmark facciali
Il codice richiede il file `shape_predictor_68_face_landmarks.dat`, necessario per il rilevamento dei punti di riferimento facciali.
Il file è scaricabile da: (http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Dopo averlo scaricato, va estratto e si consiglia di posizionarlo nella stessa directory del tuo script (qualora si preferisce averlo da altre parti, bisogna modificare lo script python aggiustando il percoso).

Si può anche scaricare da terminale col seguente comando: wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
Ed estrarlo con: bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

### 3. Assicurarsi che la webcam funzioni
Il codice utilizza la webcam per catturare i frame. Assicurati che il tuo dispositivo abbia una webcam funzionante e che i driver siano correttamente installati.

## Esecuzione del codice
Dopo aver installato i prerequisiti, puoi eseguire il codice con: python Face_eye_tracking.py , o in alternativa: python3 Face_eye_tracking.py

### Possibili problemi HW:
Se incontri problemi con la webcam, prova ad avviare lo script con i permessi di amministratore:
sudo python Face_eye_tracking.py  # Su Linux/macOS
python Face_eye_tracking.py       # Su Windows (da terminale con privilegi di amministratore)

### Risoluzione dei problemi con il codice:

- **Errore: `ImportError: No module named cv2`**
  - Assicurati di aver installato OpenCV con `pip install opencv-python`.

- **Errore: `RuntimeError: Unable to open shape_predictor_68_face_landmarks.dat`**
  - Controlla che il file `shape_predictor_68_face_landmarks.dat` sia nella directory corretta.

- **Errore: `VideoCapture(0) non si apre`**
  - Verifica che la tua webcam funzioni correttamente e che non sia utilizzata da un'altra applicazione.

# Test.py
Questo è un semplice programma python per verificare la corretta installazione e importazione delle librerie.
Una volta eseguito, importa e, se l'importazione ha esito positivo, stampa la versione delle librerie importate. Se tutto ha successo, stampa un messaggio di conferma.
Utile prima di avviare il programma completo.
