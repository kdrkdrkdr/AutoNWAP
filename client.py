
from codecs import ignore_errors
from typing_extensions import final
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import time
import os, glob, shutil

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common import exceptions

from chr_drvier import DriverSession


class RunAutoPaint(QThread):
    changeValue = Signal(int)

    def __init__(self, window):
        QThread.__init__(self)
        self.window = window
        self.driver = DriverSession()

    def stop(self):
        self.terminate()


    def run(self):
        self.driver.get('https://ai.webtoons.com/painter/paint')

        # src_dir = self.window.painted_file_dir.text().replace('/', '\\')
        src_dir = r'C:\Users\power\Desktop\Project\Dev\AutoNWAP\MyImages'
        dst_dir = f'{src_dir}\\AiPaintedResult'


        imageTypes = ('jpg', 'png', 'jpeg')
        imageList = []
        for ext in imageTypes:
            imageList.extend(glob.glob(f'{src_dir}\\*.{ext}'))
        

        if (len(imageList) == 0) or (len(src_dir) == 0):
            self.window.run_paint_btn.setText('채색 시작')
            return


        for i, j in enumerate(imageList):
            try:
                self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(j)

                time.sleep(1)

                self.driver.find_element(By.XPATH, '//button[text()="채색하기"]').click()
                WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[text()="기본 모델"]')))
                time.sleep(1)

                self.driver.find_element(By.XPATH, '//*[text()="기본 모델"]').click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, f'//*[text()="{self.window.select_model_cbox.currentText()}"]').click()
                
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)


                self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/div[2]/label').click()
                self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[3]/div[2]/label').click()
                time.sleep(1)

                WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div[5]/button'))).click()
                self.driver.find_element(By.XPATH, '//*[text()="PNG로 저장하기"]').click()


                if not os.path.isdir(dst_dir): os.mkdir(dst_dir)
                
                p_src = f'./tmp/{os.path.splitext(os.path.basename(j))[0]}_ai-painter.png'
                p_dst = f'{dst_dir}\\painted_{os.path.basename(j)}'

                while not os.path.isfile(p_src): pass
                shutil.move(p_src, p_dst)


                self.window.log_browser.append(f'{dst_dir}\\painted_{os.path.basename(j)} 에 저장되었습니다.')
                self.changeValue.emit(int(100* (i+1)/len(imageList)))
                self.window.log_browser.verticalScrollBar().setValue(self.window.log_browser.verticalScrollBar().maximum())

                time.sleep(2)
            
            except (exceptions.ElementClickInterceptedException):
                print("Element Click 인터셉트!")


            finally:
                self.driver.get('https://ai.webtoons.com/painter/paint')
                
                try: Alert(self.driver).accept()
                except: pass

                time.sleep(2)
            



        self.window.log_browser.append('\n채색 완료!')
        self.window.run_paint_btn.setText('채색 시작')


