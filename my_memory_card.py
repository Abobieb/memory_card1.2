from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('как называлась копия игры half-life когда ее слили до даты выхода', 'half-life-beta','half-life-gama', 'half-life-alfa',' half-life-abama'))
questions_list.append(Question('в каком году вышла первая часть серии игр half-life?', '1987', '1999', '1200', '1996'))
questions_list.append(Question('Как зовут основателя компании Valve?', 'Гейб Нюэл', 'Нерел Автел', 'Джон Банди', 'Никола Бебрович'))
questions_list.append(Question('что кричали гражданские когда на них проводили набеги с проверками сотрудники Альянса?', 'ГОшники!', 'Шухер!', 'Бежим!', 'Спасайтесь!'))
questions_list.append(Question('что отличает обычного сотрудника ГО от солдата Альянса?', 'Солдат альянса генно модефецированый солдат в отличии от обычного сотрудника', 'Ну солдат круче', 'солдат сильнее чем обычный сотрудник', 'а вот потому-что пон?'))
questions_list.append(Question('Чем опасен Барнакл из серии игр half-life?', 'тем что способен схватить жертву и медленно поедать','Неожиданно нападет из темноты', 'тем что может выпускать кислоту в противника', 'воздействует на жертву психологически'))
questions_list.append(Question('Ради чего граждане вступали в ряды ГО?','Ради лучшей жизни',"ради власти",'ради безопасности','ради уажения со стороны общества'))
questions_list.append(Question('Как зовут домашнего животного доктора Кляйнера','Хедкраб Ламар','Пёс Андре','Ворона Джери','Жук переросток Колли'))
questions_list.append(Question('Что делали headcrab когда попадал на голову человека?','Заражал его тем самым делая его своим носителем','Убивал','Наносил значительный вред здоровью','Просто сидел на голове'))
questions_list.append(Question('как приготовить макароны?','легко','нелегко','дело настоящего воина','да кто его знает'))
questions_list.append(Question('Как назывался игровой движок который стал прорывным в 2004 году и поражал людей своими возможностями?', 'Source', 'Gold source', 'Source2','Source-betta'))
questions_list.append(Question('Когда началась вторая МИРОВАЯ война?','1939','1941','1940','1930'))
app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    window.total += 1
    window.cur_question = window.cur_question + 1 
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 
    q = questions_list[window.cur_question]
    ask(q)
    print('Статистика -\n всего вопросов:\n' , window.total, 'Правильных ответов:', window.score )

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question() 

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.cur_question = -1    
                            
btn_OK.clicked.connect(click_OK) 

window.score = 0
window.total = 0

next_question()
window.resize(400, 300)
window.show()
app.exec()
