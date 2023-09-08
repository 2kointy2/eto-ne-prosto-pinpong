from PIL import Image, ImageFilter

class ImageProcessor:
    def __init__(self):
        self.filename = None
        self.image = None
        self.changed = []
        
    # завантаження картинки, відкриття її в пайтоні
    def load_image(self, filename):
        self.filename =  filename  #  запам'ятувємо назву файлу
        self.image = Image.open(filename)  # відкриваємо картинку

    def save_image(self):
        self.image.save()  # зберігаємо картинку

    def do_bw(self):
        self.image = self.image.convert('L')  # робимо картинку чб
        self.save_image()  # зберігаємо картикну
        

