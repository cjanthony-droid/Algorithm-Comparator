import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Qt
from logic import Algorithm as al


class CardWidget(QWidget):
    def __init__(self, card_name: str, path_name: str, parent=None):
        super().__init__(parent)

        self.name_label = QLabel(card_name)
        self.elapsed_time_label = QLabel("Elapsed time: 0.000 s")
        self.graph_widget = QLabel()
        self.graph_widget.setPixmap(QPixmap(f"../assets/{path_name}_complexity.png"))

        label_layout = QHBoxLayout()
        label_layout.addWidget(self.name_label)
        label_layout.addWidget(self.elapsed_time_label)

        label_layout.setAlignment(Qt.AlignLeft)
        label_layout.setSpacing(10)
        label_layout.setContentsMargins(10, 10, 10, 10)

        main_layout = QVBoxLayout()
        main_layout.addLayout(label_layout)
        main_layout.addWidget(self.graph_widget)
        self.setLayout(main_layout)

        self.setMaximumSize(200, 200)

    def set_elapsed_time(self, elapsed_time: float):
        self.elapsed_time_label.setText(f"Elapsed time: {elapsed_time:.3f} s")


# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Relative path to the image from the src directory
    widget = CardWidget("MergeSortRecur", al.ALGORITHM_NAMES[4])
    widget.show()

    sys.exit(app.exec())
