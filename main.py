from PyQt5.QtWidgets import QApplication

app = QApplication([])

from m2 import*
from m3 import*
from random import choice, shuffle
from time import sleep
class Question:
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer=answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
        self.isAsking = True
q1 = Question('2+2', '4', '6', '8', '10')
q2 = Question('102*5', '510', '89', '50', '90')
q3 = Question('34*9', '306', '23', '2', '603')
q4 = Question('90-35', '55', '1', '302', '3')
q5 = Question('89-7', '82', '901', '82', '23')
q6 = Question('8*0', '0', '6', '56', '78')
q7 = Question('6+8', '14', '90', '7', '9')
q8 = Question('32-6', '26', '21', '4', '58')
q9 = Question('67-89', '-22', '-90', "-3", '90')
q10 = Question('678-984', '-306', '-4', '-21', '98')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question. setText (cur_q.question)
    lb_right_answer.setText (cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText (cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText (cur_q.answer)
new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText("Правильно")
                answer.setChecked(False)
                break
    else:
        lb_result.setText("Неправильно")
    RadioGroup.setExclusive(True)
def click_ok ():
    if btn_next.text()=="Відповісти":
        check()
        gb_question.hide()
        gb_answer.show()


        btn_next.setText("Наступне запитання")
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()


        btn_next.setText("Відповісти")
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def menu_generation():
    menu_win.show()
    window.hide()

btn_menu. clicked. connect (menu_generation)
#
def back_menu():
    menu_win.hide()
    window.show()

btn_back. clicked. connect (back_menu)
def clear():
    le_question.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect (clear)
def add_question():
    new_q=Question(le_question.text(),le_right_ans.text(),le_wrong_ans1.text(),le_wrong_ans2.text(),le_wrong_ans3.text())


    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)


window.show()
app.exec_()

