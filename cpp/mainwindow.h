#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "add_track.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:

    void on_add_track_btn_clicked();

    void on_pushButton_3_clicked();

private:
    Ui::MainWindow *ui;
    Add_track *add_track;
    QString *note;
};

#endif // MAINWINDOW_H
