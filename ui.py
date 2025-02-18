MainWindow = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>593</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="map">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>0</y>
      <width>541</width>
      <height>521</height>
     </rect>
    </property>
    <property name="text">
     <string>под карту</string>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>163</width>
      <height>241</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QComboBox" name="maptypeBox">
       <item>
        <property name="text">
         <string>Базовая</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Автомобильная навигация</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Общественный транспорт</string>
        </property>
       </item>
       <item>
        <property name="text">
         <string>Административная</string>
        </property>
       </item>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="temaBox">
       <property name="text">
        <string>Темная тема</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="checkBox">
       <property name="text">
        <string>Индекс</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>250</y>
      <width>160</width>
      <height>101</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QTextEdit" name="findTextEdit"/>
     </item>
     <item>
      <widget class="QPushButton" name="findButton">
       <property name="text">
        <string>Искать</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>370</y>
      <width>160</width>
      <height>111</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_3">
     <item>
      <widget class="QLabel" name="adLabel">
       <property name="text">
        <string>Текущий адрес:</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="adressLabel">
       <property name="text">
        <string>вот тут адрес</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="hideButton">
       <property name="text">
        <string>Сброс</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""
