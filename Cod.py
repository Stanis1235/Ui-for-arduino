from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app = QtWidgets.QApplication([])
ui = uic.loadUi("Ui.ui")
ui.setWindowTitle("Ui for arduino")

serial = QSerialPort()
serial.setBaudRate(115200)

def ComboBoxReset():
    ui.comboBox.clear()
    PortsList = []
    Ports = QSerialPortInfo().availablePorts()
    for port in Ports:
        PortsList.append(port.portName())
    ui.comboBox.addItems(PortsList)

ComboBoxReset()

def OpenPort():
    serial.setPortName(ui.comboBox.currentText())
    serial.open(QIODevice.ReadWrite)

def ClosePort():
    serial.close()


def PrintTextEdit():
    serial.write(("*" + ui.textEdit.toPlainText() + "*").encode())

def PrintPushButton():
    serial.write(("0PushButton0").encode())

def PrintHorizontalSlider(value):
    serial.write(("-" + str(value) + "-").encode())

def PrintVerticalSlider(value):
    serial.write(("|" + str(value) + "|").encode())

def PrintDial(value):
    serial.write(("@" + str(value) + "@").encode())

def PrintcheckBox():
    mensagem = 0

    if ui.checkBox.checkState() == 2: mensagem = 1

    serial.write(( "#" + str(mensagem) + "#").encode())


ui.OpenButton.clicked.connect(OpenPort)
ui.CloseButton.clicked.connect(ClosePort)
ui.ResetButton.clicked.connect(ComboBoxReset)

ui.PrintButton.clicked.connect(PrintTextEdit)

ui.checkBox.stateChanged.connect(PrintcheckBox)

ui.pushButton.clicked.connect(PrintPushButton)

ui.verticalSlider.valueChanged.connect(PrintVerticalSlider)
ui.horizontalSlider.valueChanged.connect(PrintHorizontalSlider)
ui.dial.valueChanged.connect(PrintDial)

ui.show()
app.exec()