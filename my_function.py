# Импорт библиотек
import cv2
from pyzbar.pyzbar import decode


# Создание метода для декодирования штрих-кода
def BarcodeReader(image):
    # Считывание изображения в массиве numpy, используя cv2
    img = cv2.imread(image)

    # Декодирование штрих кода
    detectedBarcodes = decode(img)

    # Проверка корректности чтения штрих кодов
    if len(detectedBarcodes) == 2:
        if len(detectedBarcodes[1][0].decode('utf-8')) == 16:
            return f"Cерийный номер: {detectedBarcodes[0][0].decode('utf-8')}\n"\
                   f"MAC: {detectedBarcodes[1][0].decode('utf-8')}"
        else:
            return f"Cерийный номер: {detectedBarcodes[1][0].decode('utf-8')}\n" \
                   f"MAC: {detectedBarcodes[0][0].decode('utf-8')}"
    else:
        return f"Загрузите фотографию заново пожалуйста, штрих коды не считались!"
