import cv2
import tkinter
from PIL import Image, ImageTk

img_path = 'img\\Lenna.png'
img=cv2.imread(img_path) # 이미지 읽기
# 수정용 이미지
imgfix = img.copy() # 원본 이미지를 수정하지 않도록 복사본 생성

if img is None:# 이미지가 없으면 종료
    print("이미지를 찾을 수 없습니다. 경로를 확인하세요.")
    exit()# 이미지가 없을 경우 프로그램 종료

drawing=False # 마우스 왼쪽 버튼이 눌렸는지 여부
ix,iy=-1,-1 # 마우스 클릭 좌표 초기화

# 마우스 이벤트 콜백 함수
def draw_line(event,x,y,flags,param):
    global ix,iy,drawing # 전역 변수 사용
    
    # 마우스 왼쪽 버튼이 눌렸을 때
    if event ==cv2.EVENT_LBUTTONUP:
        drawing=True
        ix,iy=x,y # 마우스 왼쪽 버튼을 떼면 좌표 저장
        
    # 마우스를 이동 할때
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(imgfix,(ix,iy),(x,y),(0,0,0),thickness=2) # 마우스 이동 중 선 그리기(thickness=2 선 두께)
            # (ix,iy) 는 이전 좌표, (x,y)는 현재 좌표(0,0,0)은 선 색상(BGR 형식)(검은색)
            ix,iy=x,y # 현재 좌표를 이전 좌표로 업데이트

    # 마우스를 버튼 업 했을 때
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False # 마우스 왼쪽 버튼을 누르면 그리기 중지
        # cv2.line(img,(ix,iy),(x,y),(0,0,0),thickness=2) # 마지막 선 그리기



def on_button_click_draw():
    cv2.namedWindow('image') # 이미지 창 생성

    # 마우스 이벤트가 발생할때 마다 함수 실행
    cv2.setMouseCallback('image', draw_line) # 마우스 이벤트 콜백 함수 설정
    while True: # 종료할때 까지 반복
        gray_img = cv2.cvtColor(imgfix, cv2.COLOR_BGR2GRAY) # 이미지를 그레이스케일로 변환
        cv2.imshow('image', gray_img) # 이미지 창에 이미지 표시

        # 창이 닫히거나 ESC 키를 누르면 종료 창수를 확인 
        if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1: # 창이 닫혔는지 확인
            break
        # esc 라는 ascII 코드(27)를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27: # ESC 키를 누르면 종료
            break

def on_button_click_contours():
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 윤곽선 찾기
    edges = cv2.Canny(gray_img, 100, 200)# 윤곽선 찾기(이미지, 낮은 임계값, 높은 임계값)
    cv2.imshow('윤곽선 창', edges)
    
window=tkinter.Tk()
window.title("tkinter 창")
window.geometry("800x800")
# 기존 opencv는 BGR 형식으로 이미지를 읽기 때문에 RGB로 변환
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR
ima1=Image.fromarray(img_rgb) # 이미지를 PIL 이미지로 변환
imtk=ImageTk.PhotoImage(ima1) # PIL 이미지를 ImageTk 객체로 변환
label = tkinter.Label(window, image=imtk) # ImageTk 객체를 라벨에 설정'
label.pack() # 라벨에 이미지 표시
button = tkinter.Button(window, text="그리기 시작", command=on_button_click_draw)
button.pack(pady=20) # 버튼 클릭 시 on_button_click 함수 호출
# 윤곽선 보기 버튼 추가
button2 = tkinter.Button(window, text="윤곽선 보기", command=on_button_click_contours)
button2.pack(pady=20) # 윤곽선 보기 버튼 클릭 시 on_button_click 함수 호출
window.mainloop() # tkinter 이벤트 루프 시작


cv2.destroyAllWindows() # 모든 창 닫기