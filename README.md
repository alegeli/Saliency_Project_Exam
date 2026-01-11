Saliency Detection Brands ADS: Signal vs Noise Analysis
Progetto di Data Mining focalizzato sull'estrazione di conoscenza da dati non strutturati (immagini pubblicitarie) attraverso tecniche di visione artificiale e analisi della salienza visiva.

📌 Obiettivi del Progetto
L'analisi mira a valutare l'efficacia comunicativa di diverse campagne pubblicitarie identificando i pattern di attenzione spontanea. Il software segue il processo KDD (Knowledge Discovery from Data) per trasformare i pixel grezzi in insight strategici per la Business Intelligence.

📊 Data Discrimination: Successo vs Rumore
Il progetto mette a confronto due classi di dati per dimostrare la capacità diagnostica dell'algoritmo:

TEST A - Signal (Successo): Immagine New Balance 550. Caratterizzata da un alto contrasto e una chiara gerarchia visiva. Il "Segnale" (il brand) emerge nettamente dal fondo.

TEST B - Noise (Insuccesso): Immagine Jordan 4 Off-White. Presenta un alto livello di rumore visivo dovuto alla complessità del paesaggio e al basso contrasto cromatico tra prodotto e ambiente. In questo caso, l'immagine è classificata come un Outlier di marketing.

🛠 Metodologia Tecnica
Pre-processing: Conversione in scala di grigi per effettuare l'Image Denoising.

Pattern Extraction: Utilizzo del gradiente di Sobel (tramite Canny/OpenCV) per identificare i bordi e i cambiamenti di intensità luminosa.

Explainable AI (XAI): L'approccio utilizzato è trasparente e matematicamente verificabile, evitando l'effetto "black box" dei sistemi di deep learning non strutturati.

🚀 Requisiti e Installazione
Il progetto è sviluppato in Python e richiede le seguenti librerie:

Bash

pip install opencv-python numpy
💻 Esecuzione
Per avviare l'analisi comparativa, posizionare i file foto.jpg e foto_noise.jpg nella root del progetto ed eseguire:

Bash

python3 main.py
