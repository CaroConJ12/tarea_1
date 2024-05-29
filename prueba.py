import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QColor
import gpiod

# Definir los pines GPIO para los botones y las salidas
BUTTON_PIN_ACTIVATE = 22
BUTTON_PIN_DEACTIVATE = 23
OUTPUT_PIN_ACTIVATE = [14, 15, 18]
OUTPUT_PIN_DEACTIVATE = 17

# Configurar los pines GPIO
chip = gpiod.Chip('gpiochip0')
button_line_activate = chip.get_line(BUTTON_PIN_ACTIVATE)
button_line_deactivate = chip.get_line(BUTTON_PIN_DEACTIVATE)
output_line_activate = chip.get_line(OUTPUT_PIN_ACTIVATE)
output_line_deactivate = chip.get_line(OUTPUT_PIN_DEACTIVATE)

button_line_activate.request(consumer="ButtonActivate", type=gpiod.LINE_REQ_EV_BOTH_EDGES)
button_line_deactivate.request(consumer="ButtonDeactivate", type=gpiod.LINE_REQ_EV_BOTH_EDGES)
output_line_activate.request(consumer="LEDActivate", type=gpiod.LINE_REQ_DIR_OUT)
output_line_deactivate.request(consumer="LEDDeactivate", type=gpiod.LINE_REQ_DIR_OUT)

app = QApplication(sys.argv)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Control de Sistema")
        self.setGeometry(100, 100, 300, 150)

    def show_activation_message(self):
        QMessageBox.information(self, 'Sistema Activo', 'El sistema está activo.')
        output_line_activate.set_value(1)

    def show_deactivation_message(self):
        QMessageBox.information(self, 'Sistema Desactivado', 'El sistema está desactivado.')
        output_line_deactivate.set_value(1)

def event_handler(event):
    if event.line == button_line_activate:
        if event.event_type == gpiod.LineEvent.TYPE_RISING_EDGE:
            window.show_activation_message()
        else:
            output_line_activate.set_value(0)
    elif event.line == button_line_deactivate:
        if event.event_type == gpiod.LineEvent.TYPE_RISING_EDGE:
            window.show_deactivation_message()
        else:
            output_line_deactivate.set_value(0)

window = MainWindow()

try:
    while True:
        event = chip.event_wait(1)
        if event:
            event_handler(event)

except KeyboardInterrupt:
    button_line_activate.release()
    button_line_deactivate.release()
    output_line_activate.release()
    output_line_deactivate.release()

sys.exit(app.exec_())
