#include "add_track.h"
#include "ui_add_track.h"

Add_track::Add_track(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Add_track)
{
    ui->setupUi(this);
}

Add_track::~Add_track()
{
    delete ui;
}

void Add_track::on_pushButton_clicked()
{
    training_file = QFileDialog::getOpenFileName(this, tr("Open File"),
                                                 "/home",
                                                 tr("MIDI files (*.mid)"));
    ui->file_label->setText(training_file);
}
