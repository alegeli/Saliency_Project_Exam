import cv2  # OpenCV per l'estrazione dei pattern visivi
import numpy as np # NumPy per la gestione dei pixel come dati matriciali

def analizza_ads(percorso, etichetta):
    # CARICAMENTO: Lettura di dati non strutturati (Immagini)
    img = cv2.imread(percorso)
    if img is None:
        print(f"Errore: non trovo {percorso}")
        return

    # PRE-PROCESSING: Conversione in scala di grigi per il Denoising
    # Riduce il rumore cromatico per far emergere il segnale informativo
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # PATTERN EXTRACTION: Gradiente di Sobel (Algoritmo di Canny)
    # Calcola le variazioni di intensità luminosa per trovare i bordi
    edges = cv2.Canny(gray, 100, 200)
    
    # KNOWLEDGE PRESENTATION: Generazione Mappa di Salienza
    # Un filtro Gaussian Blur simula la distribuzione dell'attenzione umana
    saliency_map = cv2.GaussianBlur(edges, (21, 21), 0)

    # Visualizzazione dei risultati
    cv2.imshow(f"ORIGINALE - {etichetta}", img)
    cv2.imshow(f"MAPPA DI SALIENZA - {etichetta}", saliency_map)

# ESECUZIONE COMPARATIVA (A/B Testing)
print("TEST A: Analisi Brand Efficace (New Balance)...")
analizza_ads("foto.jpg", "NB 550 (SUCCESS)")
cv2.waitKey(0) # Attesa interazione utente

print("TEST B: Analisi Brand con Rumore (Jordan 4)...")
analizza_ads("foto_noise.jpg", "JORDAN (NOISE)")
cv2.waitKey(0)

cv2.destroyAllWindows()
