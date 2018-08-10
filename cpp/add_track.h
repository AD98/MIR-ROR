#ifndef ADD_TRACK_H
#define ADD_TRACK_H

#include <QDialog>
#include <QInputDialog>
#include <QFileDialog>

namespace Ui {
class Add_track;
}

class Add_track : public QDialog
{
    Q_OBJECT

public:
    explicit Add_track(QWidget *parent = 0);
    ~Add_track();

private slots:
    void on_pushButton_clicked();


private:
    Ui::Add_track *ui;
    QString training_file;
};

#endif // ADD_TRACK_H
