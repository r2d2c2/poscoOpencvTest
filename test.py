import cv2
import tkinter
from PIL import Image, ImageTk

# print(cv2.__version__ )

img_path = 'img\\Lenna.png'
img=cv2.imread(img_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def on_button_click(state):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_img)

window=tkinter.Tk()
window.title("Image Viewer")
window.geometry("800x800")

imag=Image.fromarray(img_rgb) # RGB로 변환된 이미지를 PIL 이미지로 변환
imtk=ImageTk.PhotoImage(imag) # PIL 이미지를 ImageTk 객체로 변환
label = tkinter.Label(window, image=imtk) # ImageTk 객체를 라벨에 설정
label.pack() # 라벨에 이미지 표시

button = tkinter.Button(window, text="흑백으로", command=lambda: on_button_click('normal'))
button.pack(pady=20) # 버튼 클릭 시 on_button_click 함수 호출
window.mainloop() # tkinter 이벤트 루프 시작


cv2.waitKey(0)
cv2.destroyAllWindows()


