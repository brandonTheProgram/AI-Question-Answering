from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMessageBox
from QnAEngines import cdQA
PUSH_BUTTON_STYLE  = "background-color: blue; color: rgb(255, 255, 255); border: 5px solid black; border-radius : 20px"

class Ui_Dialog(object):
    #Set up the Question and Answer UI as defined by PyQt
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1344, 747)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, 
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().
                                     hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.questionLineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionLineEdit.sizePolicy().hasHeightForWidth())
        self.questionLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.questionLineEdit.setFont(font)
        self.questionLineEdit.setObjectName("questionLineEdit")
        self.verticalLayout_3.addWidget(self.questionLineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setStyleSheet(PUSH_BUTTON_STYLE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, 
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_2.addWidget(self.searchButton)
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setStyleSheet(PUSH_BUTTON_STYLE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, 
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy(). hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.answerTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, 
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerTextEdit.sizePolicy().hasHeightForWidth())
        self.answerTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.answerTextEdit.setFont(font)
        self.answerTextEdit.setReadOnly(True)
        self.answerTextEdit.setObjectName("answerTextEdit")
        self.verticalLayout_2.addWidget(self.answerTextEdit)
        
        #Connect the QObjects so that they perforn actions
        self.searchButton.clicked.connect(self.answerQuetion)
        self.cancelButton.clicked.connect(self.cancelQuestion)
        
        #Variable for the data
        self.data = ""
        self.firstRun = True
    
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #Update the UI page as defined by PyQt    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", 
                                      "Please input your question:"))
        self.searchButton.setText(_translate("Dialog", "SUBMIT"))
        self.cancelButton.setText(_translate("Dialog", "CANCEL"))
        
    #If a question was typed, display the answer else a warning message
    def answerQuetion(self):
        #Check if a question was typed
        if(self.questionLineEdit.text()):
            self.answerTextEdit.setPlainText("Loading Answer!")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please Wait")
            msg.setInformativeText("Please wait and allow up to 30 seconds while the engine processes, "
                                   "you may see the window say not responding, but it is processing data."
                                   "\n\nClose this to begin")
            msg.setWindowTitle("Processing")
            msg.exec_()

            answer = cdQA(self.questionLineEdit.text(), self.firstRun)

            if self.firstRun:
                self.firstRun = False

            self.answerTextEdit.setPlainText(answer)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setInformativeText('Please enter some text')
            msg.setWindowTitle("Error")
            msg.exec_()
    
    #If the user clicks the cancel button, clear the question and answer        
    def cancelQuestion(self):
        if(self.questionLineEdit.text()):
            self.questionLineEdit.clear()
            self.answerTextEdit.clear()
            
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Exit")
        msg.setInformativeText('If you wish to go back, exit the screen')
        msg.setWindowTitle("Exit")
        msg.exec_()
        
    #Set the data for the dialog
    def setData(self, data):
        self.data = data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

