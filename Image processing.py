import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

def img_input():
    print('Enter the name of the image (extension included): ')
    img_name = input()

    return img_name
def reflect(img, direction):
    img_arr=np.array(img)
    if direction == 1:
        horizontal=img_arr[:, ::-1, :]
        return horizontal

    elif direction == 2:
        vertical= img_arr[::-1]
        return vertical

def translate(img, x, y):
    img = np.array(img)
    h, w, _ = img.shape
    translation= np.full((h + abs(y), w + abs(x), 3),255, dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            a = np.dot([[1, 0, x], [0, 1, y]], [[j], [i], [1]])
            new_i = int(a[1][0])
            new_j = int(a[0][0])
            if 0 <= new_i < h + abs(y) and 0 <= new_j < w + abs(x):
                translation[new_i, new_j, :] = img[i, j, :]

    return translation

def scaling(img,c):
    img = np.array(img)
    h, w, _ = img.shape

    new_width = int(w*c)
    new_height = int(h*c)
    result = cv2.resize(img
                        , (new_width, new_height))

    return result
def rotation(img):
    angle=float(input("Enter rotation angle : "))
    img_arr = np.array(img)
    rows, cols = img_arr.shape[:2]
    rotation_m = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    img_rotation = cv2.warpAffine(img_arr, rotation_m, (cols, rows),borderValue=(255, 255, 255))

    return img_rotation

def composite(img, direction, c):
    reflected_img = reflect(img, direction)
    transformed_img = scaling(reflected_img,c)
    return transformed_img


def display(original_img, result_img,z,proc):
    w=15
    h=10
    original_imgarr = np.array(original_img)
    _, pics = plt.subplots(1, 2, figsize=(w,h))

    pics[0].axis("off")
    pics[0].set_title("Original image")
    pics[0].imshow(original_img)

    pics[1].axis("off")
    pics[1].set_title(f"{proc} image")
    pics[1].imshow(result_img)

    if z==1:
        pics[1].set_xlim(0, original_imgarr.shape[1])
        pics[1].set_ylim(original_imgarr.shape[0], 0)

    plt.show()

def menu():
    print("-----------------Menu-----------------")
    print("1. Reflect Image (vertically and horizontally)")
    print("2. Translate Image")
    print("3. Scale Image")
    print("4. Rotate Image")
    print("5. Composite Image")
    print("0. Exit Menu")

    print("Enter your choice: ")
    choice = int(input())

    while choice < 0 or choice > 6 :
        print("Enter correct choice :")
        choice = int(input())

    return choice

def main():
    z=1
    img_name = img_input()

    img = Image.open(img_name)
    img_arr = np.array(img)
    while z:


        choice = menu()
        if choice == 1 or choice == 5:
            print("1. Horizontal Reflection")
            print("2. Vertical Reflection")
            direction=int(input())
            while direction < 1 or direction >2:
                direction=int(input("Enter a correct choice : "))
        if choice == 6:
            print
        match choice:

            case 1:
                if direction == 1:
                    proc='Horizontally Reflected'
                else :
                    proc='Vertically Reflected'
                display(img, reflect(img,direction),0,proc)

            case 2:
                proc='Translated'
                x=int(input("Enter translation value in x direction : "))
                y=int(input("Enter translation value in y direction : "))
                display(img,translate(img,x,y),1,proc)

            case 3:
                c = float(input("Enter scaling factor :"))
                while c <= 0:
                    c = float(input("Enter scaling factor greater than 0 :"))
                if c<1:
                    proc = 'Scaled Down'
                else:
                    proc='Scaled Up'
                display(img,scaling(img,c),0,proc)

            case 4:
                proc='Rotated'
                display(img,rotation(img),0,proc)

            case 5:
                proc='Composite'
                c = float(input("Enter scaling factor :"))
                while c <= 0:
                    c = float(input("Enter scaling factor greater than 0 :"))
                display(img,composite(img,direction,c),1,proc)

        choice_2=int(input("Do you want another transformation?\n1. Yes\n2. No\n "))

        while choice_2 < 1 or choice_2 >2 :
            choice_2=int(input("Enter correct value: "))
        if choice_2==2:
            z=0
        else:
            z=1

if __name__ == '__main__':
    main()





