# Analisi della Salienza Visiva tramite Gradiente (Sobel)
Questo progetto utilizza tecniche di Computer Vision per identificare le aree di un'immagine che attirano maggiormente l'attenzione visiva, basandosi sul contrasto e sulla densità dei bordi.

## Descrizione del Progetto
L'algoritmo implementato in `main.py` utilizza l'operatore di Sobel per calcolare il gradiente dell'immagine. In termini di Business Intelligence e Marketing, questo permette di simulare dove l'occhio umano cade per primo (loghi, testi, contorni del prodotto), rendendolo uno strumento utile per l'analisi di materiali pubblicitari.

## Requisiti Tecnici
- Python 3.x
- OpenCV (`opencv-python`)
- Numpy

## Istruzioni per l'uso
1. Assicurarsi che l'immagine da analizzare sia nella cartella principale e rinominata in `foto.jpg`.
2. Eseguire il programma da terminale con:
   `python3 main.py`