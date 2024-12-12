from tkinter import *
# 버튼 클릭 이벤트 함수
def button_click(value):
    """
    숫자 또는 연산자를 입력창에 추가하는 함수.
    :param value: 버튼 클릭 시의 값 (문자열)
    """
    current = ent.get() # 현재 입력창의 값을 가져오기
    ent.delete(0, END) # 입력창 초기화
    ent.insert(0,current + value) #기존 값에 클릭한 값을 추가하여 입력창에 다시 삽입
# "=" 버튼 클릭 시 계산 수행 입력창의 수식(eval을 사용) 결과를 계산하는 함수.
def nuen():
    try:
        result = eval(ent.get())
        ent.delete(0,END)
        ent.insert(0,str(result))
    except Exception as e :
       ent.delete(0,END)
       ent.insert(0,"수식을 입력해주세요")

# "C" 버튼 클릭 시 입력 초기화
def claer():
    ent.delete(0, END)
#백스페이스

def Backs():
    result = ent.get()
    ent.delete(len(result)-1,END)
    


win = Tk()
win.geometry("350x400")
win.title("계산기")

ent = Entry(
    win,#윈도우
    width= 45, #입력창 너비
    #fornt = ("돋움", 20), #입력창 폰트와 크기
    borderwidth = 5,
    justify=  "right"# 텍스트를 오른쪽 정렬
)
ent.grid(row=0, column=0,columnspan=4,padx=10,pady=10) #그리드 배치

Buttons = [
    'C', '<-', '%', '/', 
    '7', '8', '9', '*', 
    '4', '5', '6', '-', 
    '1', '2', '3', '+', 
    '+/-', '0','.', '='
]
row1 = 1
col1 = 0



for i in Buttons:
    if i == "=":
        btn = Button(win, text=i, width=5, height=2, command= nuen, font=("궁서", 16, "bold"), relief="raised", bg="#40FF00", fg="#000000")
    elif i == "C":
        btn = Button(win, text=i, width=5, height=2, command=claer, font=("돋움", 16, "bold"), relief="raised", bg="#3B0B0B", fg="#FFFFFF")
    elif i == "<-":
        btn = Button(win, text=i, width=5, height=2, command=Backs, font=("바탕", 20, "bold"), relief="raised", bg="#FFFF00", fg="#000000")
    else:
        btn = Button(win,text=i,width=5,height=2, command=lambda b = i: button_click(b), font=("돋움", 16, "bold"), relief="flat", bg="#848484", fg="#FFFFFF") #숫자 버튼
    btn.grid(row=row1, column = col1,padx=5,pady=5)
    col1 += 1
    if col1 > 3:
        col1 = 0
        row1 += 1
win.mainloop()

