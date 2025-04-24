#if 0

 A very simple Linux-version of the Software for the
 Voltcraft CO-20 AirSensor...

 uses:

  - libusb-0.1
    (or libusb-1.0 with libusb-compat)
  - QT
  - QWT

  JKN (2011)

#endif

#include <qapplication.h>
#include <qlayout.h>
#include <qlabel.h>
#include <qpainter.h>
#include <qwt_plot_layout.h>
#include <qwt_plot_curve.h>
#include <qwt_scale_draw.h>
#include <qwt_scale_widget.h>
#include <qwt_legend.h>
#include <qwt_legend_item.h>
#include <qwt_plot.h>
#include <qthread.h>
#include <QtCore/qdatetime.h>
#include <QtGui/QLinearGradient>
#include <assert.h>
#include <signal.h>
#include <cstdio>
#include <usb.h>

#define HISTORY 120 // seconds
// A wild guess where the transition green/yellow/red are...
// range: 450-2000 CO2-equiv. pppm
#define AQ_MIN  450
#define AQ_1ST  800
#define AQ_2ND  900
#define AQ_MAX 1100


class QwtPlotCurve;
class AirSensor;

class ASStat : public QThread
 {
     Q_OBJECT

 private:
   AirSensor* parent;
   struct usb_device *find_device(int vendor, int product);
 public:
   void setParent(AirSensor* p_in);
   void shutdown_usb();
   QTime upTime() const;
 protected:
     void run();
};


class AirSensor : public QwtPlot 
{
    Q_OBJECT
public:
    enum CpuData
    {
        User,
        System,
        Total,
        Idle,

        NCpuData
    };

    AirSensor(QWidget * = 0);
    const QwtPlotCurve *cpuCurve() const
        { return data.curve; }

    void newValue(unsigned short);
    bool newVal;
    bool write2file;
    unsigned short new_val;
    FILE* plotFile;
protected:
    void timerEvent(QTimerEvent *e);

private slots:
    void showCurve(QwtPlotItem *, bool on);
    void writeCurve(QwtPlotItem *, bool on);

private:
    struct
    {
        QwtPlotCurve *curve;
        double data[HISTORY];
    } data;
    double timeData[HISTORY];

    int dataCount;
    ASStat asStat;
};
