from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QTableWidget, QTableWidgetItem, QStackedWidget, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Hotel')
        self.setGeometry(100, 100, 400, 300)

        # Create StackedWidget to manage different views
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Main Menu
        self.main_menu = QWidget()
        self.main_menu_layout = QVBoxLayout()
        self.main_menu.setLayout(self.main_menu_layout)
        
        self.main_menu_layout.addWidget(QLabel('<h1>Aplikasi Hotel</h1>'))

        self.register_button = QPushButton('Daftar Tamu')
        self.register_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.register_button.clicked.connect(self.show_register_guest)
        self.main_menu_layout.addWidget(self.register_button)

        self.booking_button = QPushButton('Pesan Kamar')
        self.booking_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.booking_button.clicked.connect(self.show_room_booking)
        self.main_menu_layout.addWidget(self.booking_button)

        self.status_button = QPushButton('Status Kamar')
        self.status_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.status_button.clicked.connect(self.show_room_status)
        self.main_menu_layout.addWidget(self.status_button)
        
        self.stacked_widget.addWidget(self.main_menu)

        # Guest Registration
        self.guest_registration = QWidget()
        self.guest_registration_layout = QFormLayout()
        self.guest_registration.setLayout(self.guest_registration_layout)
        
        self.guest_registration_layout.addRow(QLabel('<h2>Pendaftaran Tamu</h2>'))
        
        self.name_input = QLineEdit()
        self.guest_registration_layout.addRow('Nama:', self.name_input)
        
        self.id_input = QLineEdit()
        self.guest_registration_layout.addRow('ID:', self.id_input)
        
        self.register_guest_button = QPushButton('Daftar')
        self.register_guest_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.guest_registration_layout.addRow(self.register_guest_button)
        
        self.back_button1 = QPushButton('Kembali ke Menu Utama')
        self.back_button1.setStyleSheet("font-size: 16px; padding: 10px;")
        self.back_button1.clicked.connect(self.show_main_menu)
        self.guest_registration_layout.addRow(self.back_button1)
        
        self.stacked_widget.addWidget(self.guest_registration)

        # Room Booking
        self.room_booking = QWidget()
        self.room_booking_layout = QFormLayout()
        self.room_booking.setLayout(self.room_booking_layout)
        
        self.room_booking_layout.addRow(QLabel('<h2>Pemesanan Kamar</h2>'))
        
        self.booking_name_input = QLineEdit()
        self.room_booking_layout.addRow('Nama:', self.booking_name_input)
        
        self.room_type_input = QComboBox()
        self.room_type_input.addItems(['Single', 'Double', 'Suite'])
        self.room_booking_layout.addRow('Tipe Kamar:', self.room_type_input)
        
        self.book_room_button = QPushButton('Pesan')
        self.book_room_button.setStyleSheet("font-size: 16px; padding: 10px;")
        self.room_booking_layout.addRow(self.book_room_button)
        
        self.back_button2 = QPushButton('Kembali ke Menu Utama')
        self.back_button2.setStyleSheet("font-size: 16px; padding: 10px;")
        self.back_button2.clicked.connect(self.show_main_menu)
        self.room_booking_layout.addRow(self.back_button2)
        
        self.stacked_widget.addWidget(self.room_booking)

        # Room Status
        self.room_status = QWidget()
        self.room_status_layout = QVBoxLayout()
        self.room_status.setLayout(self.room_status_layout)
        
        self.room_status_layout.addWidget(QLabel('<h2>Status Kamar</h2>'))
        
        self.status_table = QTableWidget()
        self.status_table.setRowCount(10)  # Assume 10 rooms for simplicity
        self.status_table.setColumnCount(2)
        self.status_table.setHorizontalHeaderLabels(['Kamar', 'Status'])
        for i in range(10):
            self.status_table.setItem(i, 0, QTableWidgetItem(f'Kamar {i+1}'))
            self.status_table.setItem(i, 1, QTableWidgetItem('Tersedia'))
        self.room_status_layout.addWidget(self.status_table)
        
        self.back_button3 = QPushButton('Kembali ke Menu Utama')
        self.back_button3.setStyleSheet("font-size: 16px; padding: 10px;")
        self.back_button3.clicked.connect(self.show_main_menu)
        self.room_status_layout.addWidget(self.back_button3)
        
        self.stacked_widget.addWidget(self.room_status)

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def show_register_guest(self):
        self.stacked_widget.setCurrentWidget(self.guest_registration)

    def show_room_booking(self):
        self.stacked_widget.setCurrentWidget(self.room_booking)

    def show_room_status(self):
        self.stacked_widget.setCurrentWidget(self.room_status)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
