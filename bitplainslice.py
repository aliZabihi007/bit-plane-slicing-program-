import numpy as np
import cv2
import time

# read image
img = cv2.imread("barbara.png", cv2.IMREAD_GRAYSCALE)
row, col = img.shape
imagrezult = []
# char for code text
dic = {"a": '000000', "b": '000001', "c": '000010', "d": '000011', "e": '000100', "f": '000101', "g": '000110',
       "h": '000111', "i": '001000'
    , "j": '001001', "k": '001010', "l": '001011', "m": '001100', "n": '001101', "o": '001110', "p": '001111',
       "q": '010000', "r": '010001'
    , "s": '010010', "t": '010011', "u": '010100', "v": '010101', "w": '010110', "x": '010111', "y": '011000',
       "z": '011001', " ": '011010'}

dic2 = {"000000": 'a', "000001": 'b', "000010": 'c', "000011": 'd', "000100": 'e', "000101": 'f', "000110": 'g',
        "000111": 'h', "001000": 'i'
    , "001001": 'j', "001010": 'k', "001011": 'l', "001100": 'm', "001101": 'n', "001110": 'o', "001111": 'p',
        "010000": 'q', "010001": 'r'
    , "010010": 's', "010011": 't', "010100": 'u', "010101": 'v', "010110": 'w', "010111": 'x', "011000": 'y',
        "011001": 'z', "011010": ' '}


# convert image to  bit
def binaryconvt(img):
    list = []
    for i in range(row):
        for j in range(col):
            list.append(np.binary_repr(img[i][j], width=8))
    return list


# separate bit form image
def bitplanechar(bitimgval, img1D):
    bitList = [i[bitimgval] for i in img1D]
    return bitList


# read text from file
def gettext(file):
    text = ""
    f = open(file, "r")
    for x in f:
        text += x
    return text


# insert data in image
def runfunction(text1):
    conbit = 0
    print(bit1[0])
    for x in text1:
        if (x in dic):
            txt = dic[x]

            bit1[conbit] = txt[0]
            bit2[conbit] = txt[1]

            bit1[conbit + 1] = txt[2]
            bit2[conbit + 1] = txt[3]

            bit1[conbit + 2] = txt[4]
            bit2[conbit + 2] = txt[5]

        conbit += 3
    print(bit1[0:15])


# convert bit to intensity
def result():
    for i in range(0, len(bit2), 1):
        imagrezult.append(
            (int(bit8[i]) * 128) + (int(bit7[i]) * 64) + (int(bit6[i]) * 32) + (int(bit5[i]) * 16) + (
                    int(bit4[i]) * 8) + (int(bit3[i]) * 4) + (
                    int(bit2[i]) * 2) + (int(bit1[i]) * 1))

    return imagrezult


# extract text from  image
def extracttext(imgenter):
    select = ""
    mytext = ""
    imgebit = binaryconvt(imgenter)
    bit2 = np.array(bitplanechar(6, imgebit))
    bit1 = np.array(bitplanechar(7, imgebit))
    for i in range(0, len(bit1), 3):
        if (i + 2 < len(bit2)):
            select = select + str(bit1[i]) + str(bit2[i]) + str(bit1[i + 1]) + str(bit2[i + 1]) + str(
                bit1[i + 2]) + str(
                bit2[i + 2])
            if (select in dic2):
                print(select)
                mytext = mytext + str(dic2[select])
            select = ""
    print(mytext)


im1 = binaryconvt(img)
# bit of image
bit8 = np.array(bitplanechar(0, im1))
bit7 = np.array(bitplanechar(1, im1))

bit6 = np.array(bitplanechar(2, im1))
bit5 = np.array(bitplanechar(3, im1))

bit4 = np.array(bitplanechar(4, im1))
bit3 = np.array(bitplanechar(5, im1))
bit2 = np.array(bitplanechar(6, im1))
bit1 = np.array(bitplanechar(7, im1))

text = gettext("demofile.txt")
runfunction(text)
image2 = result()

image2 = np.reshape(image2, (row, col))
# create image outer
cv2.imwrite("rezult.png", image2)
# read  outer image
img2 = cv2.imread("rezult.png", cv2.IMREAD_GRAYSCALE)

row, col = img.shape
extracttext(img2)

# cv2.destroyAllWindows()
