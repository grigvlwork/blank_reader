# Вот пример кода на Python для поиска чёрных квадратов размером 20–50 пикселей на изображении и сохранения их
# координат в списке:
# Этот код загружает изображение, применяет маску для поиска чёрных квадратов размером 20–50 пикселей, находит контуры
# найденных квадратов и сохраняет их координаты в списке.
import cv2
import numpy as np
from PIL import Image
from PyQt5.QtGui import QImage, QPixmap
import os
import sqlite3


def create_project_database(path:str)->bool:
    last_directory_name = os.path.basename(os.path.normpath(path))
    db_name = f"{path}/{last_directory_name}.db"
    conn = sqlite3.connect(db_name)
    try:
        cursor = conn.cursor()
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS project_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        return True

    except sqlite3.Error as e:
        return False

    finally:
        conn.close()


def pil2pixmap(image):
    if image.mode == "RGB":
        r, g, b = image.split()
        im = Image.merge("RGB", (b, g, r))
    elif image.mode == "RGBA":
        r, g, b, a = image.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif image.mode == "L":
        im = image.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


def squares_coord(file_name, min_size=10, max_size=100):
    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    result = []
    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)
            ratio = float(w) / h
            if 0.9 <= ratio <= 1.1:
                result.append([x1, y1, x1 + w, y1 + h])
    return result


if __name__ == '__main__':
    coordinates = squares_coord("image.jpg")
    print("Координаты чёрных квадратов:")
    for coordinate in coordinates:
        print(coordinate)
