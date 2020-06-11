# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diceroller2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
"""
This is a dicerolling app for (primarily) DND 5E.  it is built using PyQt5
using the designer app to make the GUI, then coding up all the buttons and logic
this is my second version of the app. using it to teach myself.  
this version included logging and a bunch of buttons, labels, checkboxes
spin boxes etc.  

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import logging

from PySide2.QtTextToSpeech import QTextToSpeech, QVoice

logging.basicConfig(
    filename = 'logfile.txt',
    level = logging.DEBUG)

def dice(r):
    # this is my main roller
    roll = random.randint(1, r)
    # str_roll = str(roll)
    # say(str_roll)
    return(roll)

crit_roll = False

def say(s):
    # this is my text to speech setup
    engine = None
    engineNames = QTextToSpeech.availableEngines()
    if len(engineNames) > 0:
        engineName = engineNames[0]
        engine = QTextToSpeech(engineName)
    engine.say(s)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.die_size = 4
        self.stat_bonus = 0
        self.text = 'Roll'
        self.engine = None
        self.curse_bonus = 0
        self.hex_bonus = False
        self.crit_on_19 = False
        self.halforc = False
        self.advantage = False
        self.disadvantage = False

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 91, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 91, 16))
        self.label_4.setObjectName("label_4")

        self.label_sneak_attack_dice = QtWidgets.QLabel(self.centralwidget)
        self.label_sneak_attack_dice.setGeometry(QtCore.QRect(40, 190, 110, 16))
        self.label_sneak_attack_dice.setObjectName("sneak attack dice")

        self.label_initiative_result = QtWidgets.QLabel(self.centralwidget)
        self.label_initiative_result.setGeometry(QtCore.QRect(460, 40, 60, 16))
        self.label_initiative_result.setObjectName("label_initiative_result")

        self.label_attack_roll = QtWidgets.QLabel(self.centralwidget)
        self.label_attack_roll.setGeometry(QtCore.QRect(340, 120, 60, 16))
        self.label_attack_roll.setObjectName("label_attack_roll")

        self.pushButton_attack_roll = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_attack_roll.setGeometry(QtCore.QRect(220, 120, 113, 51))
        self.pushButton_attack_roll.setObjectName("pushButton_attack_roll")
        self.pushButton_attack_roll.clicked.connect(self.attack_clicked)

        self.checkBox_include_stat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_include_stat.setGeometry(QtCore.QRect(40, 70, 191, 20))
        self.checkBox_include_stat.setObjectName("checkBox_include_stat")
        self.checkBox_include_stat.stateChanged.connect(self.stat_clicked)

        self.checkBox_include_hex = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_include_hex.setGeometry(QtCore.QRect(40, 90, 191, 20))
        self.checkBox_include_hex.setObjectName("checkBox_include_hex")
        self.checkBox_include_hex.stateChanged.connect(self.hex_clicked)

        self.checkBox_include_curse = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_include_curse.setGeometry(QtCore.QRect(40, 110, 191, 20))
        self.checkBox_include_curse.setObjectName("checkBox_include_curse")
        self.checkBox_include_curse.stateChanged.connect(self.curse_clicked)

        self.checkBox_is_halforc = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_is_halforc.setGeometry(QtCore.QRect(40, 130, 191, 20))
        self.checkBox_is_halforc.setObjectName("checkBox_is_halforc")
        self.checkBox_is_halforc.stateChanged.connect(self.is_halforc)

        self.checkBox_is_champion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_is_champion.setGeometry(QtCore.QRect(40, 150, 191, 20))
        self.checkBox_is_champion.setObjectName("checkBox_is_champion")
        self.checkBox_is_champion.stateChanged.connect(self.is_champion)

        self.checkBox_advantage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_advantage.setGeometry(QtCore.QRect(240, 70, 191, 20))
        self.checkBox_advantage.setObjectName("checkBox_advantage")
        self.checkBox_advantage.stateChanged.connect(self.has_advantage)

        self.checkBox_disadvantage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_disadvantage.setGeometry(QtCore.QRect(240, 90, 191, 20))
        self.checkBox_disadvantage.setObjectName("checkBox_disadvantage")
        self.checkBox_disadvantage.stateChanged.connect(self.has_disadvantage)

        self.engine = None

        self.combo_box_damage_dice = QtWidgets.QComboBox(self.centralwidget)
        self.combo_box_damage_dice.setGeometry(QtCore.QRect(40, 200, 101, 121))
        self.combo_box_damage_dice.setObjectName("combo_box_damage_dice")
        self.combo_box_damage_dice.addItem("D4", 4)
        self.combo_box_damage_dice.addItem("D6", 6)
        self.combo_box_damage_dice.addItem("D8", 8)
        self.combo_box_damage_dice.addItem("D10", 10)
        self.combo_box_damage_dice.addItem("D12", 12)
        self.combo_box_damage_dice.activated.connect(self.handleActivated)

        self.pushButton_D4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D4.setGeometry(QtCore.QRect(30, 290, 110, 25))
        self.pushButton_D4.setObjectName("pushButton_D4")
        self.pushButton_D4.clicked.connect(lambda:self.random_roll(4))

        self.pushButton_D6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D6.setGeometry(QtCore.QRect(30, 310, 110, 25))
        self.pushButton_D6.setObjectName("pushButton_D6")
        self.pushButton_D6.clicked.connect(lambda:self.random_roll(6))

        self.pushButton_D8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D8.setGeometry(QtCore.QRect(30, 330, 110, 25))
        self.pushButton_D8.setObjectName("pushButton_D8")
        self.pushButton_D8.clicked.connect(lambda:self.random_roll(8))

        self.pushButton_D10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D10.setGeometry(QtCore.QRect(30, 350, 110, 25))
        self.pushButton_D10.setObjectName("pushButton_D10")
        self.pushButton_D10.clicked.connect(lambda:self.random_roll(10))

        self.pushButton_D12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D12.setGeometry(QtCore.QRect(30, 370, 110, 25))
        self.pushButton_D12.setObjectName("pushButton_D12")
        self.pushButton_D12.clicked.connect(lambda:self.random_roll(12))

        self.pushButton_D20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_D20.setGeometry(QtCore.QRect(30, 390, 110, 25))
        self.pushButton_D20.setObjectName("pushButton_D20")
        self.pushButton_D20.clicked.connect(lambda:self.random_roll(20))

        self.pushButton_roll_initiative = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_roll_initiative.setGeometry(QtCore.QRect(330, 30, 110, 25))
        self.pushButton_roll_initiative.setObjectName("pushButton_roll_initiative")
        self.pushButton_roll_initiative.clicked.connect(self.initiative_roll)

        self.label_dam_roll = QtWidgets.QLabel(self.centralwidget)
        self.label_dam_roll.setGeometry(QtCore.QRect(340, 150, 60, 16))
        self.label_dam_roll.setObjectName("label_dam_roll")
        self.label_dam_final = QtWidgets.QLabel(self.centralwidget)
        self.label_dam_final.setGeometry(QtCore.QRect(420, 150, 60, 16))
        self.label_dam_final.setObjectName("label_dam_final")
        self.label_attack_final = QtWidgets.QLabel(self.centralwidget)
        self.label_attack_final.setGeometry(QtCore.QRect(420, 120, 60, 16))
        self.label_attack_final.setObjectName("label_attack_final")
        self.label_random_roll = QtWidgets.QLabel(self.centralwidget)
        self.label_random_roll.setGeometry(QtCore.QRect(200, 270, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_random_roll.setFont(font)
        self.label_random_roll.setIndent(40)
        self.label_random_roll.setObjectName("label_random_roll")

        self.spinBox_prof_bonus = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_prof_bonus.setGeometry(QtCore.QRect(170, 10, 61, 24))
        self.spinBox_prof_bonus.setMaximum(6)
        self.spinBox_prof_bonus.setProperty("value", 0)
        self.spinBox_prof_bonus.setObjectName("spinBox")
        
        self.spinBox_stat_bonus = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_stat_bonus.setGeometry(QtCore.QRect(170, 30, 61, 24))
        self.spinBox_stat_bonus.setMaximum(10)
        self.spinBox_stat_bonus.setProperty("value", 0)
        self.spinBox_stat_bonus.setObjectName("spinBox_2")
        
        self.spinBox_magic_bonus = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_magic_bonus.setGeometry(QtCore.QRect(170, 50, 61, 24))
        self.spinBox_magic_bonus.setMaximum(3)
        self.spinBox_magic_bonus.setProperty("value", 0)
        self.spinBox_magic_bonus.setObjectName("spinBox_3")
        
        self.spinBox_initiative_bonus = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_initiative_bonus.setGeometry(QtCore.QRect(450, 10, 61, 24))
        self.spinBox_initiative_bonus.setMaximum(15)
        self.spinBox_initiative_bonus.setProperty("value", 0)
        self.spinBox_initiative_bonus.setObjectName("spinBox_4")

        self.spinBox_sneak_attack_dice = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_sneak_attack_dice.setGeometry(QtCore.QRect(170, 190, 61, 24))
        self.spinBox_sneak_attack_dice.setMaximum(10)
        self.spinBox_sneak_attack_dice.setProperty("value", 0)
        self.spinBox_sneak_attack_dice.setObjectName("SneakAttackDice")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DnD roller 2.0"))
        self.label.setText(_translate("MainWindow", "Prof Bonus"))
        self.label_2.setText(_translate("MainWindow", "Stat Bonus"))
        self.label_3.setText(_translate("MainWindow", "Magic Bonus"))
        self.label_4.setText(_translate("MainWindow", "Initiative Bonus"))
        self.label_initiative_result.setText(_translate("MainWindow", "Result"))
        self.label_attack_roll.setText(_translate("MainWindow", "Atk roll"))
        self.pushButton_attack_roll.setText(_translate("MainWindow", "Attack"))
        self.checkBox_include_stat.setText(_translate("MainWindow", "Include Stat in damage roll"))
        self.checkBox_include_hex.setText(_translate("MainWindow", "Include Hex in damage roll"))
        self.checkBox_include_curse.setText(_translate("MainWindow", "Include Hexblade's Curse"))
        self.checkBox_is_champion.setText(_translate("MainWindow","Champion subclass"))
        self.checkBox_is_halforc.setText(_translate("MainWindow", "Half Orc Race"))
        self.checkBox_advantage.setText(_translate("MainWindow", "Advantage on atk"))
        self.checkBox_disadvantage.setText(_translate("MainWindow", "disadvantage on atk"))
        self.pushButton_D4.setText(_translate("MainWindow", "D4"))
        self.pushButton_D6.setText(_translate("MainWindow", "D6"))
        self.pushButton_D8.setText(_translate("MainWindow", "D8"))
        self.pushButton_D10.setText(_translate("MainWindow", "D10"))
        self.pushButton_D12.setText(_translate("MainWindow", "D12"))
        self.pushButton_D20.setText(_translate("MainWindow", "D20"))
        self.pushButton_roll_initiative.setText(_translate("MainWindow", "Roll Initiative"))
        self.label_dam_roll.setText(_translate("MainWindow", "Dam roll"))
        self.label_dam_final.setText(_translate("MainWindow", "Dam Final"))
        self.label_attack_final.setText(_translate("MainWindow", "Atk Final"))
        self.label_random_roll.setText(_translate("MainWindow", "Roll"))
        self.label_sneak_attack_dice.setText(_translate("MainWindow", "Sneak Attack Dice"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


    def attack_clicked(self):
        
   
        global crit_roll
        roll = dice(20)
        roll2 = dice(20)
        logging.debug("NEW ATTACK =============")
        logging.debug("Roll1: " + str(roll))
        logging.debug("Roll2: " + str(roll2))

        if self.advantage == True and roll2 > roll:
            logging.debug("using second roll")
            roll = roll2
        if self.disadvantage == True and roll2 < roll:
            logging.debug("Using second roll")
            roll = roll2

        prof_bonus = self.spinBox_prof_bonus.value()
        magic_bonus = self.spinBox_magic_bonus.value()
        stat_bonus = self.spinBox_stat_bonus.value()
        damage_dice = self.die_size

        if roll == 20:
            crit_roll = True
            logging.debug('CRIT')
        if roll == 19 and self.crit_on_19 == True:
            crit_roll = True
            logging.debug('CRIT')
        roll_with_mods = roll + prof_bonus + magic_bonus + stat_bonus
        # logging.debug('attack roll ' + str(roll))
        logging.debug('final attack: ' + str(roll_with_mods))
        self.label_attack_roll.setText(str(roll))
        self.label_attack_roll.repaint()
        self.label_attack_final.setText(str(roll_with_mods))
        self.label_attack_final.repaint()
        self.damage_roll(damage_dice)


    def damage_roll(self, die_size):
        magic_bonus = self.spinBox_magic_bonus.value()
        # stat_bonus = self.spinBox_stat_bonus.value()
        raw_damage = dice(die_size)
        global crit_roll
        crit_damage = 0

        # if the attack is a crit, you get to add an extra damage dice roll
        if crit_roll == True:
            crit_damage = dice(die_size)

        # if the player is a half orc race, they get ANOTHER extra dice on a crit
        if self.halforc == True and crit_roll == True:
            crit_damage = crit_damage + dice(die_size)

        # hexblade's curse is a bonus action. adds PROF modifier to damage roll
        hexblade_damage = self.curse_bonus

        # hex is a spell warlocks cast, causing all subsequent attacks to deal an extra d6
        hex_damage = 0
        if self.hex_bonus == True:
            hex_damage = dice(6) + dice(6) if crit_roll == True else dice(6)
        # Sneak attack is a rogue ability to add damage to an attack
        # this adds whatever number of D6s indicated by the spinbox
        SA_dice = self.spinBox_sneak_attack_dice.value()
        sneak_attack_damage = sum(dice(6) for _ in range(SA_dice))
        if crit_roll == True:
            for _ in range(SA_dice):
                sneak_attack_damage += dice(6)
    

        logging.debug('sneak attack damage: ' + str(sneak_attack_damage))
        logging.debug('hexblade curse damage: ' +str(hexblade_damage))
        logging.debug('hex damage: ' +str(hex_damage))
        logging.debug('stat bonus: ' +str(self.stat_bonus))
        logging.debug('magic bonus: ' +str(magic_bonus))
        logging.debug('damageroll: ' +str(raw_damage))
        logging.debug('crit damage: ' +str(crit_damage))
        final_damage = raw_damage + crit_damage + magic_bonus + self.stat_bonus + hexblade_damage + hex_damage + sneak_attack_damage
        logging.debug('final damage: ' + str(final_damage))

        self.label_dam_roll.setText(str(raw_damage))
        self.label_dam_roll.repaint()
        self.label_dam_final.setText(str(final_damage))
        self.label_dam_final.repaint()
        crit_roll = False
    

    def handleActivated(self, index):
        self.die_size = self.combo_box_damage_dice.itemData(index)


    def random_roll(self, r):
        random = dice(r)
        str_r = str(r)
        str_random = str(random)
        self.label_random_roll.setText(str_random)
        self.label_random_roll.repaint()
        logging.debug('randomroll:' +str_r + ': '+ str_random)


# these are the 5 optional checkboxes
# the first is whether stat bonus gets included in the damage.  for a cantrip, its usually no
# for a weapon using the proper bonus, you get to add your stat to the damage
# for example, a fighter using a longsword in his main hand gets to add his STR to both the
# attack roll and the damage roll
# Hex is for a warlock using the hex spell to add 1d6 to all attacks on that creature
# hexblade's curse is for a hexblade warlock that gets to add his PROF bonus to damage


    def stat_clicked(self, state):
        if state == QtCore.Qt.Checked:
            self.stat_bonus = self.spinBox_stat_bonus.value()
        else:
            self.stat_bonus = 0

    def hex_clicked(self, state):
        # when the warlock attacks a target with hex, they add D6 damage
        # this value gets added to a dice(r) in the damage roll
        if state == QtCore.Qt.Checked:
            self.hex_bonus = True
            logging.debug('HEX SPELL')
        else:
            self.hex_bonus = False

    def curse_clicked(self, state):
        # hexblade's curse lets the hexblade add their prof score to damage
        if state == QtCore.Qt.Checked:
            self.curse_bonus = self.spinBox_prof_bonus.value()
            self.crit_on_19 = True
            logging.debug('HEXBLADE CURSE')
        else:
            self.curse_bonus = 0

    def is_halforc(self, state):
        # half orcs get an extra dice on crit hits
        if state == QtCore.Qt.Checked:
            self.halforc = True
            logging.debug('HALF ORC')
        else:
            self.halforc = False
    
    def is_champion(self, state):
        # champion fighter subclass gets to crit on a 19
        if state == QtCore.Qt.Checked:
            self.crit_on_19 = True
            logging.debug('CHAMPION')
        else:
            self.crit_on_19 = False

    def has_advantage(self, state):
        # advantage lets you roll 2 D20s and use the higher roll
        self.advantage = True if state == QtCore.Qt.Checked else False

    def has_disadvantage(self, state):
        # disadvantage means you roll 2 d20, use the lower roll
        self.disadvantage = True if state == QtCore.Qt.Checked else False

    def say(self):
        self.engine.setVoice('Alex')
        self.engine.setVolume(45)
        self.engine.say(self.text)

    def initiative_roll(self):
        # this is for the initiative roller in the top right corner
        initiative_bonus = 0        
        initiative_bonus = self.spinBox_initiative_bonus.value()    
        initiative = dice(20) + initiative_bonus
        str_initiative = str(initiative)
        say(str_initiative)
        logging.debug('initiative ' + str_initiative)
        self.label_initiative_result.setText(str_initiative)
        self.label_initiative_result.repaint()
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
