from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Marishba(object):
    def setupUi(self, Marishba):
        Marishba.setObjectName("Marishba")
        Marishba.resize(293, 354)
        Marishba.setStyleSheet("QWidget{\n"
"    background-color:black;\n"
"}")
        Marishba.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Marishba)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:white;\n"
"border-radius: 4px;\n"
"color: grey;\n"
"\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.percent = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("%"))
        self.percent.setGeometry(QtCore.QRect(10, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.percent.setFont(font)
        self.percent.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.percent.setObjectName("percent")
        self.divide = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divide.setGeometry(QtCore.QRect(220, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.divide.setFont(font)
        self.divide.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.divide.setObjectName("divide")
        self.black = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.black.setGeometry(QtCore.QRect(150, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.black.setFont(font)
        self.black.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.black.setObjectName("black")
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.clear.setGeometry(QtCore.QRect(80, 80, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear.setFont(font)
        self.clear.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.clear.setObjectName("clear")
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.eight.setGeometry(QtCore.QRect(80, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eight.setFont(font)
        self.eight.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.eight.setObjectName("eight")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multiply.setGeometry(QtCore.QRect(220, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.multiply.setObjectName("multiply")
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.nine.setGeometry(QtCore.QRect(150, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nine.setFont(font)
        self.nine.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.nine.setObjectName("nine")
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.seven.setGeometry(QtCore.QRect(10, 130, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.seven.setFont(font)
        self.seven.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.seven.setObjectName("seven")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.five.setGeometry(QtCore.QRect(80, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.five.setObjectName("five")
        self.minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minus.setGeometry(QtCore.QRect(220, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.minus.setObjectName("minus")
        self.sex = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.sex.setGeometry(QtCore.QRect(150, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sex.setFont(font)
        self.sex.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.sex.setObjectName("sex")
        self.four = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.press_it("4"))
        self.four.setGeometry(QtCore.QRect(10, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.four.setObjectName("four")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.two.setGeometry(QtCore.QRect(80, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.two.setObjectName("two")
        self.plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.plus.setGeometry(QtCore.QRect(220, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.plus.setObjectName("plus")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.three.setGeometry(QtCore.QRect(150, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.three.setObjectName("three")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.one.setGeometry(QtCore.QRect(10, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.one.setObjectName("one")
        self.decimal = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.decimal.setGeometry(QtCore.QRect(80, 280, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.decimal.setFont(font)
        self.decimal.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.decimal.setObjectName("decimal")
        self.equal = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_it())
        self.equal.setGeometry(QtCore.QRect(150, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equal.setFont(font)
        self.equal.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:green;\n"
"}")
        self.equal.setObjectName("equal")
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.zero.setGeometry(QtCore.QRect(10, 280, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zero.setFont(font)
        self.zero.setStyleSheet("QPushButton{\n"
"color:white;\n"
"\n"
"border-radius:50px;\n"
"background-color:red;\n"
"}")
        self.zero.setObjectName("zero")
        Marishba.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Marishba)
        self.statusbar.setObjectName("statusbar")
        Marishba.setStatusBar(self.statusbar)

        self.retranslateUi(Marishba)
        QtCore.QMetaObject.connectSlotsByName(Marishba)
    def math_it(self):
        
        scr = self.label.text()
        if scr == "9594":
                self.label.setText("Codevision")
        else:
                answer = eval(scr)
    
                self.label.setText(str(answer))
    def remove_it(self):
        scr = self.label.text()
        scr = scr[:-1]
        self.label.setText(scr)
    def dot_it(self):
        scr = self.label.text()
        if scr[-1] == ".":
            pass
        else:
            self.label.setText(f"{scr}.")
    def press_it(self,pressed):
        if pressed == "C":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                self.label.setText("")
                self.label.setText(pressed)
            else:
                self.label.setText(f"{self.label.text()}{pressed}")
    def retranslateUi(self, Marishba):
        _translate = QtCore.QCoreApplication.translate
        Marishba.setWindowTitle(_translate("Marishba", "Codevision"))
        self.label.setText(_translate("Marishba", "0"))
        self.percent.setText(_translate("Marishba", "%"))
        self.divide.setText(_translate("Marishba", "/"))
        self.black.setText(_translate("Marishba", "X"))
        self.clear.setText(_translate("Marishba", "C"))
        self.eight.setText(_translate("Marishba", "8"))
        self.multiply.setText(_translate("Marishba", "*"))
        self.nine.setText(_translate("Marishba", "9"))
        self.seven.setText(_translate("Marishba", "7"))
        self.five.setText(_translate("Marishba", "5"))
        self.minus.setText(_translate("Marishba", "-"))
        self.sex.setText(_translate("Marishba", "6"))
        self.four.setText(_translate("Marishba", "4"))
        self.two.setText(_translate("Marishba", "2"))
        self.plus.setText(_translate("Marishba", "+"))
        self.three.setText(_translate("Marishba", "3"))
        self.one.setText(_translate("Marishba", "1"))
        self.decimal.setText(_translate("Marishba", "."))
        self.equal.setText(_translate("Marishba", "="))
        self.zero.setText(_translate("Marishba", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Marishba = QtWidgets.QMainWindow()
    ui = Ui_Marishba()
    ui.setupUi(Marishba)
    Marishba.show()
    sys.exit(app.exec_())


