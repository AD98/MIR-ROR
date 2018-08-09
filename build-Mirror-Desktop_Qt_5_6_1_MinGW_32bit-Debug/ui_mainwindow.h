/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionOptions;
    QWidget *centralWidget;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_2;
    QRadioButton *note1;
    QRadioButton *note2;
    QRadioButton *note3;
    QRadioButton *random_note;
    QLineEdit *custom_note;
    QPushButton *pushButton_3;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *track;
    QLabel *label;
    QPushButton *add_track_btn;
    QMenuBar *menuBar;
    QMenu *menuMirror;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(872, 311);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        actionOptions = new QAction(MainWindow);
        actionOptions->setObjectName(QStringLiteral("actionOptions"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy1);
        horizontalLayout = new QHBoxLayout(centralWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        note1 = new QRadioButton(centralWidget);
        note1->setObjectName(QStringLiteral("note1"));
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(note1->sizePolicy().hasHeightForWidth());
        note1->setSizePolicy(sizePolicy2);

        verticalLayout_2->addWidget(note1);

        note2 = new QRadioButton(centralWidget);
        note2->setObjectName(QStringLiteral("note2"));
        sizePolicy2.setHeightForWidth(note2->sizePolicy().hasHeightForWidth());
        note2->setSizePolicy(sizePolicy2);

        verticalLayout_2->addWidget(note2);

        note3 = new QRadioButton(centralWidget);
        note3->setObjectName(QStringLiteral("note3"));
        sizePolicy2.setHeightForWidth(note3->sizePolicy().hasHeightForWidth());
        note3->setSizePolicy(sizePolicy2);

        verticalLayout_2->addWidget(note3);

        random_note = new QRadioButton(centralWidget);
        random_note->setObjectName(QStringLiteral("random_note"));
        sizePolicy2.setHeightForWidth(random_note->sizePolicy().hasHeightForWidth());
        random_note->setSizePolicy(sizePolicy2);

        verticalLayout_2->addWidget(random_note);

        custom_note = new QLineEdit(centralWidget);
        custom_note->setObjectName(QStringLiteral("custom_note"));
        QSizePolicy sizePolicy3(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(custom_note->sizePolicy().hasHeightForWidth());
        custom_note->setSizePolicy(sizePolicy3);

        verticalLayout_2->addWidget(custom_note);

        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        QSizePolicy sizePolicy4(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(pushButton_3->sizePolicy().hasHeightForWidth());
        pushButton_3->setSizePolicy(sizePolicy4);

        verticalLayout_2->addWidget(pushButton_3);


        horizontalLayout->addLayout(verticalLayout_2);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setSizeConstraint(QLayout::SetMinimumSize);
        track = new QHBoxLayout();
        track->setSpacing(6);
        track->setObjectName(QStringLiteral("track"));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setMaximumSize(QSize(1280, 720));
        label->setPixmap(QPixmap(QString::fromUtf8("../img/TileClouds.png")));
        label->setScaledContents(false);

        track->addWidget(label);


        verticalLayout->addLayout(track);

        add_track_btn = new QPushButton(centralWidget);
        add_track_btn->setObjectName(QStringLiteral("add_track_btn"));
        sizePolicy4.setHeightForWidth(add_track_btn->sizePolicy().hasHeightForWidth());
        add_track_btn->setSizePolicy(sizePolicy4);

        verticalLayout->addWidget(add_track_btn);


        horizontalLayout->addLayout(verticalLayout);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 872, 21));
        menuBar->setDefaultUp(false);
        menuMirror = new QMenu(menuBar);
        menuMirror->setObjectName(QStringLiteral("menuMirror"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuMirror->menuAction());
        menuMirror->addAction(actionOptions);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        actionOptions->setText(QApplication::translate("MainWindow", "options", 0));
        note1->setText(QApplication::translate("MainWindow", "Possible Note 1", 0));
        note2->setText(QApplication::translate("MainWindow", "Possible Note 2", 0));
        note3->setText(QApplication::translate("MainWindow", "Possible Note 3", 0));
        random_note->setText(QApplication::translate("MainWindow", "Random Note", 0));
        custom_note->setInputMask(QString());
        custom_note->setText(QApplication::translate("MainWindow", "Custom", 0));
        pushButton_3->setText(QApplication::translate("MainWindow", "Add Note", 0));
        label->setText(QString());
        add_track_btn->setText(QApplication::translate("MainWindow", "Add Track", 0));
        menuMirror->setTitle(QApplication::translate("MainWindow", "Mirror", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
