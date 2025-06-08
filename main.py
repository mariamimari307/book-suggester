import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox, QListWidgetItem
)
from PyQt5.QtCore import Qt
from main_window_ui import Ui_MainWindow


class BookTokApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.recommendationLayout = self.ui.recommendationLayout

        self.ui.selectionList.hide()
        self.ui.addToListButton.hide()
        self.ui.viewListButton.show()
        self.ui.dateLabel.hide()
        self.ui.readingDateEdit.hide()
        self.ui.commentEdit.hide()

        self.books = [
            {
                "title": "ჰარი პოტერი და ფილოსოფიური ქვა",
                "author": "ჯოან როულინგი",
                "genres": ["ფენტეზი", "სათავგადასავლო"],
                "format": "print",
                "fiction": True,
                "description": "პატარა ჯადოქრის პირველი წელი ჰოგვორტსში.",
                "price": 20.99,
                "rating": 5
            },
            {
                "title": "ჰარი პოტერი და საიდუმლო ოთახი",
                "author": "ჯოან როულინგი",
                "genres": ["ფენტეზი", "სათავგადასავლო"],
                "format": "digital",
                "fiction": True,
                "description": "საშიში საიდუმლოებები ჰოგვორტსის კედლებში.",
                "price": 11.99,
                "rating": 4
            },
            {
                "title": "ბეჭდების მბრძანებელი: ბეჭდის საძმო",
                "author": "ჯონ რონალდ რუელ ტოლკინი",
                "genres": ["ფენტეზი", "სათავგადასავლო"],
                "format": "print",
                "fiction": True,
                "description": "ერთ ბეჭედს შეუძლია სამყაროს ბედი განსაზღვროს.",
                "price": 25.50,
                "rating": 5
            },
            {
                "title": "ბეჭდების მბრძანებელი: ორი ციხე-კოშკი",
                "author": "ჯონ რონალდ რუელ ტოლკინი",
                "genres": ["ფენტეზი"],
                "format": "print",
                "fiction": True,
                "description": "მეგობრები იბრძვიან ბნელ ძალებთან.",
                "price": 20.99,
                "rating": 5
            },
            {
                "title": "ბეჭდების მბრძანებელი: მეფის დაბრუნება",
                "author": "ჯონ რონალდ რუელ ტოლკინი",
                "genres": ["ფენტეზი", "სათავგადასავლო"],
                "format": "print",
                "fiction": True,
                "description": "მეფე არაგორნი მეფობის მესამე წელს მიდის.",
                "price": 29.99,
                "rating": 5
            },
            {
                "title": "შიმშილის თამაშები",
                "author": "სუზან კოლინზი",
                "genres": ["დისტოპია", "სათავგადასავლო"],
                "format": "print",
                "fiction": True,
                "description": "პანემის სასტიკ თამაშებში გადარჩენის ისტორია.",
                "price": 17.00,
                "rating": 5
            },
            {
                "title": "1984",
                "author": "ჯორჯ ორველი",
                "genres": ["დისტოპია", "ფილოსოფიური"],
                "format": "print",
                "fiction": True,
                "description": "ტოტალიტარული საზოგადოების შოკისმომგვრელი ხილვა.",
                "price": 14.90,
                "rating": 5
            },
            {
                "title": "დიუნი",
                "author": "ალექსანდრე დიუმა",
                "genres": ["საი-ფაი", "ფენტეზი"],
                "format": "print",
                "fiction": True,
                "description": "მელანჟის ბრძოლა უდაბნოს პლანეტა არაკისზე.",
                "price": 23.45,
                "rating": 5
            },
            {
                "title": "შერლოკ ჰოლმსის თავგადასავლები",
                "author": "ართურ კონან დოილი",
                "genres": ["დეტექტივი"],
                "format": "print",
                "fiction": True,
                "description": "მხოლოდ ლოგიკით გამოწვეული გახსნილი საქმეები.",
                "price": 16.00,
                "rating": 4
            },
            {
                "title": "დიდი გეტსბი",
                "author": "ფრენსის სკოტ ფიცჯერალდი",
                "genres": ["კლასიკა", "რომანტიკა"],
                "format": "print",
                "fiction": True,
                "description": "ამერიკული ოცნების ბნელი მხარე.",
                "price": 10.99,
                "rating": 5
            },
            {
                "title": "ფრანკენშტეინი",
                "author": "მერი შელი",
                "genres": ["კლასიკა", "საშიში"],
                "format": "digital",
                "fiction": True,
                "description": "ადამიანის მიერ შექმნილი მონსტრის ისტორია.",
                "price": 5.99,
                "rating": 4
            },
            {
                "title": "მარტოობის ასი წელი", 
                "author": "გაბრიელ გარსია მარკესი",
                "genres": ["მაგიური რეალიზმი", "კლასიკა"], 
                "format": "print", 
                "fiction": True, 
                "description": "ბუენდიების საგა მაკონდოში.", 
                "price": 16.00, "rating": 5
            },
            {
                "title": "მე, ბებია, ილიკო და ილარიონი", 
                "author": "ნოდარ დუმბაძე",
                "genres": ["კლასიკა", "დრამა"], 
                "format": "print", 
                "fiction": True, 
                "description": "მხიარული და სევდიანი ამბები სოფელში.", 
                "price": 5.99, "rating": 5
            },
            {
                "title": "ჯინსების თაობა", 
                "author": "დათო ტურაშვილი",
                "genres": ["დრამა", "ნონ-ფიქშენ"], 
                "format": "print", 
                "fiction": False, 
                "description": "საბჭოთა ახალგაზრდობის მღელვარე რეალობა.", 
                "price": 9.99, 
                "rating": 5
            },
            {
                "title": "ვამპირის დღიურები",
                "author": "ლიზა ჯეინ სმითი",
                "genres": ["ფენტენზი"],
                "format": "digital",
                "fiction": True,
                "description": "ვამპირების ისტორია",
                "price": 7.99,
                "rating": 4
            },
            {
                "title": "მეფე ლომი",
                "author": "ანდრე ნორტ",
                "genres": ["ფენტეზი"],
                "format": "print",
                "fiction": True,
                "description": "მეფე ლომის ისტორია",
                "price": 9.99,
                "rating": 4
            }
        ]

        self.readingList = []

        self.ui.recommendButton.clicked.connect(self.showRecommendations)
        self.ui.addToListButton.clicked.connect(self.addToReadingList)
        self.ui.viewListButton.clicked.connect(self.viewReadingList)
        self.ui.restartButton.clicked.connect(self.restartApp)
        self.ui.selectionList.itemClicked.connect(self.displayBookDetails)

        self.filtered_books = []

        self.populateGenreComboBoxes()

    def populateGenreComboBoxes(self):
        genres = set()
        for book in self.books:
            genres.update(book['ჟანრი'])
        genre_list = sorted(genres)

        self.ui.genreComboBox1.clear()
        self.ui.genreComboBox2.clear()
        self.ui.genreComboBox1.addItem('')
        self.ui.genreComboBox2.addItem('')
        self.ui.genreComboBox1.addItems(genre_list)
        self.ui.genreComboBox2.addItems(genre_list)

    def showRecommendations(self):
        while self.recommendationLayout.count():
            item = self.recommendationLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        genre1 = self.ui.genreComboBox1.currentText()
        genre2 = self.ui.genreComboBox2.currentText()
        selected_format = 'ბეჭდური' if self.ui.printRadioButton.isChecked() else 'ციფრული'
        fiction_only = self.ui.fictionCheckBox.isChecked()

        filtered_books = []

        for book in self.books:
            if genre1 and genre1 not in book['ჟანრი']:
                continue
            if genre2 and genre2 not in book['ჟანრი']:
                continue
            if book['ფორმატი'] != selected_format:
                continue
            if fiction_only and not book['მხატვრული']:
                continue
            filtered_books.append(book)

        self.filtered_books = filtered_books

        if not filtered_books:
            no_result_label = QLabel('შენთვის რეკომენდირებული წიგნი ვერ მოიძებნა.')
            self.recommendationLayout.addWidget(no_result_label)
            self.ui.selectionList.hide()
            self.ui.addToListButton.hide()
            self.ui.viewListButton.hide()
            self.ui.dateLabel.hide()
            self.ui.readingDateEdit.hide()
            self.ui.commentEdit.hide()
            return

        self.ui.selectionList.clear()
        for book in filtered_books:
            self.ui.selectionList.addItem(book['სათაური'])

        self.ui.selectionList.show()
        self.ui.addToListButton.show()
        self.ui.viewListButton.show()
        self.ui.dateLabel.show()
        self.ui.readingDateEdit.show()
        self.ui.commentEdit.show()

        if len(filtered_books) == 1:
            self.displayBookDetails(self.ui.selectionList.item(0))
        else:
            while self.recommendationLayout.count():
                item = self.recommendationLayout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

    def displayBookDetails(self, item):
        title = item.text()
        for book in self.filtered_books:
            if book['სათაური'] == title:
                while self.recommendationLayout.count():
                    old_item = self.recommendationLayout.takeAt(0)
                    widget = old_item.widget()
                    if widget:
                        widget.deleteLater()

                details = (
                    f'<b>{book['სათაური']}</b><br>'
                    f'ჟანრი: {', '.join(book['ჟანრი'])}<br>'
                    f'ფორმატი: {book['ფორმატი']}<br>'
                    f'მხატვრული: {'კი' if book['მხატვრული'] else 'არა'}<br>'
                    f'აღწერა: {book['აღწერა']}<br>'
                    f'ფასი: ${book['ღირებულება']:.2f}<br>'
                    f'შეფასება: {'★' * book['შეფასება']} {'☆' * (5 - book['შეფასება'])}'
                )
                label = QLabel(details)
                label.setWordWrap(True)
                self.recommendationLayout.addWidget(label)
                break

    def addToReadingList(self):
        selected_items = self.ui.selectionList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'შეცდომა', 'გთხოვთ აირჩიოთ წიგნი სიაში დამატებისთვის.')
            return

        for item in selected_items:
            title = item.text()
            if title in self.readingList:
                QMessageBox.information(self, 'ინფორმაცია', f'წიგნი "{title}" უკვე დამატებულია სიაში.')
            else:
                self.readingList.append(title)
                QMessageBox.information(self, 'წარმატება', f'წიგნი "{title}" დამატებულია სიაში.')

    def viewReadingList(self):
        if not self.readingList:
            QMessageBox.information(self, 'სია ცარიელია', 'წასაკითხი წიგნების სია ცარიელია.')
            return
        msg = 'თქვენი წასაკითხი წიგნების სია:\n' + '\n'.join(self.readingList)
        QMessageBox.information(self, 'წასაკითხ წიგნთა სია', msg)

    def restartApp(self):
        self.ui.genreComboBox1.setCurrentIndex(0)
        self.ui.genreComboBox2.setCurrentIndex(0)
        self.ui.printRadioButton.setAutoExclusive(False)
        self.ui.digitalRadioButton.setAutoExclusive(False)
        self.ui.printRadioButton.setChecked(False)
        self.ui.digitalRadioButton.setChecked(False)
        self.ui.printRadioButton.setAutoExclusive(True)
        self.ui.digitalRadioButton.setAutoExclusive(True)
        self.ui.fictionCheckBox.setChecked(False)
        self.ui.selectionList.clear()
        self.ui.readingDateEdit.clear()
        self.ui.commentEdit.clear()
        while self.recommendationLayout.count():
            item = self.recommendationLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ui.selectionList.hide()
        self.ui.addToListButton.hide()
        self.ui.viewListButton.show()
        self.ui.dateLabel.hide()
        self.ui.readingDateEdit.hide()
        self.ui.commentEdit.hide()


app = QApplication(sys.argv)
window = BookTokApp()
window.show()
sys.exit(app.exec_())
