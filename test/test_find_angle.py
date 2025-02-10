import cv2
from PIL import Image

# Загружаем изображение
img = cv2.imread('17v1h0.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Применяем фильтр Кэнни для выделения границ
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Находим контуры
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Ищем самый большой контур
max_area = 0
best_rect = None

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area
        best_rect = cv2.minAreaRect(cnt)

# Если нашли подходящий контур, определяем угол поворота
if best_rect is not None:
    angle = best_rect[-1]

    if angle < -45:
        angle += 90

    print(f"Угол поворота: {angle}")
else:
    print("Не удалось найти подходящий контур.")

image = Image.open('17v1h0.tif').rotate(angle)
image.save('rotated.tif')
