import numpy as np
from PySide6 import QtWidgets, QtGui, QtCore
import os

class SetupScreen(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.iscsv = False
        self.parent = parent  # Store the reference to the main window

        # Create the setup layout as before
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setAlignment()
        text_with_icon = QtWidgets.QHBoxLayout()

        text_a = QtWidgets.QLabel("Enter array to be sorted: ")

        icon = QtGui.QPixmap('../assets/Information.png')
        icon_label = QtWidgets.QLabel("")
        icon_label.setPixmap(icon.scaled(20, 20, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.FastTransformation))

        text_with_icon.addWidget(text_a)
        text_with_icon.addWidget(icon_label, QtCore.Qt.AlignmentFlag.AlignLeft)
        main_layout.addLayout(text_with_icon)

        # Input box
        self.input_box = QtWidgets.QPlainTextEdit()
        self.input_box.setPlaceholderText("[1,2,3,4 ...]")
        self.input_box.setMaximumHeight(200)
        input_box_padding = QtWidgets.QHBoxLayout()
        input_box_padding.setSpacing(10)

        input_box_padding.addWidget(QtWidgets.QLabel(""))
        input_box_padding.addWidget(self.input_box)
        input_box_padding.addWidget(QtWidgets.QLabel(""))
        main_layout.addLayout(input_box_padding)

        # Buttons for importing files
        file_button_layout = QtWidgets.QHBoxLayout()

        import_txt = QtWidgets.QPushButton("Import .txt")
        import_csv = QtWidgets.QPushButton("Import .csv")

        # Connect buttons to their respective functions
        import_txt.clicked.connect(self.import_txt_file)
        import_csv.clicked.connect(self.import_csv_file)

        file_button_layout.addWidget(import_txt)
        file_button_layout.addWidget(import_csv)

        main_layout.addLayout(file_button_layout)

        # Preview layout
        preview_layout = QtWidgets.QVBoxLayout()

        preview_text = QtWidgets.QLabel("Preview")
        self.preview_box = QtWidgets.QPlainTextEdit()
        self.preview_box.setReadOnly(True)
        self.preview_content = "[1,2,3,4 ...]"
        self.preview_box.setPlaceholderText(self.preview_content)
        self.preview_box.setMaximumHeight(200)

        nav_layout = QtWidgets.QHBoxLayout()

        self.verify_btn = QtWidgets.QPushButton("Verify")
        self.continue_btn = QtWidgets.QPushButton("Continue")
        self.continue_btn.setStyleSheet("background-color: red;")  # Start with red background
        self.verify_btn.clicked.connect(self.verify_input)  # Connect the verify button
        self.continue_btn.clicked.connect(self.switch_to_result_screen)  # Connect to the screen switch method

        nav_layout.addWidget(self.verify_btn)
        nav_layout.addWidget(self.continue_btn)
        preview_layout.addWidget(preview_text)
        preview_layout.addWidget(self.preview_box)
        preview_layout.addLayout(nav_layout)

        main_layout.addLayout(preview_layout)

    def switch_to_result_screen(self):
        """Switch to the result screen via the parent window."""
        # Get the NumPy array from the preview box
        if self.continue_btn.styleSheet() != "background-color: green;":
            return  # Do nothing if the button is not green
        preview_text = self.preview_box.toPlainText().strip()
        array = self.convert_to_array(preview_text)

        if array is not None:
            self.parent.show_result_screen(array)

    def import_txt_file(self):
        """Open a file dialog to import .txt files from the project's directory."""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Text File", os.getcwd(), "Text Files (*.txt)")
        if file_path:
            self.load_file(file_path)
            self.iscsv = False

    def import_csv_file(self):
        """Open a file dialog to import .csv files from the project's directory."""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open CSV File", os.getcwd(), "CSV Files (*.csv)")
        if file_path:
            self.load_file(file_path)
            self.iscsv = True

    def load_file(self, file_path):
        """Load the selected file's contents into the preview box."""
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                # Load the file content into the preview_box instead of the input_box
                self.preview_box.setPlainText(data)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"Failed to load the file: {e}")

    def verify_input(self):
        """Verify user-entered data or file-imported data."""
        # Step 1: Check user-entered data in the input box
        input_text = self.input_box.toPlainText().strip()

        if input_text:
            # Try to convert user input into a NumPy array
            array = self.convert_to_array(input_text)
            if array is not None:
                self.preview_box.setPlainText(input_text)  # If valid, mirror into preview box
                self.continue_btn.setStyleSheet("background-color: green;")  # Change button to green
            else:
                self.show_error_message("Invalid input in the input box. Please enter a valid list of numbers.")
            return  # Exit after checking input box

        # Step 2: Check if the preview box has imported data only if input box is empty
        preview_text = self.preview_box.toPlainText().strip()

        if preview_text:
            if self.convert_to_array(preview_text) is None:
                self.show_error_message("Invalid data in the preview box. Please import a valid file or enter correct data.")
            else:
                self.preview_box.setPlainText(preview_text)  # If valid, mirror into preview box
                self.continue_btn.setStyleSheet("background-color: green;")  # Change button to green
    def convert_to_array(self, text):
        """Try to convert a string to a NumPy array of numbers."""
        try:
            if self.iscsv:
                clean_text = ','.join([x.strip() for x in text.split('\n') if x.strip()]).split(',',1)[1]
            else:
                clean_text = ','.join([x.strip() for x in text.split(',') if x.strip()])  # Remove empty parts
            # Evaluate the cleaned input text and attempt to convert it to a NumPy array
            array = np.fromstring(clean_text, sep=',')
            return array  # Return the NumPy array if successful
        except:
            return None  # Return None if the conversion fails

    def show_error_message(self, message):
        """Show a pop-up error message."""
        QtWidgets.QMessageBox.warning(self, "Error", message)