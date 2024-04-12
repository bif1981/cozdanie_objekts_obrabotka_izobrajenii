# Домашнее задание по теме "Создание объектов, обработка изображений"
#
# Цель задания:
#
# Закрепить знания о координатной плоскости, работе с геометрическими примитивами и цветами библиотеки OpenCV.
#
# Задание:
#
# Нужно нарисовать упрощённый вариант логотипа университета Urban (да простят нас дизайнеры и Midjorney).
#
# Используя геометрические примитивы из библиотеки OpenCV, нужно отрисовать следующий рисунок:
#
# Создайте матрицу (картинку) при помощи NumPy в виде квадрата произвольного размера.
# Отрисуйте картинку используя примитивы circle, ellipse, line и др.
# Цвета должны совпадать с картинкой или хотя бы быть того же оттенка
# Приветствуются дополнительные элементы, так вы лучше отточите навык определения координат.
#
# Доп. задание:
# Попробуйте сделать фон - градиент (можно цветной):
#
#
# Файл с кодом отрисовки прикрепите к домашнему заданию.

import cv2
import numpy as np

photo = np.zeros((440, 445, 3), dtype='uint8')

# RGB - стандарт
# BGR - формат в OpenCV
# google/color picker - выбор цвета

photo[:] = 255, 0, 255

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 170, (255, 255 ,255), thickness=5)

# 2 горизонтальные красные линии
cv2.line(photo, (170, 175), (200, 175), (0,0,255), thickness=3)
cv2.line(photo, (250, 175), (280, 175), (0,0,255), thickness=3)

# 4 вертикальные синии линии
cv2.line(photo, (170, 175), (170, 225), (255,0,0), thickness=3)
cv2.line(photo, (200, 175), (200, 225), (255,0,0), thickness=3)
cv2.line(photo, (250, 175), (250, 225), (255,0,0), thickness=3)
cv2.line(photo, (280, 175), (280, 225), (255,0,0), thickness=3)

# 2 зеленые дуги эллипса
cv2.ellipse(photo, (225, 225), (25, 30), 0, 0, 180, (0,255,0), thickness=3)
cv2.ellipse(photo, (225, 225), (55, 60), 0, 0, 180, (0,255,0), thickness=3)

cv2.imshow('U Letter', photo)
cv2.waitKey(0)



