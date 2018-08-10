#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QLabel>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_add_track_btn_clicked()
{
    add_track = new Add_track(this);
    add_track->show();
}

void MainWindow::on_pushButton_3_clicked()
{
    void *add = NULL;
    if (ui->note1->isChecked()){
        add = (char*)"1";
        ui->note1->setAutoExclusive(false);
        ui->note1->setChecked(false);
        ui->note1->setAutoExclusive(true);
    }
    else if (ui->note2->isChecked()){
        add = (char*)"2";
        ui->note2->setAutoExclusive(false);
        ui->note2->setChecked(false);
        ui->note2->setAutoExclusive(true);
    }
    else if (ui->note3->isChecked()){
        add = (char*)"3";
        ui->note3->setAutoExclusive(false);
        ui->note3->setChecked(false);
        ui->note3->setAutoExclusive(true);
    }
    else if (ui->random_note->isChecked()){
        add = (char*)"4";
        ui->random_note->setAutoExclusive(false);
        ui->random_note->setChecked(false);
        ui->random_note->setAutoExclusive(true);
    }
    if (add != NULL)
        ui->track->addWidget(new QLabel((char*)add));
    else
        ui->track->addWidget(new QLabel(ui->custom_note->text()));

}
