# Analisi della Salienza Visiva tramite Gradiente (Sobel)

Questo progetto utilizza tecniche di Computer Vision per identificare le aree di un'immagine che attirano maggiormente l'attenzione visiva, basandosi sul contrasto e sulla densità dei bordi.

## Descrizione del Progetto
L'algoritmo implementato in `main.py` utilizza l'operatore di Sobel per calcolare il gradiente dell'immagine. In termini di Business Intelligence e Marketing, questo permette di simulare la foveazione umana e distinguere tra **Segnale** informativo e **Rumore** visivo.

Il sistema effettua una **Data Discrimination** tra due casi studio:
* **Success (NB 550)**: ADS con brand chiaro e saliente.
* **Noise (Jordan 4)**: ADS con alto rumore visivo e basso contrasto del prodotto.

## Requisiti Tecnici
- Python 3.x
- OpenCV (`opencv-python`)
- Numpy

## Istruzioni per l'uso
1. Assicurarsi che le immagini da analizzare siano nella cartella principale e rinominate in `foto.jpg` e `foto_noise.jpg`.
2. Eseguire il programma da terminale con:
   `python3 main.py`
