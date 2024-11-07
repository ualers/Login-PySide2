########################################################################
## IMPORTS Libs
import sys
import os
import subprocess
from typing import Dict, Any
import time
import psutil
import GPUtil
import math
import hashlib
from typing import Dict, Any
import os
import subprocess
import platform
from firebase_admin import credentials, initialize_app, storage, db, delete_app
import concurrent.futures
########################################################################


########################################################################
# IMPORT FirebaseKeys
from FirebaseKeys.key import keys_app_2 
app2 = keys_app_2()
########################################################################

########################################################################
# IMPORT .qrc
from src import icons_interpreter
########################################################################

########################################################################
# IMPORT GUI Loading
from src.ui_splash_screen import *
########################################################################

########################################################################
# IMPORT GUI Login
from src.ui_interface import Ui_MainWindow
########################################################################

########################################################################
# IMPORT GUI SoftwareAI
from src.ui_cliente_and_chat import Ui_MainWindow_SoftwareAI
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomModals import QCustomModals
########################################################################

########################################################################
# IMPORT Pyside2
from PySide2extn.RoundProgressBar import roundProgressBar #IMPORT THE EXTENSION LIBRARY
from PySide2.QtCore import QTimer, Signal, QThread


########################################################################


########################################################################
# IMPORT nvidia-smi
possible_paths = [
    "C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi.exe",
    "C:\\Windows\\System32\\nvidia-smi.exe",
    "/usr/bin/nvidia-smi",
    "/usr/local/bin/nvidia-smi"
]
nvidia_smi = None
for path in possible_paths:
    if os.path.exists(path):
        nvidia_smi = path
        break
x = 0
p = 1
########################################################################

########################################################################
# QThread Update Loading Screen
class Updateloader(QThread):
    messagesignal = Signal(str)
    circleColor1signal = Signal(str)
    circleColor2signal = Signal(str)
    finishedd = Signal()
    def __init__(self, message, color1, color2):
        super().__init__()
        self.message = message
        self.color1 = color1
        self.color2 = color2
        self.running = True

    def run(self):
        while self.running:
            time.sleep(4)
            self.messagesignal.emit(self.message)

            self.messagesignal.emit("LOADING..")

            # self.circleColor1signal.emit(self.color1)
            # self.circleColor2signal.emit(self.color2)

            self.messagesignal.emit("LOADING...")

            self.finishedd.emit()

    def stop(self):
        self.running = False
        self.wait()

########################################################################
# QThread Update Loading Screen
class Updateloader_2(QThread):
    messagesignal = Signal(str)
    circleColor1signal = Signal(str)
    circleColor2signal = Signal(str)
    finishedd = Signal()
    def __init__(self, message, color1, color2):
        super().__init__()
        self.message = message
        self.color1 = color1
        self.color2 = color2
        self.running = True

    def run(self):
        while self.running:
            time.sleep(4)
            self.messagesignal.emit(self.message)

            self.messagesignal.emit("LOADING..")

            # self.circleColor1signal.emit(self.color1)
            # self.circleColor2signal.emit(self.color2)

            self.messagesignal.emit("LOADING...")

            self.finishedd.emit()

    def stop(self):
        self.running = False
        self.wait()



########################################################################
# MainWindow SoftwareAI
class MainWindowSoftwareAI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_SoftwareAI()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style_loading.json"}
                      )

########################################################################
# MainWindow Loading Screen SoftwareAI
class LoadingScreen_MainWindow_SoftwareAI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_Loading()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style_loading_2.json"}
                      )
        self.myParentWidget = self.ui.widget
        
        self.myParentWidget.message="LOADING."
        self.myParentWidget.size=QSize(600, 600)
        self.myParentWidget.color=QColor("white")
        self.myParentWidget.fontFamily="Ebrima"
        self.myParentWidget.fontSize=30
        self.myParentWidget.rayon=200
        self.myParentWidget.duration=60 * 1000
        self.myParentWidget.noiseOctaves=0.8
        self.myParentWidget.noiseSeed=int(time.time())
        self.myParentWidget.backgroundColor=QColor("transparent")
        self.myParentWidget.circleColor1=QColor("#ff2e63")
        self.myParentWidget.circleColor2=QColor("#082e63")
        self.myParentWidget.circleColor3=QColor(57, 115, 171, 100)
        # myModal = QCustomModals.InformationModal(
        #     title="Loading SoftwareAI", 
        #     parent=self,
        #     position='top-right',
        #     closeIcon=":/feather/icons/feather/window_close.png",
        #     modalIcon=":/feather/icons/feather/info.png",
        #     description="loading should take a few seconds...",
        #     isClosable=False,
        #     duration=3000
        # )
        #myModal.show()

        ########################################################################
        #QAppSettings.updateAppSettings(self)
        ########################################################################
        message = "LOADING."
        circleColor1 = QColor("#1e0880")
        circleColor2 = QColor("#000000")


        self.threadUpdateloader = Updateloader(message, circleColor1, circleColor2)
        self.threadUpdateloader.messagesignal.connect(self.message_signal)
        self.threadUpdateloader.circleColor1signal.connect(self.circleColor1_signal)
        self.threadUpdateloader.circleColor2signal.connect(self.circleColor2_signal)
        self.threadUpdateloader.finishedd.connect(self.finish_loading)
        self.threadUpdateloader.start()


        #self.show()

    def circleColor1_signal(self, Color1):
        self.myParentWidget.circleColor1=Color1

    def circleColor2_signal(self, Color2):
        self.myParentWidget.circleColor2=Color2

    def message_signal(self, mensage):
        self.myParentWidget.message=mensage

    def finish_loading(self):
        QTimer.singleShot(1000, self.show_main_window)


    def show_main_window(self):
        self.threadUpdateloader.stop()
        self.close()
        self.main_window = MainWindowSoftwareAI()
        self.main_window.show()

########################################################################
# MainWindow Login and Sign Up
class MainWindow_Login_and_Sign_Up(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        loadJsonStyle(self, self.ui, jsonFiles={"JsonStyle/style.json"})

        self.User_or_Gmail_Login = self.ui.lineEdit_2
        self.Password_Login = self.ui.lineEdit
        self.button_Login = self.ui.pushButton_2
        self.button_Login.clicked.connect(self.login_and_Auth)
        self.button_Login.clicked.connect(self.save_config)


        self.User_or_Gmail_SignUp = self.ui.lineEdit_3
        self.Password_SignUp = self.ui.lineEdit_4
        self.TermsAgree_SignUp = self.ui.checkBox
        self.Register_button_SignUp = self.ui.pushButton_3
        self.Register_button_SignUp.clicked.connect(self.SignUp_and_Auth)

        #self.load_config()
        #QAppSettings.updateAppSettings(self)
       

    def SignUp_and_Auth(self):
        User_or_Gmail_SignUp = self.User_or_Gmail_SignUp.text()
        Password_SignUp = self.Password_SignUp.text()
        TermsAgree_SignUp = self.TermsAgree_SignUp.isChecked()
        if TermsAgree_SignUp:
            reference_db_Firebase = db.reference('Login_and_Auth', app=app2)

            
            User_or_Gmail_hash = hashlib.sha256(f"{User_or_Gmail_SignUp}".encode()).hexdigest()
        
            controle_das_funcao_info_2 = {
                "User_or_Gmail": User_or_Gmail_SignUp,
                "Password": Password_SignUp,

            }
            reference_db_Firebase.child(User_or_Gmail_hash).set(controle_das_funcao_info_2)
            myModal = QCustomModals.SuccessModal(
                title="Success Sign Up", 
                parent=self,
                position='top-right',
                closeIcon=":/feather/icons/feather/window_close.png",
                modalIcon=":/feather/icons/feather/info.png",
                description="Your account has been created, log in",
                isClosable=False,
                duration=3000
            )
            myModal.show()
            self.ui.stackedWidget.slideToPreviousWidget()

        else:
            myModal = QCustomModals.WarningModal(
                title="Terms and conditions", 
                parent=self,
                position='top-right',
                closeIcon=":/feather/icons/feather/window_close.png",
                modalIcon=":/feather/icons/feather/info.png",
                description="Accept the terms and conditions",
                isClosable=False,
                duration=3000
            )
            myModal.show()




    def login_and_Auth(self):
        User_or_Gmail_Login = self.User_or_Gmail_Login.text()
        Password_Login = self.Password_Login.text()

        User_or_Gmail_hash = hashlib.sha256(f"{User_or_Gmail_Login}".encode()).hexdigest()
        
        reference_db_Firebase = db.reference(f'Login_and_Auth/{User_or_Gmail_hash}', app=app2)
        data1 = reference_db_Firebase.get()                         
        if data1:
            User_or_Gmail = data1["User_or_Gmail"]
            Password = data1["Password"]
            if str(Password) == str(Password_Login):
                # myModal = QCustomModals.SuccessModal(
                #     title="Success Login", 
                #     parent=self,
                #     position='top-right',
                #     closeIcon=":/feather/icons/feather/window_close.png",
                #     modalIcon=":/feather/icons/feather/info.png",
                #     description="Your account has been successfully logged in Loading SoftwareAI",
                #     isClosable=False,
                #     duration=3000
                # )
                # myModal.show()
                self.close()
                self.main_window_loading = LoadingScreen_MainWindow_SoftwareAI()
                self.main_window_loading.show()


            else:
                myModal = QCustomModals.WarningModal(
                    title="Password", 
                    parent=self,
                    position='top-right',
                    closeIcon=":/feather/icons/feather/window_close.png",
                    modalIcon=":/feather/icons/feather/info.png",
                    description="Your password is not recognized",
                    isClosable=False,
                    duration=3000
                )
                myModal.show()



            
        else:
            myModal = QCustomModals.ErrorModal(
                title="Sign Up", 
                parent=self,
                position='top-right',
                closeIcon=":/feather/icons/feather/window_close.png",
                modalIcon=":/feather/icons/feather/info.png",
                description="You do not have any gmail account or username, Create an account for yourself",
                isClosable=False,
                duration=3000
            )
            myModal.show()
            self.ui.stackedWidget.slideToNextWidget()




    def get_machine_info(self):
        system_info = platform.uname()
        machine = system_info.node
        return machine

    def save_config(self):
        ref1 = db.reference(f'Save_Settings_Login_Users', app=app2)
        User_or_Gmail_hash = hashlib.sha256(f"{self.User_or_Gmail_Login.text()}".encode()).hexdigest()
        controle_das_funcao_info_2 = {
            "User_or_Gmail_Login": f"{self.User_or_Gmail_Login.text()}",
            "Password_Login": f"{self.Password_Login.text()}",
        }
        ref1.child(User_or_Gmail_hash).set(controle_das_funcao_info_2)
        # myModal = QCustomModals.SuccessModal(
        #     title="Success Save Login", 
        #     parent=self,
        #     position='top-right',
        #     closeIcon=":/feather/icons/feather/window_close.png",
        #     modalIcon=":/feather/icons/feather/info.png",
        #     description="Successfully !!",
        #     isClosable=False,
        #     duration=3000
        # )
        # myModal.show()
    def load_config(self):

        try:
            User_or_Gmail_hash = hashlib.sha256(f"{self.User_or_Gmail_Login.text()}".encode()).hexdigest()
            reference_db_Firebase = db.reference(f'Save_Settings_Login_Users/{User_or_Gmail_hash}', app=app2)
            data1 = reference_db_Firebase.get()                                     

            User_or_Gmail_Login = data1["User_or_Gmail_Login"]
            Password_Login = data1["Password_Login"]

            self.User_or_Gmail_Login.setText(str(User_or_Gmail_Login))
            self.Password_Login.setText(str(Password_Login))

            # myModal = QCustomModals.SuccessModal(
            #     title="Success Load Login", 
            #     parent=self,
            #     position='top-right',
            #     closeIcon=":/feather/icons/feather/window_close.png",
            #     modalIcon=":/feather/icons/feather/info.png",
            #     description="Successfully !!",
            #     isClosable=False,
            #     duration=3000
            # )
            # myModal.show()

        except Exception as e:
            print(e)
            #self.save_config()


########################################################################
# MainWindow Loading Screen Login and Sign Up
class LoadingScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_Loading()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles = {"JsonStyle/style_loading.json"}
                      )
        self.myParentWidget = self.ui.widget
        
        self.myParentWidget.message="LOADING."
        self.myParentWidget.size=QSize(600, 600)
        self.myParentWidget.color=QColor("white")
        self.myParentWidget.fontFamily="Ebrima"
        self.myParentWidget.fontSize=30
        self.myParentWidget.rayon=200
        self.myParentWidget.duration=60 * 1000
        self.myParentWidget.noiseOctaves=0.8
        self.myParentWidget.noiseSeed=int(time.time())
        self.myParentWidget.backgroundColor=QColor("transparent")
        self.myParentWidget.circleColor1=QColor("#ff2e63")
        self.myParentWidget.circleColor2=QColor("#082e63")
        self.myParentWidget.circleColor3=QColor(57, 115, 171, 100)
        # myModal = QCustomModals.InformationModal(
        #     title="Loading SoftwareAI", 
        #     parent=self,
        #     position='top-right',
        #     closeIcon=":/feather/icons/feather/window_close.png",
        #     modalIcon=":/feather/icons/feather/info.png",
        #     description="loading should take a few seconds...",
        #     isClosable=False,
        #     duration=3000
        # )
        #myModal.show()

        ########################################################################
        #QAppSettings.updateAppSettings(self)
        ########################################################################
        message = "LOADING."
        circleColor1 = QColor("#1e0880")
        circleColor2 = QColor("#000000")


        self.threadUpdateloader = Updateloader_2(message, circleColor1, circleColor2)
        self.threadUpdateloader.messagesignal.connect(self.message_signal)
        self.threadUpdateloader.circleColor1signal.connect(self.circleColor1_signal)
        self.threadUpdateloader.circleColor2signal.connect(self.circleColor2_signal)
        self.threadUpdateloader.finishedd.connect(self.finish_loading)
        self.threadUpdateloader.start()


    def circleColor1_signal(self, Color1):
        self.myParentWidget.circleColor1=Color1

    def circleColor2_signal(self, Color2):
        self.myParentWidget.circleColor2=Color2

    def message_signal(self, mensage):
        self.myParentWidget.message=mensage

    def finish_loading(self):
        QTimer.singleShot(1000, self.show_main_window)


    def show_main_window(self):
        self.threadUpdateloader.stop()
        self.close()
        self.main_window_loading = MainWindow_Login_and_Sign_Up()
        self.main_window_loading.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = LoadingScreen()
    MainWindow.show()
    sys.exit(app.exec())