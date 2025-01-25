import concurrent.futures

import numpy as np
from PySide6 import QtWidgets, QtCore
from logic import Algorithm as algo


class ResultScreen(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent  # Store the reference to the main window
        self.timeOutput = "Loading ..."
        # Create the layout for the results screen
        main_layout = QtWidgets.QVBoxLayout(self)

        compare_label = QtWidgets.QLabel("Algorithm Chart:")
        main_layout.addWidget(compare_label)

        self.compare_box = QtWidgets.QPlainTextEdit(self.timeOutput)
        self.compare_box.setReadOnly(True)
        self.compare_box.setMaximumHeight(300)
        main_layout.addWidget(self.compare_box)

        self.executor = concurrent.futures.ThreadPoolExecutor()

        # Add a label for the results
        results_label = QtWidgets.QLabel("Sorted Results:")
        main_layout.addWidget(results_label)

        # Add a text box to display the NumPy array
        self.results_box = QtWidgets.QPlainTextEdit()
        self.results_box.setReadOnly(True)
        self.results_box.setMaximumHeight(100)
        main_layout.addWidget(self.results_box)

        # Optionally add a button to return to the setup screen
        back_btn = QtWidgets.QPushButton("Back to Setup")
        back_btn.clicked.connect(self.back_to_setup)
        main_layout.addWidget(back_btn)

    def display_results(self, array):
        """Display the NumPy array in the results screen."""
        sorted_array = np.sort(array)
        if array.size <= 40:
            sorted_array = ', '.join(f"{num:.2f}" if num % 1 != 0 else str(int(num)) for num in sorted_array)
        else:
            sorted_array = f"[{', '.join(f'{num:.2f}' if num % 1 != 0 else str(int(num)) for num in sorted_array[:20])} ... {', '.join(f'{num:.2f}' if num % 1 != 0 else str(int(num)) for num in sorted_array[-20:])}]"


        self.results_box.setPlainText(sorted_array)
        self.run_compare(array)

    def back_to_setup(self):
        """Return to the setup screen."""
        self.parent.show_setup_screen()  # Implement this in your main window

    def time_table(self):
        ph = "Timeout Value"
        timeout = 5
        timeOutput = f"  {ph:<18} |   {timeout}.00s\n"
        timeOutput += "--------------------------------\n"
        for e in self.parent.times:
            timeOutput += f"  {e[0]:<18} |   {e[1]}s\n"
        return timeOutput

    def run_compare(self, array):
        if array is not None:
            # Submit the task to the thread pool and specify the callback
            future = self.executor.submit(self.run_sorting_algorithms, array)
            future.add_done_callback(self.update_compare_box)

    def run_sorting_algorithms(self, array):
        # Run sorting algorithms and store times in parent
        self.parent.times = algo.run_times(array)
        # Return the time table text
        return self.time_table()

    def update_compare_box(self, future):
        try:
            # Retrieve the result (time table) from the future
            result = future.result()
            # Update the compare_box on the main thread
            QtCore.QMetaObject.invokeMethod(self.compare_box, "setPlainText",
                                            QtCore.Qt.QueuedConnection,
                                            QtCore.Q_ARG(str, result))
        except Exception as e:
            print(f"Error: {e}")
