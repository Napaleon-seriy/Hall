import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit

vibor_zala = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>603</width>
    <height>135</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="addZalBtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>271</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать зал</string>
    </property>
   </widget>
   <widget class="QPushButton" name="viborZalaBtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>40</y>
      <width>601</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Выбрать зал для работы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="redactZalBtn">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>0</y>
      <width>331</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Отредактировать зал</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>603</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


august = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>773</width>
    <height>633</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="ok">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>210</y>
      <width>61</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>ok</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="del_big_x">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>30</y>
      <width>41</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>50</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>y</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_start_x">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>150</y>
      <width>51</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="otpravit">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>80</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>отправить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="otpravit_2">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>80</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>отправить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ok_2">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>250</y>
      <width>61</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>ok</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>31</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>количество мест:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_k_x">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>130</y>
      <width>41</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="del_place">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>40</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>удалить место</string>
    </property>
   </widget>
   <widget class="QPushButton" name="show_hall">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>510</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>показ зала</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ok_3">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>160</y>
      <width>61</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>ok</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="add_big_y">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>50</y>
      <width>41</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>30</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>x</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>180</y>
      <width>16</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>y</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_13">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>130</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>координат, и </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_17">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>220</y>
      <width>16</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>y</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_15">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>170</y>
      <width>151</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>высота и ширина места:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add_place">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>0</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>добавить место</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>11</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Удалить большое</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_shir">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>190</y>
      <width>51</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="done">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>550</y>
      <width>91</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>готово</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>130</y>
      <width>221</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>раставлять через кажое </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>49</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>y</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>10</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить большое</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>29</y>
      <width>55</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>x</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>30</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>количество мест:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_14">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>130</y>
      <width>81</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>координат</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_visota">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>220</y>
      <width>51</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>291</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>С каких координат начинать раставление мест:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_k_y">
    <property name="geometry">
     <rect>
      <x>630</x>
      <y>130</y>
      <width>41</width>
      <height>22</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="add_dig_x">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>29</y>
      <width>41</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_16">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>190</y>
      <width>16</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>x</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add_scene">
    <property name="geometry">
     <rect>
      <x>2</x>
      <y>10</y>
      <width>101</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить сцену</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="del_big_y">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>51</y>
      <width>41</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>150</y>
      <width>21</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>x</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="koord_start_y">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>180</y>
      <width>51</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>773</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

show_hall = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1100</width>
    <height>840</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
 </widget>
 <resources/>
 <connections/>
</ui>
'''



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(vibor_zala)
        uic.loadUi(f, self)
        self.addZalBtn.clicked.connect(self.createzal)
        # self.viborZalaBtn.clicked.connect(self.new_plan)
        # self.redactZalBtn.clicked.connect(self.new_plan)

    def createzal(self):
        self.w = Zalappend()
        ex.close()
        self.w.show()

    '''def redactzal(self):
        w2 = '''


class Zalappend(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(august)
        uic.loadUi(f, self)
        self.scn = False
        self.add_scene.clicked.connect(self.added_scene)
        self.otpravit.clicked.connect(self.otpravite)
        self.ok.clicked.connect(self.oke)
        self.ok_2.clicked.connect(self.oke2)
        self.ok_3.clicked.connect(self.oke3)
        self.show_hall.clicked.connect(self.showing_hall)

    def added_scene(self):
        global scn
        scn = True

    def otpravite(self):
        global kax, kay
        kax = int(QLineEdit.koord_add_x.text())
        kay = int(QLineEdit.koord_add_y.text())
        '''self.txtfile()'''

    def oke(self):
        global ksx, ksy
        ksx = int(QLineEdit.koord_start_x.text())
        ksy = int(QLineEdit.koord_start_y.text())

    def oke2(self):
        global ksh, kv
        ksh = int(QLineEdit.koord_shir.text())
        kv = int(QLineEdit.koord_visota.text())

    def oke3(self):
        global kkx, kky
        kkx = int(QLineEdit.koord_k_x.text())
        kky = int(QLineEdit.koord_k_y.text())

    def showing_hall(self):
        self.w1 = SwimHall()
        self.w1.show()

    def txtfile(self):
        global txt
        txt = [self.scn]
        ''', self.kax, self.kay, self.ksx, self.ksy, self.ksh, self.kv, self.kkx, self.kky'''

class SwimHall(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(show_hall)
        uic.loadUi(f, self)
        self.sozidanie()

    def sozidanie(self):
        if scn == True:
            scene = QPushButton('Сцена', self)
            scene.resize(1100, 40)
            scene.move(0, 0)
        placenum = 1
        place = QPushButton(placenum, self)
        place.resize(ksh, kv)
        place.move(ksx, ksy)
        for i in range(kay):
            for j in range(kax):
                place = QPushButton(placenum, self)
                place.resize(ksh, kv)
                ksx += ksh + kax
                place.move(ksx, ksy)
                placenum += 1
            place = QPushButton(placenum, self)
            place.resize(ksh, kv)
            ksy += kv + kay
            place.move(ksx, ksy)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())