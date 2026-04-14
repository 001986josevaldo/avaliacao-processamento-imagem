import cv2
import numpy as np

# Criar uma imagem "autoral" (simples com texto)
img = np.zeros((400, 600, 3), dtype=np.uint8)

# Desenhar algo na imagem
cv2.putText(img, 'Teste OpenCV', (50, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostrar imagem
cv2.imshow('Imagem em Tons de Cinza', gray)

# Esperar tecla para fechar
cv2.waitKey(0)
cv2.destroyAllWindows()