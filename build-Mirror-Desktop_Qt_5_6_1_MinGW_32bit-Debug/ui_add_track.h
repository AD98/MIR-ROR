/********************************************************************************
** Form generated from reading UI file 'add_track.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADD_TRACK_H
#define UI_ADD_TRACK_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Add_track
{
public:
    QDialogButtonBox *buttonBox;
    QWidget *layoutWidget;
    QFormLayout *formLayout;
    QLabel *label;
    QComboBox *comboBox;
    QComboBox *comboBox_2;
    QLabel *label_2;
    QLabel *label_3;
    QPushButton *pushButton;
    QLabel *label_4;
    QLabel *file_label;

    void setupUi(QDialog *Add_track)
    {
        if (Add_track->objectName().isEmpty())
            Add_track->setObjectName(QStringLiteral("Add_track"));
        Add_track->resize(400, 300);
        buttonBox = new QDialogButtonBox(Add_track);
        buttonBox->setObjectName(QStringLiteral("buttonBox"));
        buttonBox->setGeometry(QRect(30, 240, 341, 32));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        layoutWidget = new QWidget(Add_track);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(20, 80, 287, 101));
        formLayout = new QFormLayout(layoutWidget);
        formLayout->setObjectName(QStringLiteral("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(layoutWidget);
        label->setObjectName(QStringLiteral("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        comboBox = new QComboBox(layoutWidget);
        comboBox->setObjectName(QStringLiteral("comboBox"));

        formLayout->setWidget(1, QFormLayout::FieldRole, comboBox);

        comboBox_2 = new QComboBox(layoutWidget);
        comboBox_2->setObjectName(QStringLiteral("comboBox_2"));

        formLayout->setWidget(2, QFormLayout::FieldRole, comboBox_2);

        label_2 = new QLabel(layoutWidget);
        label_2->setObjectName(QStringLiteral("label_2"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        label_3 = new QLabel(layoutWidget);
        label_3->setObjectName(QStringLiteral("label_3"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_3);

        pushButton = new QPushButton(layoutWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        formLayout->setWidget(0, QFormLayout::FieldRole, pushButton);

        label_4 = new QLabel(Add_track);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(20, 30, 221, 31));
        file_label = new QLabel(Add_track);
        file_label->setObjectName(QStringLiteral("file_label"));
        file_label->setGeometry(QRect(160, 60, 201, 20));

        retranslateUi(Add_track);
        QObject::connect(buttonBox, SIGNAL(accepted()), Add_track, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Add_track, SLOT(reject()));

        QMetaObject::connectSlotsByName(Add_track);
    } // setupUi

    void retranslateUi(QDialog *Add_track)
    {
        Add_track->setWindowTitle(QApplication::translate("Add_track", "Dialog", 0));
        label->setText(QApplication::translate("Add_track", "Choose MIDI:", 0));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("Add_track", "<Select Model>", 0)
         << QApplication::translate("Add_track", "Lempel ziv", 0)
         << QApplication::translate("Add_track", "1st Order Markov Chain", 0)
         << QApplication::translate("Add_track", "2nd Order Markov Chain", 0)
        );
        comboBox_2->clear();
        comboBox_2->insertItems(0, QStringList()
         << QApplication::translate("Add_track", "<Select Instrument>", 0)
         << QApplication::translate("Add_track", "Guitar", 0)
         << QApplication::translate("Add_track", "Piano", 0)
        );
        label_2->setText(QApplication::translate("Add_track", "Model Type:", 0));
        label_3->setText(QApplication::translate("Add_track", "Instrument:", 0));
        pushButton->setText(QApplication::translate("Add_track", "Browse", 0));
        label_4->setText(QApplication::translate("Add_track", "Choose Options for New Track", 0));
        file_label->setText(QApplication::translate("Add_track", "No file selected", 0));
    } // retranslateUi

};

namespace Ui {
    class Add_track: public Ui_Add_track {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADD_TRACK_H
