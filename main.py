from UI_MAIN import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import qdarkstyle, os

from client import RunAutoPaint
from chr_drvier import DriverSession


class AutoNWAP(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setFont(QFont('나눔고딕OTF', 10))
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        QObject.connect(self.select_file_dir_btn, SIGNAL('clicked()'), self.selectFiles)
        QObject.connect(self.open_file_dir_btn, SIGNAL('clicked()'), self.openFolder)
        QObject.connect(self.run_paint_btn, SIGNAL('clicked()'), self.runPaint)

        self.rt = RunAutoPaint(self)
        self.rt.changeValue.connect(self.progressBar.setValue)


        # self.setWindowIcon(QIcon('./utils/sayo.ico'))

        self.show()


    def runPaint(self):
        if self.run_paint_btn.text() == '채색 시작':
            self.log_browser.clear()
            self.rt.start()
            self.run_paint_btn.setText('채색 중지')
        else:
            self.rt.stop()
            self.run_paint_btn.setText('채색 시작')




    def selectFiles(self):
        dir_loc = QFileDialog.getExistingDirectory(self, 'Find Folder')
        if len(dir_loc) == 0:
            return
        self.painted_file_dir.setText(dir_loc)



    def openFolder(self):
        os.system('explorer \"{}\"'.format((self.painted_file_dir.text()).replace('/', '\\')))



if __name__ == '__main__':
    import sys
    # import ctypes
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    app = QApplication(sys.argv)
    auto_nwap = AutoNWAP()
    app.exec_()
    auto_nwap.rt.driver.quit()
