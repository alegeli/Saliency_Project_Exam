import cv2
import numpy as np

def analizza_attenzione():
    # Carica la foto
    img = cv2.imread("foto.jpg")
    if img is None:
        print("Errore: non trovo foto.jpg!")
        return

    # Trasforma in scala di grigi per l'analisi
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applica un filtro per evidenziare i bordi e il contrasto (Simula l'attenzione visiva)
    # Usiamo il filtro di Sobel per trovare i cambiamenti di intensità
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    mag = np.sqrt(sobelx**2 + sobely**2)
    
    # Rendi la mappa visibile (0-255)
    saliency_map = np.uint8(255 * mag / np.max(mag))

    # Mostra i risultati
    cv2.imshow("1. Immagine Originale", img)
    cv2.imshow("2. Analisi dell'Attenzione (Mappa)", saliency_map)
    
    print("Premi un tasto qualsiasi sulla foto per chiudere.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    analizza_attenzione()