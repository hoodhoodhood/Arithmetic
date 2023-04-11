import tkinter as tk

# 계산기 클래스 정의
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("계산기")

        # 계산식을 표시할 엔트리 위젯 생성
        self.expression = tk.StringVar()
        self.expression.set("")
        self.entry = tk.Entry(self.window, textvariable=self.expression, font=("Helvetica", 20), justify="right", width=20, relief="groove", borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 버튼 위젯 생성
        buttons = [
            ['7', 1, 0], ['8', 1, 1], ['9', 1, 2], ['/', 1, 3],
            ['4', 2, 0], ['5', 2, 1], ['6', 2, 2], ['*', 2, 3],
            ['1', 3, 0], ['2', 3, 1], ['3', 3, 2], ['-', 3, 3],
            ['0', 4, 0], ['.', 4, 1], ['=', 4, 2], ['+', 4, 3],
            ['C', 5, 0, 2, 1],  # 리셋 버튼 추가
        ]

        # 버튼 생성 및 이벤트 처리 함수 연결
        for button in buttons:
            text = button[0]
            row = button[1]
            column = button[2]
            colspan = button[3] if len(button) > 3 else 1
            tk.Button(self.window, text=text, font=("Helvetica", 20), command=lambda text=text: self.on_button_click(text), width=5, height=2, relief="groove", borderwidth=3).grid(row=row, column=column, columnspan=colspan, padx=5, pady=5)

    # 버튼 클릭 이벤트 처리 함수
    def on_button_click(self, text):
        current_expression = self.expression.get()
        if text == '=':
            try:
                result = eval(current_expression)
                self.expression.set(result)
            except ZeroDivisionError:
                self.expression.set("Error")
        elif text == 'C':  # 리셋 버튼 처리
            self.expression.set("")
        else:
            self.expression.set(current_expression + text)

# 계산기 인스턴스 생성 및 실행
calculator = Calculator()
calculator.window.mainloop()