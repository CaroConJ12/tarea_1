import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QTimer
import gpiod
from datetime import datetime

LED_PIN = 4
BUTTON_PIN = 18

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button_press_count = 0
        self.button_press_times = []

        self.init_gpio()
        self.init_ui()

    def init_gpio(self):
        self.chip = gpiod.Chip('gpiochip4')
        self.DO_00 = self.chip.get_line(LED_PIN)
        self.DI_00 = self.chip.get_line(BUTTON_PIN)

        self.DO_00.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
        self.DI_00.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

    def init_ui(self):
        self.setWindowTitle("Sistema de Control")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Numero de Alarmas: 0", self)
        self.reset_button = QPushButton("Resetear Contador", self)
        self.log_label = QLabel("Históricos", self)
        self.log_text = QTextEdit(self)
        self.log_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.log_label)
        layout.addWidget(self.log_text)
        self.setLayout(layout)

        self.reset_button.clicked.connect(self.reset_counter)

        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_button_state)
        self.timer.start(100)

    def closeEvent(self, event):
        self.timer.stop()
        self.DO_00.release()
        self.DI_00.release()

    def show_message(self):
        QMessageBox.information(self, "Mensaje", "Sistema Desactivado")

    def update_counter(self):
        self.button_press_count += 1
        self.label.setText(f"Número de Alarmas: {self.button_press_count}")

    def reset_counter(self):
        self.button_press_count = 0
        self.label.setText("Número de Alarmas: 0")
        self.button_press_times = []
        self.log_text.clear()

    def check_button_state(self):
        button_state = self.DI_00.get_value()
        if button_state == 0:  # Cambiamos la condición para verificar cuando la señal del botón es baja
            self.DO_00.set_value(1)
            self.show_message()
            self.update_counter()
            self.log_button_press_time()
        else:
            self.DO_00.set_value(0)

    def log_button_press_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.button_press_times.append(current_time)
        self.update_log_text()

    def update_log_text(self):
        log_text = "\n".join(self.button_press_times)
        self.log_text.setPlainText(log_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
