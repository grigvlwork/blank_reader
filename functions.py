
# Вот пример кода на Python для поиска чёрных квадратов размером 20–50 пикселей на изображении и сохранения их
# координат в списке:
# Этот код загружает изображение, применяет маску для поиска чёрных квадратов размером 20–50 пикселей, находит контуры
# найденных квадратов и сохраняет их координаты в списке.
import cv2
import numpy as np

def squares_coord(file_name):
    # Загрузка изображения и преобразование его в оттенки серого
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Установка диапазонов поиска чёрных квадратов
    lower = np.array([0, 0, 0], np.uint8)
    upper = np.array([180, 10, 60], np.uint8)

    # Применение маски для поиска чёрных квадратов
    mask = cv2.inRange(gray, lower, upper)

    # Поиск контуров чёрных квадратов и сохранение координат в списке
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    coordinates = []
    for contour in contours:
       if cv2.contourArea(contour) > 2000:
           coordinates.append((contour))

    # Вывод списка координат чёрных квадратов
    return coordinates


coordinates = squares_coord("image.jpg")
print("Координаты чёрных квадратов:")
for coordinate in coordinates:
 print(coordinate)
