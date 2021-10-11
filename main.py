from PySide2 import QtWidgets

app = QtWidgets.QApplication([])

win = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout()
button = QtWidgets.QPushButton("Useless button")

layout.addWidget(QtWidgets.QLabel('Label text'))
layout.addWidget(button)

win.setLayout(layout)
win.show()
app.exec_()
