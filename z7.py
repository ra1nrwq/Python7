from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMenuBar, QMenu
from PyQt6.QtGui import QAction  
import sys

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Приложение для заметок")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('Файл')

        new_action = QAction('Новая заметка', self)
        new_action.triggered.connect(self.new_note)
        file_menu.addAction(new_action)

        save_action = QAction('Сохранить заметку', self)
        save_action.triggered.connect(self.save_note)
        file_menu.addAction(save_action)
        
    def new_note(self):
        self.text_edit.clear()

    def save_note(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить заметку", "", "Text Files (*.txt);;All Files (*)")
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())  
app = QApplication(sys.argv)
window = NoteApp()
window.show()
sys.exit(app.exec())
