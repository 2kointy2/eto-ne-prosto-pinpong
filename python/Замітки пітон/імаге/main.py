import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
# from PyQt5 import uic
from main import Ui_MainWindow
from PyQt5.QtGui import QIcon

import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt  # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка

from PIL import Image
from PIL.ImageQt import ImageQt  # Для перенесення графіки з Pillow до QT
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
    GaussianBlur, UnsharpMask
)
workdir = ''


def filter(files, extensions):
    # створення порожнього списку, куди ми будемо додавати файли, які нам підходять
    result = []
    # прохід по цьому списку
    for f in files:
        # прохід по списку дозволених розширень
        for e in extensions:
            # перевірка на те, чи закінчується поточний файл на розширення
            if f.endswith(e):
                # додавання поточного файлу у список графічних файлів
                result.append(f)
    # повернення списку графічних файлів
    return result


def chooseWorkdir():
    # робимо workdir глобальною змінною
    global workdir
    # викликаємо вікно з вибором папки, передаємо результат у змінну workdir
    workdir = QFileDialog.getExistingDirectory()


class ImageProcessor():
    def __init__(self):
        ...

    def load_image(self, filename):
        ...

    def save_image(self):
        ...

    def do_bw(self):
        self.image = self.image.convert('L')  # робимо картинку чб
        self.save_image()  # зберігаємо картикну
        image_path = os.path.join(workdir, self.save_dir, self.filename)  # генеруємо шлях, до тільки що збереженої картинки
        ex.show_image(image_path)  # показуємо картинку на екрані

    def do_flip(self):
        ...

    def do_sharp(self):
        ...

    def do_rotate(self):
        self.image = self.image.transpose(Image.ROTATE_90)  # робимо картинку чб
        self.save_image()  # зберігаємо картикну
        image_path = os.path.join(workdir, self.save_dir,
                                  self.filename)  # генеруємо шлях, до тільки що збереженої картинки
        ex.show_image(image_path)  # показуємо картинку на екрані

    def do_rotate2(self):
        ...

    def do_blur(self):
        ...

workimage = ImageProcessor()

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(workimage.do_bw)
        self.ui.pushButton_3.clicked.connect(workimage.do_rotate)


    def show_choosen_image(self):
        ...

    def showImage(self, path):
        lable_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.heigh()
        pixmapimage = pixmapimage.scarlet(w, h, Qt.keepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

        ...

app = QApplication(sys.argv)
ex = Widget()
ex.show()

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp'] # створення списку валідних розширень
    chooseWorkdir() # виклик функції для отримання шляху до папки
    filenames = filter(os.listdir(workdir), extensions) # виклик функції для фільтрації. Виклик функції для отримання списку всіх файлів в папці

    ex.ui.label.clear() # очищення cписку
    for files in filenames: # перебираємо всі дозволені файли
        ex.ui.label.addItem(files) # додаємо всі відібрані файли

ex.ui.pushButton.clicked.connect(showFilenamesList)

sys.exit(app.exec_())