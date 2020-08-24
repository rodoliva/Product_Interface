from PyQt5 import QtCore, QtGui, QtWidgets
import ConfigData as bd
from ConfigData import save_data as saver, openerli as opener, UndoRedoManager as urmger
from functools import partial
import copy

class Ui_productWin(object):

    def setupUi(self, productWin):

        productWin.resize(1361, 500)

        self.prodwin = productWin
        self.li = opener(bd.prod_dir) # product list
        self.manager = urmger(self.li.copy()) # undo and redo manager


        # ------------------------------Colors Palette----------------------------------------

        self.color_pallete(productWin)
        self.centralwidget = QtWidgets.QWidget(productWin)

        # ------------------------------Tool Box----------------------------------------
        self.ToolsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ToolsBox.setGeometry(QtCore.QRect(10, 10, 421, 421))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ToolsBox.setFont(font)
        self.toolBox = QtWidgets.QToolBox(self.ToolsBox)
        self.toolBox.setGeometry(QtCore.QRect(20, 30, 381, 381))

        # ------------------------------New Product Page----------------------------------------
        self.newprodpage = QtWidgets.QWidget()
        self.newprodpage.setGeometry(QtCore.QRect(0, 0, 98, 28))

        self.labelid = QtWidgets.QLabel(self.newprodpage)
        self.labelid.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelid.setFont(font)

        # New product input line id
        self.linidnpnp = QtWidgets.QLineEdit(self.newprodpage)
        self.linidnpnp.setGeometry(QtCore.QRect(170, 10, 113, 22))

        # New product Check ID
        self.checkIDnpButton = QtWidgets.QPushButton(self.newprodpage)
        self.checkIDnpButton.setGeometry(QtCore.QRect(300, 10, 71, 28))
        #self.checkIDnpButton.clicked.connect(partial(self.check_id_message_newprod, 'ID'))
        self.checkIDnpButton.clicked.connect(partial(self.check_id_message_newprod))

        self.labelnamenp = QtWidgets.QLabel(self.newprodpage)
        self.labelnamenp.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelnamenp.setFont(font)

        # New product input line Name
        self.linenamenp = QtWidgets.QLineEdit(self.newprodpage)
        self.linenamenp.setGeometry(QtCore.QRect(170, 50, 113, 22))

        self.labelshortnp = QtWidgets.QLabel(self.newprodpage)
        self.labelshortnp.setGeometry(QtCore.QRect(10, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelshortnp.setFont(font)

        # New product input line Short Name
        self.lineshortnp = QtWidgets.QLineEdit(self.newprodpage)
        self.lineshortnp.setGeometry(QtCore.QRect(170, 90, 113, 22))

        self.labelprodtynp = QtWidgets.QLabel(self.newprodpage)
        self.labelprodtynp.setGeometry(QtCore.QRect(10, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelprodtynp.setFont(font)

        # New product input line Product Type
        self.linetypenp = QtWidgets.QLineEdit(self.newprodpage)
        self.linetypenp.setGeometry(QtCore.QRect(170, 130, 113, 22))

        # New product Check Product Type
        self.checkproductnpButton = QtWidgets.QPushButton(self.newprodpage)
        self.checkproductnpButton.setGeometry(QtCore.QRect(300, 130, 71, 28))
        self.checkproductnpButton.clicked.connect(self.prod_type_message)

        self.labelrefprnp = QtWidgets.QLabel(self.newprodpage)
        self.labelrefprnp.setGeometry(QtCore.QRect(10, 170, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelrefprnp.setFont(font)

        # New product input line Reference Price
        self.linerefprnp = QtWidgets.QLineEdit(self.newprodpage)
        self.linerefprnp.setGeometry(QtCore.QRect(170, 170, 113, 22))

        # New product ok or cancel
        self.buttonBoxnp = QtWidgets.QDialogButtonBox(self.newprodpage)
        self.buttonBoxnp.setGeometry(QtCore.QRect(10, 220, 321, 32))
        self.buttonBoxnp.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxnp.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxnp.accepted.connect(self.new_product)
        self.buttonBoxnp.rejected.connect(self.new_prod_clear)


        # ------------------------------Update Page----------------------------------------
        self.toolBox.addItem(self.newprodpage, "")
        self.updatepage = QtWidgets.QWidget()
        self.updatepage.setGeometry(QtCore.QRect(0, 0, 381, 270))
        self.labelidup = QtWidgets.QLabel(self.updatepage)
        self.labelidup.setGeometry(QtCore.QRect(10, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)

        self.labelidup.setFont(font)

        # Update id line input
        self.lineidup = QtWidgets.QLineEdit(self.updatepage)
        self.lineidup.setGeometry(QtCore.QRect(170, 20, 113, 22))

        # Update id Check button
        self.checkidupButton = QtWidgets.QPushButton(self.updatepage)
        self.checkidupButton.setGeometry(QtCore.QRect(300, 20, 71, 28))
        self.checkidupButton.clicked.connect(self.check_id_message_update)

        self.labelchangeup = QtWidgets.QLabel(self.updatepage)
        self.labelchangeup.setGeometry(QtCore.QRect(10, 60, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelchangeup.setFont(font)

        # Combobox update ID, Name, Short Name, Product Type, Reference Price
        self.comboBoxup = QtWidgets.QComboBox(self.updatepage)
        self.comboBoxup.setGeometry(QtCore.QRect(170, 60, 161, 22))
        self.comboBoxup.addItem("")
        self.comboBoxup.addItem("")
        self.comboBoxup.addItem("")
        self.comboBoxup.addItem("")
        self.comboBoxup.addItem("")
        self.comboBoxup.addItem("")

        self.labelinup = QtWidgets.QLabel(self.updatepage)
        self.labelinup.setGeometry(QtCore.QRect(10, 100, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelinup.setFont(font)

        # Update input line input
        self.lineinpuup = QtWidgets.QLineEdit(self.updatepage)
        self.lineinpuup.setGeometry(QtCore.QRect(170, 100, 113, 22))

        # Update ok or cancel
        self.buttonBoxup = QtWidgets.QDialogButtonBox(self.updatepage)
        self.buttonBoxup.setGeometry(QtCore.QRect(10, 190, 321, 32))
        self.buttonBoxup.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxup.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxup.accepted.connect(self.update_product)
        self.buttonBoxup.rejected.connect(self.update_prod_clear)


        # ------------------------------Delete Page----------------------------------------
        self.toolBox.addItem(self.updatepage, "")  # create the delete page
        self.deletepage = QtWidgets.QWidget()
        self.deletepage.setGeometry(QtCore.QRect(0, 0, 98, 28))

        self.labeliddel = QtWidgets.QLabel(self.deletepage)
        self.labeliddel.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labeliddel.setFont(font)

        # Delete line input
        self.lineiddel = QtWidgets.QLineEdit(self.deletepage)
        self.lineiddel.setGeometry(QtCore.QRect(170, 20, 113, 22))

        # Delete ok or cancel
        self.buttonBoxdel = QtWidgets.QDialogButtonBox(self.deletepage)
        self.buttonBoxdel.setGeometry(QtCore.QRect(10, 160, 321, 32))
        self.buttonBoxdel.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxdel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxdel.accepted.connect(self.delete_product)
        self.buttonBoxdel.rejected.connect(self.delete_prod_clear)
        self.toolBox.addItem(self.deletepage, "")


        # ------------------------------Show Products Table----------------------------------------
        # Table that show products

        self.set_table()

        # Column an row set up
        self.tableWidget.setColumnCount(5)

        self.product_data_table()

        self.set_first_row()

        productWin.setCentralWidget(self.centralwidget)

        # Menu bar

        self.menubar = QtWidgets.QMenuBar(productWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1361, 26))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuTools = QtWidgets.QMenu(self.menubar)
        productWin.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(productWin)
        productWin.setStatusBar(self.statusbar)

        # Action in menu
        self.actionOpen_File = QtWidgets.QAction(productWin)
        self.actionOpen_File.setStatusTip('Add new products by file')
        self.actionOpen_File.triggered.connect(self.load_file)

        self.actionSave = QtWidgets.QAction(productWin)
        self.actionSave.setStatusTip('Save Changes')
        self.actionSave.triggered.connect(self.save_and_backup)

        self.actionExit = QtWidgets.QAction(productWin)
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(QtWidgets.QApplication.instance().quit)

        self.actionUndo = QtWidgets.QAction(productWin)
        self.actionUndo.setStatusTip('Undo last Change')
        self.actionUndo.triggered.connect(self.undo_products)

        self.actionRedo = QtWidgets.QAction(productWin)
        self.actionRedo.setStatusTip('Redo last Change')
        self.actionRedo.triggered.connect(self.redo_products)

        self.actionRefresh = QtWidgets.QAction(productWin)
        self.actionRefresh.setStatusTip('Refresh Table')
        self.actionRefresh.triggered.connect(self.refresh_table)

        self.actionSearch = QtWidgets.QAction(productWin)
        self.actionSearch.setStatusTip('Search product by ID')
        self.actionSearch.triggered.connect(self.searched)

        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionRefresh)
        self.menuTools.addAction(self.actionSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(productWin)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(productWin)

    def color_pallete(self, productWin):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 235, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 144, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 235, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 235, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 144, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 235, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 235, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 144, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 216, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        productWin.setPalette(palette)

    def set_table(self):
        self.TableBoxprod = QtWidgets.QGroupBox(self.centralwidget)
        self.TableBoxprod.setGeometry(QtCore.QRect(460, 10, 811, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableBoxprod.sizePolicy().hasHeightForWidth())
        self.TableBoxprod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TableBoxprod.setFont(font)
        self.tableWidget = QtWidgets.QTableWidget(self.TableBoxprod)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 771, 371))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def set_first_row(self):
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

    def retranslateUi(self, productWin):
        _translate = QtCore.QCoreApplication.translate
        productWin.setWindowTitle(_translate("productWin", "productWin"))
        self.ToolsBox.setTitle(_translate("productWin", "Tools"))
        self.labelid.setText(_translate("productWin", "ID"))
        self.checkIDnpButton.setText(_translate("productWin", "Check"))
        self.labelnamenp.setText(_translate("productWin", "Name"))
        self.labelshortnp.setText(_translate("productWin", "Short Name"))
        self.labelprodtynp.setText(_translate("productWin", "Product Type"))
        self.checkproductnpButton.setText(_translate("productWin", "Check"))
        self.labelrefprnp.setText(_translate("productWin", "Reference Price"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.newprodpage), _translate("productWin", "New Product"))
        self.labelidup.setText(_translate("productWin", "ID"))
        self.checkidupButton.setText(_translate("productWin", "Check"))
        self.labelchangeup.setText(_translate("productWin", "Item to change"))
        self.comboBoxup.setItemText(0, _translate("productWin", "----------------"))
        self.comboBoxup.setItemText(1, _translate("productWin", "ID"))
        self.comboBoxup.setItemText(2, _translate("productWin", "Name"))
        self.comboBoxup.setItemText(3, _translate("productWin", "Short Name"))
        self.comboBoxup.setItemText(4, _translate("productWin", "Product Type"))
        self.comboBoxup.setItemText(5, _translate("productWin", "Reference Price"))
        self.labelinup.setText(_translate("productWin", "Input"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.updatepage), _translate("productWin", "Update"))
        self.labeliddel.setText(_translate("productWin", "ID"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.deletepage), _translate("productWin", "Delete"))
        self.TableBoxprod.setTitle(_translate("productWin", "Products"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("productWin", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("productWin", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("productWin", "Short Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("productWin", "Product Type"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("productWin", "Reference Price"))
        self.menuFile.setTitle(_translate("productWin", "File"))
        self.menuEdit.setTitle(_translate("productWin", "Edit"))
        self.menuTools.setTitle(_translate("productWin", "Tools"))
        self.actionOpen_File.setText(_translate("productWin", "Open File"))
        self.actionSave.setText(_translate("productWin", "Save"))
        self.actionExit.setText(_translate("productWin", "Exit"))
        self.actionUndo.setText(_translate("productWin", "Undo"))
        self.actionRedo.setText(_translate("productWin", "Redo"))
        self.actionRefresh.setText(_translate("productWin", "Refresh"))
        self.actionSearch.setText(_translate("productWin", "Search"))

    def product_data_table(self):
        row_num = 0
        self.tableWidget.setRowCount(0)
        for prod in self.li:
            self.tableWidget.insertRow(row_num)
            self.tableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(prod.id)))
            self.tableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(prod.name)))
            self.tableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(prod.short_name)))
            self.tableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(prod.prod_type)))
            self.tableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(str(prod.reference_price)))
            row_num += 1
        if not len(self.li) == 0:
            self.tableWidget.resizeColumnsToContents()

    def save_and_backup(self):
        saver(bd.prod_dir, bd.prod_bck, self.li)

    def check_id_message_newprod(self):
        try:
            data = self.linidnpnp.text()
            response = bd.check_id(int(data), bd.min_prod_id, bd.max_prod_id)
            if response and bd.check_dup_id(int(data), self.li):
                QtWidgets.QMessageBox().about(self.prodwin, 'All good',f'Id checked')
            else:
                QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a new ID between {bd.min_prod_id} and {bd.max_prod_id}')
        except ValueError:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID between {bd.min_prod_id} and {bd.max_prod_id}')

    def new_product(self):
        try:
            try:
                dataid = self.linidnpnp.text()
                dataname = self.linenamenp.text()
                datashort = self.lineshortnp.text()
                datatype = self.linetypenp.text()
                dataref = self.linerefprnp.text()
                if bd.check_id(int(dataid), bd.min_prod_id, bd.max_prod_id) and bd.check_dup_id(int(dataid), self.li):
                    prod_new = bd.Product(int(dataid), dataname, datashort, datatype, dataref)
                    self.li.append(prod_new)
                    self.manager.do_new_action(self.clone_li())  # for undo and redo
                    QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and new product created')
                    self.refresh_table()
                else:
                    QtWidgets.QMessageBox().about(self.prodwin, 'Warning',f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
            except ValueError:
                QtWidgets.QMessageBox().about(self.prodwin, 'Warning',f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
        except TypeError:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', 'Empty Data')

    def new_prod_clear(self):
        self.linidnpnp.clear()
        self.linenamenp.clear()
        self.lineshortnp.clear()
        self.linetypenp.clear()
        self.linerefprnp.clear()

    def check_id_message_update(self):
        try:
            data = self.lineidup.text()
            if bd.check_id(int(data), bd.min_prod_id, bd.max_prod_id) and not bd.check_dup_id(int(data), self.li):
                QtWidgets.QMessageBox().about(self.prodwin, 'All good',f'Id checked')
            else:
                QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
        except ValueError:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')

    def prod_type_message(self):
        data = self.linetypenp.text()
        prodtypelist = bd.prod_type(self.li)
        aux = False
        for prod in prodtypelist:
            if data == prod:
                aux = True
        if aux == True:
            QtWidgets.QMessageBox().about(self.prodwin, str(data), f'Product type found')
        else:
            QtWidgets.QMessageBox().about(self.prodwin, 'Not Fount', 'You input is a new type')

    def update_product(self):
        try:
            try:
                dataid = self.lineidup.text()
                data = self.lineinpuup.text()
                text = str(self.comboBoxup.currentText())
                if bd.check_id(int(dataid), bd.min_prod_id, bd.max_prod_id) and not bd.check_dup_id(int(dataid), self.li):
                    prod = self.search(int(dataid))
                    if text == 'ID':
                        if bd.check_id(int(data), bd.min_prod_id, bd.max_prod_id) and bd.check_dup_id(int(data), self.li):
                            prod.id = int(data)
                            self.manager.do_new_action(self.clone_li())  # for undo and redo
                            QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and product updated')
                            self.refresh_table()
                        else:
                            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID between {bd.min_prod_id} and {bd.max_prod_id}')
                    elif text == 'Name' and bd.notemp(data):
                        prod.name = data
                        self.manager.do_new_action(self.clone_li())  # for undo and redo
                        QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and product updated')
                        self.refresh_table()
                    elif text == 'Short Name' and bd.notemp(data):
                        prod.short_name = data
                        self.manager.do_new_action(self.clone_li())  # for undo and redo
                        QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and product updated')
                        self.refresh_table()
                    elif text == 'Product Type' and bd.notemp(data):
                        prod.prod_type = data
                        self.manager.do_new_action(self.clone_li())  # for undo and redo
                        QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and product updated')
                        self.refresh_table()
                    elif text == 'Reference Price' and bd.notemp(data):
                        prod.reference_price = data
                        self.manager.do_new_action(self.clone_li())  # for undo and redo
                        QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Id checked and product updated')
                        self.refresh_table()
                    else:
                        pass
                else:
                    QtWidgets.QMessageBox().about(self.prodwin, 'Warning',f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
            except ValueError:
                QtWidgets.QMessageBox().about(self.prodwin, 'Warning',f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
        except TypeError:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', 'Empty Data')

    def update_prod_clear(self):
        self.lineidup.clear()
        self.lineinpuup.clear()
        self.comboBoxup.setCurrentIndex(0)

    def delete_product(self):
        try:
            data = self.lineiddel.text()
            response = bd.check_id(int(data), bd.min_prod_id, bd.max_prod_id)
            if response and not bd.check_dup_id(int(data), self.li):
                ob = self.search(int(data))
                self.li.remove(ob)
                self.manager.do_new_action(self.clone_li()) #for undo and redo
                QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'Product Deleted')
                self.refresh_table()
            else:
                QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')
        except ValueError:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')

    def delete_prod_clear(self):
        self.lineiddel.clear()

    def refresh_table(self):
        self.tableWidget.clearContents()
        self.product_data_table()

    def undo_products(self):
        self.li = self.manager.undo()
        self.refresh_table()

    def redo_products(self):
        self.li = self.manager.redo()
        self.refresh_table()

    def load_file(self):
        try:
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.prodwin, 'Open file', "", "Excel files (*.xls, *.xlsx);;Text files (*.txt, *.csv);;All Files (*.*)")
            if not file_name == '':
                data_list = bd.open_excel(file_name)
                count = 0
                for prod in data_list: # Check all IDs
                    if bd.check_id(prod[0], bd.min_prod_id, bd.max_prod_id):
                        count +=1
                if count == len(data_list):
                    for prod in data_list:
                        id, name, short_name, prod_type, reference_price = prod[0], prod[1], prod[2], prod[3], prod[4]
                        if bd.check_dup_id(id, self.li):
                            prod_new = bd.Product(id, name, short_name, prod_type, reference_price)
                            self.li.append(prod_new)
                            self.manager.do_new_action(self.clone_li())  # for undo and redo
                        else:
                            pr = self.search(id)
                            pr.name, pr.short_name, pr.prod_type, pr.reference_price = name, short_name, prod_type, reference_price
                            self.manager.do_new_action(self.clone_li())  # for undo and redo
                    QtWidgets.QMessageBox().about(self.prodwin, 'All good', f'File loaded')
                    self.refresh_table()
                else:
                    QtWidgets.QMessageBox().about(self.prodwin, 'Warning',f'Need a ID between {bd.min_prod_id} and {bd.max_prod_id}')
        except bd.o.utils.exceptions.InvalidFileException:
            QtWidgets.QMessageBox().about(self.prodwin, 'Warning', 'File format not suported')

    def search(self, id):
        for p in self.li:
            if p.id == id:
                return p

    def searched(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProductSearch()
        self.ui.setupUi(self.window, self.li)
        self.window.show()

    def clone_li(self):
        auxli = []
        if not self.li == []:
            copyli = copy.deepcopy(self.li)
            for prod in copyli:
                auxli.append(copy.deepcopy(prod))
            return auxli

class Ui_ProductSearch(object):

    def setupUi(self, ProductSearch, li):

        self.win = ProductSearch
        self.li = li
        ProductSearch.setObjectName("ProductSearch")
        ProductSearch.resize(420, 374)
        self.centralwidget = QtWidgets.QWidget(ProductSearch)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 55, 16))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 331, 192))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(140, 300, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.searched)
        self.buttonBox.rejected.connect(self.win.close)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 30, 113, 22))

        ProductSearch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProductSearch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))

        ProductSearch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProductSearch)

        ProductSearch.setStatusBar(self.statusbar)

        self.retranslateUi(ProductSearch)
        QtCore.QMetaObject.connectSlotsByName(ProductSearch)

    def retranslateUi(self, ProductSearch):
        _translate = QtCore.QCoreApplication.translate
        ProductSearch.setWindowTitle(_translate("ProductSearch", "Product Search"))
        self.label.setText(_translate("ProductSearch", "ID"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ProductSearch", "Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ProductSearch", "Short Name"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ProductSearch", "Product Type"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ProductSearch", "Reference Price"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProductSearch", "Product"))

    def search(self, id):
        if not self.li == []:
            for p in self.li:
                if p.id == id:
                    return p

    def searched(self):
        try:
            idsearch = int(self.lineEdit.text())
            prod = self.search(idsearch)
            if not self.li == [] and not prod == None:
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(prod.name)))
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem(str(prod.short_name)))
                self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem(str(prod.prod_type)))
                self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem(str(prod.reference_price)))
                self.tableWidget.resizeColumnsToContents()
            else:
                QtWidgets.QMessageBox().about(self.win, 'Warning', 'ID not found')
        except ValueError:
            QtWidgets.QMessageBox().about(self.win, 'Warning',f'Need a ID from table and between {bd.min_prod_id} and {bd.max_prod_id}')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_productWin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
