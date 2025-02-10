from PIL import Image

# Загружаем основное изображение
background = Image.open("1v0h0.jpg")

# Загружаем изображение с прозрачностью (PNG)
foreground = Image.open("overlay.png").convert("RGBA")

# Получаем размеры основного изображения
width, height = background.size

# Накладываем foreground на background
background.paste(foreground, (250, 150), foreground)

# Сохраняем результирующее изображение
background.save("result.jpg")
