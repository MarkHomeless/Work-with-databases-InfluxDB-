import cv2 
import numpy as np
def detect_cloude(container, results):
    '''
    Function for recognizing clouds in an image 
    Gets an image from a shared resource processes it and packages the results in a container for results
        -container - shared resource 
        -results - list of results of function
    '''
    try:
        image = container.get()
    except:
        results.append(0)
    image = cv2.GaussianBlur(image, (7, 7), 0) #Сглаживание изображение гаусовским фильтром
    #viewImage(image)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Перевод в формат HSV
    #viewImage(hsv_img) 
    white_low = np.array([0,0,60] )
    white_high = np.array([145,80,255])
    white_mask = cv2.inRange(hsv_img, white_low, white_high)
    result_white = cv2.bitwise_and(image, image, mask=white_mask) #Выявление белого и серого цвета на изображении
    #viewImage(result_white)
    RGB_again = cv2.cvtColor(result_white, cv2.COLOR_HSV2RGB) #Перевод в формат RGB
    gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY) #Перевод в оттенки серого
    #viewImage(gray)
    ret, threshold = cv2.threshold(gray, 127, 255, 0) #Выделение оттенков облака
    #viewImage(threshold)
    contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #Получение контуров
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3) #Нанесение контуров на изображение
    #viewImage(image) 
    area_list = [cv2.contourArea(x) for x in contours] #Получение площади каждого контура
    results.append(sum(area_list)) #Занесение общей площади в список результатов
def viewImage(image):
    '''
    Displays image per screen
    '''
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()