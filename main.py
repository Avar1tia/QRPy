import cv2
from pyzbar import pyzbar

# Установка размера видео
width, height = 640, 480

# Путь к видеофайлу
video_path = "qr.mp4"

# Открываем видеофайл
video_capture = cv2.VideoCapture(video_path)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    # Считываем кадр из видеофайла
    ret, frame = video_capture.read()

    if not ret:
        break

    # Изменяем размер кадра
    frame = cv2.resize(frame, (width, height))

    # Переводим кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Поиск QR-кодов на кадре
    barcodes = pyzbar.decode(gray)

    # Обрабатываем найденные QR-коды
    for barcode in barcodes:
        #    Извлекаем данные из QR-кода
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Рисуем рамку вокруг QR-кода
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Выводим данные QR-кода
        cv2.putText(frame, f"QR", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
        2)

        # Выводим данные QR-кода в терминал
        print(f"QR Code: {barcode_data}, Type: {barcode_type}")

    # Показываем кадр с видео
    cv2.imshow("Video", frame)

    # Проверяем нажатие клавиши 'q' для выхода из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
video_capture.release()
cv2.destroyAllWindows()

