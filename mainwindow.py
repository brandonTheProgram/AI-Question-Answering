from QuestionAndAnswer import *
from ListBoxWidget import *
from FileConverters import *
from DataVisual import Canvas
from PyQt5.Qt import QFileDialog, QThread
import sys, os, pickle

DEFAULT_MES       = "Enter the article text here then click confirm"
PROGRESS_BAR_RATE = 20
SAVE_STATE_FILE   = "SaveState.txt"
DATA_FILE         = "Data.txt"

class Ui_MainWindow(object):
    #Set up the UI as defined by PyQt
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 992)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWindowLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainWindowLayout.setObjectName("mainWindowLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.mainWindowLayout.addWidget(self.label)
        self.uploadGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadGroupBox.sizePolicy().hasHeightForWidth())
        self.uploadGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.uploadGroupBox.setFont(font)
        self.uploadGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uploadGroupBox.setFlat(False)
        self.uploadGroupBox.setCheckable(False)
        self.uploadGroupBox.setObjectName("uploadGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uploadGroupBox)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(13, -1, -1, -1)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uploadFELabel = QtWidgets.QLabel(self.uploadGroupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uploadFELabel.setFont(font)
        self.uploadFELabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadFELabel.setObjectName("uploadFELabel")
        self.horizontalLayout_4.addWidget(self.uploadFELabel)
        self.uploadFEButton = QtWidgets.QPushButton(self.uploadGroupBox)
        self.uploadFEButton.setStyleSheet(PUSH_BUTTON_STYLE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadFEButton.sizePolicy().hasHeightForWidth())
        self.uploadFEButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uploadFEButton.setFont(font)
        self.uploadFEButton.setObjectName("uploadFEButton")
        self.horizontalLayout_4.addWidget(self.uploadFEButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uploadDDLabel = QtWidgets.QLabel(self.uploadGroupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uploadDDLabel.setFont(font)
        self.uploadDDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadDDLabel.setObjectName("uploadDDLabel")
        self.horizontalLayout_5.addWidget(self.uploadDDLabel)
        self.uploadDDButton = QtWidgets.QPushButton(self.uploadGroupBox)
        self.uploadDDButton.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uploadDDButton.setFont(font)
        self.uploadDDButton.setObjectName("uploadDDButton")
        self.horizontalLayout_5.addWidget(self.uploadDDButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.mainWindowLayout.addWidget(self.uploadGroupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enterTextLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.enterTextLabel.setFont(font)
        self.enterTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.enterTextLabel.setObjectName("enterTextLabel")
        self.horizontalLayout.addWidget(self.enterTextLabel)
        self.enterTextButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterTextButton.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.enterTextButton.setFont(font)
        self.enterTextButton.setObjectName("enterTextButton")
        self.horizontalLayout.addWidget(self.enterTextButton)
        self.mainWindowLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.showVisualLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.showVisualLabel.setFont(font)
        self.showVisualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showVisualLabel.setObjectName("showVisualLabel")
        self.horizontalLayout_6.addWidget(self.showVisualLabel)
        self.showVisualBut = QtWidgets.QPushButton(self.centralwidget)
        self.showVisualBut.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.showVisualBut.setFont(font)
        self.showVisualBut.setObjectName("showVisualBut")
        self.horizontalLayout_6.addWidget(self.showVisualBut)
        self.mainWindowLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.showFilesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.showFilesLabel.setFont(font)
        self.showFilesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showFilesLabel.setObjectName("showFilesLabel")
        self.horizontalLayout_7.addWidget(self.showFilesLabel)
        self.showFilesBut = QtWidgets.QPushButton(self.centralwidget)
        self.showFilesBut.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.showFilesBut.setFont(font)
        self.showFilesBut.setObjectName("showFilesBut")
        self.horizontalLayout_7.addWidget(self.showFilesBut)
        self.mainWindowLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.qnAEngineLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.qnAEngineLabel.setFont(font)
        self.qnAEngineLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.qnAEngineLabel.setObjectName("qnAEngineLabel")
        self.horizontalLayout_2.addWidget(self.qnAEngineLabel)
        self.qnAButton = QtWidgets.QPushButton(self.centralwidget)
        self.qnAButton.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.qnAButton.setFont(font)
        self.qnAButton.setObjectName("qnAButton")
        self.horizontalLayout_2.addWidget(self.qnAButton)
        self.mainWindowLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.askQuestionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.askQuestionLabel.setFont(font)
        self.askQuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.askQuestionLabel.setObjectName("askQuestionLabel")
        self.horizontalLayout_3.addWidget(self.askQuestionLabel)
        self.askQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.askQuestionButton.setStyleSheet(PUSH_BUTTON_STYLE)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.askQuestionButton.setFont(font)
        self.askQuestionButton.setObjectName("askQuestionButton")
        self.horizontalLayout_3.addWidget(self.askQuestionButton)
        self.mainWindowLayout.addLayout(self.horizontalLayout_3)
        self.label.raise_()
        self.uploadGroupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 31))
        self.menubar.setObjectName("menubar")
        self.menuUpload = QtWidgets.QMenu(self.menubar)
        self.menuUpload.setObjectName("menuUpload")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload_Documents = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.actionUpload_Documents.setFont(font)
        self.actionUpload_Documents.setObjectName("actionUpload_Documents")
        self.actionUpload_DocumentsDD = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.actionUpload_DocumentsDD.setFont(font)
        self.actionUpload_DocumentsDD.setObjectName("actionUpload_DocumentsDD")
        self.menuUpload.addAction(self.actionUpload_Documents)
        self.menuUpload.addAction(self.actionUpload_DocumentsDD)
        self.menubar.addAction(self.menuUpload.menuAction())
        #End of PyQt Definition
        
        #Create and Add the extra QWidgets to the UI
        self.canvas = Canvas(self.centralwidget)
        self.mainWindowLayout.addWidget(self.canvas)

        self.closeVisualBut = QtWidgets.QPushButton(self.centralwidget)
        self.closeVisualBut.setStyleSheet(PUSH_BUTTON_STYLE)
        self.mainWindowLayout.addWidget(self.closeVisualBut)

        self.enteredText = QtWidgets.QTextEdit(self.centralwidget)
        self.mainWindowLayout.addWidget(self.enteredText)
        
        self.listbox_view = ListBoxWidget(self.centralwidget)
        self.mainWindowLayout.addWidget(self.listbox_view)
        
        self.confirmTextBut = QtWidgets.QPushButton(self.centralwidget)
        self.confirmTextBut.setStyleSheet(PUSH_BUTTON_STYLE)
        self.mainWindowLayout.addWidget(self.confirmTextBut)
        
        self.confirmDDBut = QtWidgets.QPushButton(self.centralwidget)
        self.confirmDDBut.setStyleSheet(PUSH_BUTTON_STYLE)
        self.mainWindowLayout.addWidget(self.confirmDDBut)
        
        self.deleteDDBut = QtWidgets.QPushButton(self.centralwidget)
        self.deleteDDBut.setStyleSheet(PUSH_BUTTON_STYLE)
        self.mainWindowLayout.addWidget(self.deleteDDBut)
        
        self.radioButtonCDQA = QtWidgets.QRadioButton(self.centralwidget)
        self.mainWindowLayout.addWidget(self.radioButtonCDQA)
        
        self.confirmQNAEnGnBut = QtWidgets.QPushButton(self.centralwidget)
        self.confirmQNAEnGnBut.setStyleSheet(PUSH_BUTTON_STYLE)
        self.mainWindowLayout.addWidget(self.confirmQNAEnGnBut)
        
        self.bar = QtWidgets.QProgressBar(self.centralwidget)
        self.bar.setTextVisible(True)
        self.bar.setAlignment(Qt.AlignCenter)
        self.mainWindowLayout.addWidget(self.bar)
        
        #Set the font for the text in the GUI
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.confirmTextBut.setFont(font)
        self.confirmDDBut.setFont(font)
        self.deleteDDBut.setFont(font)
        self.confirmQNAEnGnBut.setFont(font)
        self.radioButtonCDQA.setFont(font)
        self.closeVisualBut.setFont(font)
        
        #Hide and show the necessary QObjects
        self.hideUIElements()
        self.showUIElements()
        
        #Connect the QObjects so that they perforn actions
        self.actionUpload_Documents.triggered.connect(self.on_UploadFiles_clicked)
        self.actionUpload_DocumentsDD.triggered.connect(self.on_UploadFilesDD_clicked)
        
        self.confirmTextBut.clicked.connect(self.confirmText)
        self.confirmDDBut.clicked.connect(self.confirmDD)
        self.confirmQNAEnGnBut.clicked.connect(self.confirmQNAEngine)
        self.uploadFEButton.clicked.connect(self.on_UploadFiles_clicked)
        self.uploadDDButton.clicked.connect(self.on_UploadFilesDD_clicked)
        self.enterTextButton.clicked.connect(self.on_EnterText_clicked)
        self.askQuestionButton.clicked.connect(self.on_AskQuestion_clicked)
        self.deleteDDBut.clicked.connect(self.deleteDD)
        self.showFilesBut.clicked.connect(self.showFiles)
        self.qnAButton.clicked.connect(self.on_QNAEngines_clicked)
        self.showVisualBut.clicked.connect(self.showVisual)
        self.closeVisualBut.clicked.connect(self.closeVisual)
        
        #Create a string to hold the data and a list for file paths
        self.data = ""
        self.dataFilePaths = []

        #Read in data from the previous state
        self.readSaveState()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        app.aboutToQuit.connect(self.closeEvent)
        
    #Update the UI page as defined by PyQt           
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", 
                "Please Select One Of The Options Below To Begin"))
        self.uploadFELabel.setText(_translate("MainWindow", 
                "Click here to upload document(s) using File Explorer"))
        self.uploadFEButton.setText(_translate("MainWindow", "BROWSE"))
        self.uploadDDLabel.setText(_translate("MainWindow", 
                "Click here to upload document(s) using Drag and Drop"))
        self.uploadDDButton.setText(_translate("MainWindow", 
                                               "Drag and Drop"))
        self.enterTextLabel.setText(_translate("MainWindow", 
                "Click here to type and paste your document text"))
        self.enterTextButton.setText(_translate("MainWindow", 
                "ENTER TEXT"))
        self.askQuestionLabel.setText(_translate("MainWindow", 
                "Ask a Question"))
        self.qnAEngineLabel.setText(_translate("MainWindow", 
                "Pick your Q&A Engine"))
        self.showVisualLabel.setText(_translate("MainWindow", 
                "Show Visual Graph"))
        self.showFilesLabel.setText(_translate("MainWindow", 
                "Show Files"))
        self.qnAButton.setText(_translate("MainWindow", "PICK ENGINE"))
        self.askQuestionButton.setText(_translate("MainWindow", "BEGIN"))
        self.menuUpload.setTitle(_translate("MainWindow", "Upload"))
        self.actionUpload_Documents.setText(_translate("MainWindow", 
                "Upload Document(s) using File Explorer"))
        self.actionUpload_DocumentsDD.setText(_translate("MainWindow", 
                "Upload Document(s) using Drag and Drag"))
        self.confirmTextBut.setText(_translate("MainWindow", "CONFIRM"))
        self.confirmDDBut.setText(_translate("MainWindow", "CONFIRM"))
        self.confirmQNAEnGnBut.setText(_translate("MainWindow", "CONFIRM"))
        self.deleteDDBut.setText(_translate("MainWindow", 
                                            "DELETE SELECTED FILE"))
        self.showFilesBut.setText(_translate("MainWindow", 
                                            "SHOW ALL FILES"))
        self.showVisualBut.setText(_translate("MainWindow", "SHOW VISUAL"))
        self.closeVisualBut.setText(_translate("MainWindow", "CLOSE VISUAL"))
        self.radioButtonCDQA.setText(_translate("MainWindow", "cdQA"))
        
        self.uploadGroupBox.setTitle(_translate("MainWindow", 
                                                "Upload Documents"))

    #Create the Dialog object for the Question and Answer
    def openDialog(self):
        self.questionAndAnswerDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.questionAndAnswerDialog)
                
        #Set the data for the dialog
        self.ui.setData(self.data)
                
        #Save the data into a text file
        try:
            with open(DATA_FILE, 'w', encoding="utf-8") as fileObject:
                fileObject.write(self.data)
        except Exception as err:
            LogError(err, DATA_FILE)

        #Convert that textfile to a pdf to use
        txtFile_to_pdf(DATA_FILE)
    
        self.questionAndAnswerDialog.exec()

    #Save the data as the window attempts to close
    def closeEvent(self):
        #Clear the data for the new save state
        try:
            open(SAVE_STATE_FILE, 'w').close()
        except Exception as err:
            LogError(err, SAVE_STATE_FILE)

        #Save the data as a save state
        try:
            with open(SAVE_STATE_FILE, 'wb') as f:
                pickle.dump(self.dataFilePaths, f)
        except Exception as err:
            LogError(err, SAVE_STATE_FILE)

        sys.exit(0)

    #Read the data from the last save state
    def readSaveState(self):
        try:
            with open(SAVE_STATE_FILE, 'rb') as f:
                #Check if the file is not empty
                if(os.stat(SAVE_STATE_FILE).st_size != 0):
                    self.dataFilePaths = pickle.load(f)

                    #Remove duplicate files
                    self.dataFilePaths = list(set(self.dataFilePaths))

                    if(self.dataFilePaths):
                        for path in self.dataFilePaths:
                            self.listbox_view.addItem(path)
        except Exception as err:
            LogError(err, SAVE_STATE_FILE)

    #Close the visual graph
    def closeVisual(self):
        self.hideUIElements()
        self.showUIElements()

    #Confirm that items were uploaded to the Drag and Drop Menu
    def confirmDD(self):        
        #Check if the listbox is empty
        if self.listbox_view.count()== 0:
            self.listbox_view.clear()
        else:
            #Add the file path of each file to the list
            for i in range(0, self.listbox_view.count()):
                self.dataFilePaths.append(self.listbox_view.item(i).text())
                                
        self.hideUIElements()
        self.showUIElements()
        
    #Confirm that a Q&A was selected
    def confirmQNAEngine(self):
        msg = QMessageBox()
        #Check if a Q&A Engine was selected
        if self.radioButtonCDQA.isChecked():
            msg.setIcon(QMessageBox.Information)
            msg.setText("Selected")
            msg.setInformativeText("You selected to use the cdQA Q&A engine")
            msg.setWindowTitle("Selected")
            msg.exec_()
        else:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Missing")
            msg.setInformativeText("You must select a QnA engine")
            msg.setWindowTitle("Warning")
            msg.exec_()
            
        self.hideUIElements()
        self.showUIElements()
        
    #Confirm that there is text entered by the user
    def confirmText(self):        
        text = self.enteredText.toPlainText()
        
        #If there is no text or still displaying the default message
        if not text or text == DEFAULT_MES:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.setInformativeText("Please enter some text")
            msg.exec_()
        else:
            self.data += (self.enteredText.toPlainText() + "\n\n")
            self.enteredText.clear()
                 
        self.hideUIElements()
        self.showUIElements()
        
    #Delete the selected file from the list
    def deleteDD(self):
        listItems = self.listbox_view.selectedItems()

        if not listItems: return     

        for item in listItems:
            deletedItem = self.listbox_view.takeItem(self.listbox_view.row(item))
            self.dataFilePaths.remove(deletedItem.text())

    #Hide any option that may be open   
    def hideUIElements(self):
        self.label.hide()
        self.uploadGroupBox.hide()
        self.enterTextLabel.hide()
        self.enterTextButton.hide()
        self.qnAEngineLabel.hide()
        self.qnAButton.hide()
        self.askQuestionLabel.hide()
        self.askQuestionButton.hide()
        self.showFilesLabel.hide()
        self.showFilesBut.hide()     
        self.enteredText.hide()
        self.confirmTextBut.hide()
        self.listbox_view.hide()
        self.confirmDDBut.hide()
        self.bar.hide()
        self.deleteDDBut.hide()
        self.confirmQNAEnGnBut.hide()
        self.radioButtonCDQA.hide()
        self.canvas.hide()
        self.showVisualBut.hide()
        self.showVisualLabel.hide()
        self.closeVisualBut.hide()
        
    #Load in the data
    def loadData(self):
        if self.dataFilePaths:
            #Remove duplicate files
            self.dataFilePaths = list(set(self.dataFilePaths))
            
            for filename in self.dataFilePaths:
                if filename[-3:] == "pdf":
                    self.data = self.data + pdf2_to_text(filename) + "\n\n"
                elif filename[-4:] == "docx":
                    self.data = self.data + docx2_to_txt(filename) + "\n\n"
                else:
                    try:
                        with open(filename, "r") as f:
                            self.data = self.data + f.read() + "\n\n"
                    except Exception as err:
                        LogError(err, filename)
                            
    #Check if there is data before proceeding to open up the Dialog
    def on_AskQuestion_clicked(self):
        self.hideUIElements()
        self.bar.show()
         
        #Show the progress bar filling up
        for i in range(0, 101):
            self.bar.setValue(i)
            self.bar.setFormat(str(i) + '%')
            QThread.msleep(PROGRESS_BAR_RATE)

        #If a Q&A Engine has been selected, load the data
        if self.radioButtonCDQA.isChecked():
            self.loadData()

            #If there is data, then proceed to the Dialog
            if self.data:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Complete")
                msg.setInformativeText
                ("The files have been uploaded\nReady for Questions")
                msg.setWindowTitle("Complete")
                msg.exec_()    
                
                self.openDialog()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Missing")
                msg.setInformativeText("Missing files!! Please upload")
                msg.setWindowTitle("Warning")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Missing")
            msg.setInformativeText("Missing Q&A Engine!! Please pick one")
            msg.setWindowTitle("Warning")
            msg.exec_()
          
        self.bar.hide()
        self.showUIElements()
        
    #Display the textedit and confirm button for the user
    def on_EnterText_clicked(self):
        self.hideUIElements()
        
        self.enteredText.setPlainText(DEFAULT_MES)
        self.enteredText.show()
        self.confirmTextBut.show()
        
    #Display the radio buttons for the user
    def on_QNAEngines_clicked(self):
        self.hideUIElements()
        self.confirmQNAEnGnBut.show()
        self.radioButtonCDQA.show()   
        
    #Ask and store the content of the files selected by the user
    def on_UploadFiles_clicked(self):
        self.hideUIElements()
                
        filenamesList = QFileDialog.getOpenFileNames()[0]
        
        #For each file selected, add the path to the list
        for filename in filenamesList:        
            if(filename):
                self.dataFilePaths.append(filename)
                self.listbox_view.addItem(filename)
                
        self.showUIElements()
    
    #Display the Drag and Drop area for the user to upload files
    def on_UploadFilesDD_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Drag and Drop")
        msg.setInformativeText("Please drag and drop your files below")
        msg.setWindowTitle("Drag and Drop")
        msg.exec_()
        
        self.hideUIElements()
        
        self.listbox_view.show()
        self.confirmDDBut.show()
        self.deleteDDBut.show()
        
    #Show the files that have been uploaded
    def showFiles(self):
        self.hideUIElements()
        
        self.listbox_view.show()
        self.confirmDDBut.show()
        self.deleteDDBut.show()

    #Show the visual graph
    def showVisual(self):
        msg = QMessageBox()
        if self.dataFilePaths:
            self.hideUIElements()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Loading Visual")
            msg.setInformativeText("Please wait while the visual loads")
            msg.setWindowTitle("Loading Visual")
            msg.exec_()

            #Remove duplicate files
            self.dataFilePaths = list(set(self.dataFilePaths))

            self.canvas.show()
            self.closeVisualBut.show()

            self.canvas.DisplayVisual(self.dataFilePaths)

        else:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Missing")
            msg.setInformativeText("Missing files!! Please upload")
            msg.setWindowTitle("Warning")
            msg.exec_()

    #Reveal the hidden UI Elements    
    def showUIElements(self):
        self.label.show()
        self.uploadGroupBox.show()
        self.enterTextLabel.show()
        self.enterTextButton.show()
        self.qnAEngineLabel.show()
        self.qnAButton.show()
        self.askQuestionLabel.show()
        self.askQuestionButton.show()
        self.showFilesBut.show()
        self.showVisualBut.show()      
        self.showFilesLabel.show()
        self.showVisualLabel.show()  
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

