from math import sqrt
from PyQt6.QtWidgets import QApplication, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

def get_a():
    global a
    a = input_prompt.text()
    input_prompt.clear()

def get_b():
    global b
    b = input_prompt.text()
    input_prompt.clear()

def get_c():
    global c
    c = input_prompt.text()
    input_prompt.clear()

def get_d():
    global d
    d = input_prompt.text()
    input_prompt.clear()

def solvef():
    global total
    try:
        alocal = float(a)
        blocal = float(b)
        clocal = float(c)
        dlocal = float(d)
        possiblesolutions = []
        counter = 1
        while counter <= abs(dlocal):
            if (dlocal % counter) == 0.0:
                possiblesolutions.append(counter)
                possiblesolutions.append((-counter))
            counter += 1
        for i in possiblesolutions:
            if (alocal*(pow(i, 3))+blocal*(pow(i, 2))+clocal*i+dlocal) == 0.0:
                solution = i
                break
        afinal = alocal
        add = afinal * solution
        bfinal = blocal + add
        add = bfinal * solution
        cfinal = clocal + add
        add = cfinal * solution
        dfinal = dlocal + add
        x1 = solution
        total += "x1 = " + str(x1) + "\n"
        D = ((bfinal * bfinal) - 4 * afinal * cfinal)
        if D > 0:
            x2 = ((-1 * bfinal) + sqrt(D)) / (2 * afinal)
            x3 = ((-1 * bfinal) - sqrt(D)) / (2 * afinal)
            total += 'x2 = ' + str(x2) + "\n" + 'x3 = ' + str(x3) + "\n"
        elif D == 0:
            x2 = (- bfinal / 2 * afinal)
            total += 'x2 = ' + str(x2) + "\n" + 'x3 = ' + str(x3) + "\n"
        display.setText(total)
    except:
        total = welcome
        display.setText(total)

app = QApplication([])
w = QWidget()
w.setWindowTitle("Cubic equation solver")
w.resize(700, 500)
display = QTextEdit()
display.setReadOnly(True)
input_prompt = QLineEdit()
input_prompt.setPlaceholderText('Type here:')
pb1 = QPushButton("a")
pb2 = QPushButton("b")
pb3 = QPushButton("c")
pb4 = QPushButton("d")
pb5 = QPushButton("Find")
l1 = QVBoxLayout()
l2 = QHBoxLayout()
l3 = QHBoxLayout()
l1.addWidget(input_prompt)
l2.addWidget(pb1)
l2.addWidget(pb2)
l2.addWidget(pb3)
l2.addWidget(pb4)
l1.addLayout(l2)
l1.addWidget(pb5)
l3.addWidget(display)
l3.addLayout(l1)
w.setLayout(l3)
w.show()
total = ''
welcome = 'The program displays the values of the the Xs that are real numbers provided they exist\nthe form of the equation is a*(x*x*x) + b*(x*x) + c*x + d = 0, with a not being equal to 0\ninput a, b, c and d\n'
total += welcome
display.setText(total)
pb1.clicked.connect(get_a)
pb2.clicked.connect(get_b)
pb3.clicked.connect(get_c)
pb4.clicked.connect(get_d)
pb5.clicked.connect(solvef)
app.exec()