import cv2
import numpy as np

my_scan = cv2.imread(r'.\image_to_process\photo_2023-12-14_13-55-59.jpg')
#зададим порог
thresh = 150
image = my_scan

# конвертировать входное изображение в Цветовое пространство в оттенках серого
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# изменить тип данных
# установка 32-битной плавающей запятой
operatedImage = np.float32(operatedImage)

# применить метод cv2.cornerHarris
# для определения углов с соответствующими
# значения в качестве входных параметров
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Результаты отмечены через расширенные углы
dest = cv2.dilate(dest, None)

# Возвращаясь к исходному изображению,
# с оптимальным пороговым значением
image[dest > 0.01 * dest.max()] = [0, 0, 255]

# окно с выводимым изображением с углами
cv2.imshow('Image with Borders', image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()