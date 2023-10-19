# Импорт библиотек
import cv2
from pyzbar.pyzbar import decode


# Создание метода для декодирования штрих-кода
def BarcodeReader(image):
    # Считывание изображения в массиве numpy, используя cv2
    img = cv2.imread(image)
    result = []
    # Декодирование штрих кода
    detectedBarcodes = decode(img)

    if len(detectedBarcodes) == 2 and (len(detectedBarcodes[1][0].decode('utf-8')) == 16 or len(detectedBarcodes[0][0].decode('utf-8')) == 16):
        if len(detectedBarcodes[1][0].decode('utf-8')) == 16:
            return f"Cерийный номер: <code>{detectedBarcodes[0][0].decode('utf-8')} </code>\n"\
                   f"MAC: <code> {detectedBarcodes[1][0].decode('utf-8')} </code>"
        else:
            return f"Cерийный номер: <code>{detectedBarcodes[1][0].decode('utf-8')}</code>\n" \
                   f"MAC:<code> {detectedBarcodes[0][0].decode('utf-8')}</code>"
    elif len(detectedBarcodes) == 1 and len(detectedBarcodes[0][0]) == 18:
        return f"ICCID: <code>{detectedBarcodes[0][0].decode('utf-8')}</code>\n"
    elif len(detectedBarcodes) == 3:
        return f"<code>{detectedBarcodes[0][0].decode('utf-8')}</code>\n" \
               f"<code> {detectedBarcodes[1][0].decode('utf-8')}</code>\n" \
               f"<code> {detectedBarcodes[2][0].decode('utf-8')}</code>"
    elif len(detectedBarcodes) == 2:
        return f"<code>{detectedBarcodes[0][0].decode('utf-8')}</code>\n" \
               f"<code> {detectedBarcodes[1][0].decode('utf-8')}</code>"
    elif len(detectedBarcodes) == 1:
        return f"<code>{detectedBarcodes[0][0].decode('utf-8')}</code>\n"



