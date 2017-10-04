from PIL import Image
import pytesseract

def Main():
    for i in range(101):
        with Image.open('img/' + str(i) + '.jpg') as file:
            result = pytesseract.image_to_string(file)
            print(result)
            pass

    pass

def Demo():
    pass


if __name__ == '__main__':
    Main()
