import sys
from PySide6 import QtWidgets
from setup_screen import SetupScreen
from result_screen import ResultScreen

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to manage different screens
        self.times = None
        self.array = None
        self.stacked_widget = QtWidgets.QStackedWidget()

        # Create the setup and result screens
        self.setup_screen = SetupScreen(self)
        self.result_screen = ResultScreen(self)

        # Add the screens to the QStackedWidget
        self.stacked_widget.addWidget(self.setup_screen)   # Index 0
        self.stacked_widget.addWidget(self.result_screen)  # Index 1

        # Set the QStackedWidget as the central widget of the main window
        self.setCentralWidget(self.stacked_widget)

    def show_result_screen(self, array):
        self.array = array
        self.result_screen.display_results(array)
        self.stacked_widget.setCurrentWidget(self.result_screen)
        
    
            
            
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

