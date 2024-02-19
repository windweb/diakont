# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExampleForm(object):
    def setupUi(self, ExampleForm):
        ExampleForm.setObjectName("ExampleForm")
        ExampleForm.resize(978, 286)
        self.gridLayout_2 = QtWidgets.QGridLayout(ExampleForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(ExampleForm)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.from_file_button = QtWidgets.QPushButton(self.groupBox_4)
        self.from_file_button.setObjectName("from_file_button")
        self.gridLayout_7.addWidget(self.from_file_button, 0, 0, 1, 1)
        self.to_file_button = QtWidgets.QPushButton(self.groupBox_4)
        self.to_file_button.setObjectName("to_file_button")
        self.gridLayout_7.addWidget(self.to_file_button, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ExampleForm)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.threshold_value = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_value.sizePolicy().hasHeightForWidth())
        self.threshold_value.setSizePolicy(sizePolicy)
        self.threshold_value.setStyleSheet("")
        self.threshold_value.setReadOnly(False)
        self.threshold_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.threshold_value.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.threshold_value.setKeyboardTracking(False)
        self.threshold_value.setDecimals(4)
        self.threshold_value.setMinimum(-100000.0)
        self.threshold_value.setMaximum(100000.0)
        self.threshold_value.setObjectName("threshold_value")
        self.gridLayout_9.addWidget(self.threshold_value, 3, 1, 1, 1)
        self.measurement_label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.measurement_label_14.setWordWrap(True)
        self.measurement_label_14.setObjectName("measurement_label_14")
        self.gridLayout_9.addWidget(self.measurement_label_14, 2, 0, 1, 1)
        self.threshold_label = QtWidgets.QLabel(self.groupBox_2)
        self.threshold_label.setWordWrap(True)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout_9.addWidget(self.threshold_label, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 4, 0, 1, 1)
        self.trigger_condition = QtWidgets.QComboBox(self.groupBox_2)
        self.trigger_condition.setObjectName("trigger_condition")
        self.trigger_condition.addItem("")
        self.trigger_condition.addItem("")
        self.trigger_condition.addItem("")
        self.trigger_condition.addItem("")
        self.gridLayout_9.addWidget(self.trigger_condition, 5, 1, 1, 1)
        self.trigger_label = QtWidgets.QLabel(self.groupBox_2)
        self.trigger_label.setWordWrap(True)
        self.trigger_label.setObjectName("trigger_label")
        self.gridLayout_9.addWidget(self.trigger_label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 5, 0, 1, 1)
        self.times = QtWidgets.QSpinBox(self.groupBox_2)
        self.times.setObjectName("times")
        self.gridLayout_9.addWidget(self.times, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 2, 2, 1, 1)
        self.posttrigger_period_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.posttrigger_period_spinbox.setMaximum(10000.0)
        self.posttrigger_period_spinbox.setObjectName("posttrigger_period_spinbox")
        self.gridLayout_9.addWidget(self.posttrigger_period_spinbox, 2, 1, 1, 1)
        self.pretrigger_period_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.pretrigger_period_spinbox.setMaximum(10000.0)
        self.pretrigger_period_spinbox.setObjectName("pretrigger_period_spinbox")
        self.gridLayout_9.addWidget(self.pretrigger_period_spinbox, 1, 1, 1, 1)
        self.start_trigger_name = QtWidgets.QComboBox(self.groupBox_2)
        self.start_trigger_name.setObjectName("start_trigger_name")
        self.gridLayout_9.addWidget(self.start_trigger_name, 0, 1, 1, 1)
        self.measurement_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.measurement_label_2.setWordWrap(True)
        self.measurement_label_2.setObjectName("measurement_label_2")
        self.gridLayout_9.addWidget(self.measurement_label_2, 1, 0, 1, 1)
        self.measurement_label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurement_label_5.sizePolicy().hasHeightForWidth())
        self.measurement_label_5.setSizePolicy(sizePolicy)
        self.measurement_label_5.setWordWrap(True)
        self.measurement_label_5.setObjectName("measurement_label_5")
        self.gridLayout_9.addWidget(self.measurement_label_5, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 6, 0, 1, 1)
        self.trigger_mode = QtWidgets.QComboBox(self.groupBox_2)
        self.trigger_mode.setObjectName("trigger_mode")
        self.trigger_mode.addItem("")
        self.trigger_mode.addItem("")
        self.trigger_mode.addItem("")
        self.trigger_mode.addItem("")
        self.gridLayout_9.addWidget(self.trigger_mode, 6, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 2, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(ExampleForm)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signals_view = QtWidgets.QTreeView(self.groupBox_5)
        self.signals_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.signals_view.setObjectName("signals_view")
        self.verticalLayout.addWidget(self.signals_view)
        self.add_signal_button = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_signal_button.sizePolicy().hasHeightForWidth())
        self.add_signal_button.setSizePolicy(sizePolicy)
        self.add_signal_button.setObjectName("add_signal_button")
        self.verticalLayout.addWidget(self.add_signal_button)
        self.gridLayout_2.addWidget(self.groupBox_5, 1, 1, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(ExampleForm)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.set_trigger_get_data_button = QtWidgets.QPushButton(self.groupBox)
        self.set_trigger_get_data_button.setObjectName("set_trigger_get_data_button")
        self.gridLayout_5.addWidget(self.set_trigger_get_data_button, 1, 1, 1, 1)
        self.set_trigger_button = QtWidgets.QPushButton(self.groupBox)
        self.set_trigger_button.setObjectName("set_trigger_button")
        self.gridLayout_5.addWidget(self.set_trigger_button, 0, 1, 1, 1)
        self.reset_trigger_button = QtWidgets.QPushButton(self.groupBox)
        self.reset_trigger_button.setObjectName("reset_trigger_button")
        self.gridLayout_5.addWidget(self.reset_trigger_button, 2, 1, 1, 1)
        self.get_data_button = QtWidgets.QPushButton(self.groupBox)
        self.get_data_button.setObjectName("get_data_button")
        self.gridLayout_5.addWidget(self.get_data_button, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 2, 1, 1)

        self.retranslateUi(ExampleForm)
        QtCore.QMetaObject.connectSlotsByName(ExampleForm)

    def retranslateUi(self, ExampleForm):
        _translate = QtCore.QCoreApplication.translate
        ExampleForm.setWindowTitle(_translate("ExampleForm", "Example Widget"))
        self.groupBox_4.setTitle(_translate("ExampleForm", "Change state"))
        self.from_file_button.setText(_translate("ExampleForm", "Load from file"))
        self.to_file_button.setText(_translate("ExampleForm", "Save to file"))
        self.groupBox_2.setTitle(_translate("ExampleForm", "Trigger parameters"))
        self.measurement_label_14.setText(_translate("ExampleForm", "Posttrigger time"))
        self.threshold_label.setText(_translate("ExampleForm", "Threshold"))
        self.label_3.setText(_translate("ExampleForm", "Times"))
        self.trigger_condition.setItemText(0, _translate("ExampleForm", "< (less)"))
        self.trigger_condition.setItemText(1, _translate("ExampleForm", "> (great)"))
        self.trigger_condition.setItemText(2, _translate("ExampleForm", "== (equal)"))
        self.trigger_condition.setItemText(3, _translate("ExampleForm", "<> (non equal)"))
        self.trigger_label.setText(_translate("ExampleForm", "StartTrigger"))
        self.label.setText(_translate("ExampleForm", "Condition"))
        self.label_5.setText(_translate("ExampleForm", "s"))
        self.start_trigger_name.setPlaceholderText(_translate("ExampleForm", "Set signal name"))
        self.measurement_label_2.setText(_translate("ExampleForm", "Pretrigger time"))
        self.measurement_label_5.setText(_translate("ExampleForm", "s"))
        self.label_2.setText(_translate("ExampleForm", "Mode"))
        self.trigger_mode.setItemText(0, _translate("ExampleForm", "Force"))
        self.trigger_mode.setItemText(1, _translate("ExampleForm", "Once"))
        self.trigger_mode.setItemText(2, _translate("ExampleForm", "Cyclic"))
        self.trigger_mode.setItemText(3, _translate("ExampleForm", "Repeat"))
        self.groupBox_5.setTitle(_translate("ExampleForm", "Signals"))
        self.add_signal_button.setText(_translate("ExampleForm", "Add signals"))
        self.groupBox.setTitle(_translate("ExampleForm", "Trigger actions"))
        self.set_trigger_get_data_button.setText(_translate("ExampleForm", "Set trigger and get data"))
        self.set_trigger_button.setText(_translate("ExampleForm", "Set trigger"))
        self.reset_trigger_button.setText(_translate("ExampleForm", "Reset trigger"))
        self.get_data_button.setText(_translate("ExampleForm", "Get data"))
