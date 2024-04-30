import os
import pygame
import sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

print(os.getcwd())

WINDOWSIZEX = 640
WINDOWSIZEY = 480

BOUNDRYINC = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False  # Save the image to disk or not
MODEL = load_model("bestmodel.h5")  # Model file name
LABELS = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three",
    4: "Four", 5: "Five", 6: "Left", 7: "Right",
    8: "Four", 9: "Nine"
}

# Initialize pygame
pygame.init()

# Load font
# FONT = pygame.font.Font("freesansbold.ttf", 18)

DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("Pygame and OpenCV")

iswriting = False
number_xcord = []
number_ycord = []

image_cnt = 1
PREDICT = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4, 0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)

        if event.type == pygame.MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == pygame.MOUSEBUTTONUP:
            iswriting = False
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)

            rect_min_x, rect_max_x = max(number_xcord[0] - BOUNDRYINC, 0), min(WINDOWSIZEX, number_xcord[-1] + BOUNDRYINC)
            rect_min_y, rect_max_y = max(number_ycord[0] - BOUNDRYINC, 0), min(WINDOWSIZEY, number_ycord[-1] + BOUNDRYINC)

            number_xcord = []
            number_ycord = []

            img_arr = np.array(pygame.surfarray.array3d(DISPLAYSURF))
            img_arr = img_arr[rect_min_y:rect_max_y, rect_min_x:rect_max_x].astype(np.float32)
            img_arr = cv2.resize(img_arr, (28, 28))
            img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
            img_arr = np.expand_dims(img_arr, axis=0)
            img_arr = np.expand_dims(img_arr, axis=3)
            img_arr = img_arr / 255.0

            if IMAGESAVE:
                cv2.imwrite(f"image{image_cnt}.png", img_arr[0])
                image_cnt += 1

            if PREDICT:
                prediction = MODEL.predict(img_arr.reshape(1, 28, 28, 1))
                label = LABELS[np.argmax(prediction)]

                # Render text
                # textSurface = FONT.render(label, True, RED)
                # textRectObj = textSurface.get_rect()
                # textRectObj.left, textRectObj.bottom = rect_min_x, rect_max_y
                # DISPLAYSURF.blit(textSurface, textRectObj)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                DISPLAYSURF.fill(BLACK)

    pygame.display.update()
