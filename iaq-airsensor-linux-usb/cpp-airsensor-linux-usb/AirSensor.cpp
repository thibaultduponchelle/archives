#include "AirSensor.h"

struct usb_dev_handle *devh;

void ASStat::setParent(AirSensor* p_in){
   parent = p_in;
}

void release_usb_device(int dummy) {
    int ret;
    ret = usb_release_interface(devh, 0);
    usb_close(devh);
    exit(1);
}

struct usb_device* ASStat::find_device(int vendor, int product) {
    struct usb_bus *bus;

    for (bus = usb_get_busses(); bus; bus = bus->next) {
        struct usb_device *dev;

        for (dev = bus->devices; dev; dev = dev->next) {
            if (dev->descriptor.idVendor == vendor
                && dev->descriptor.idProduct == product)
                return dev;
        }
    }
    return NULL;
}

void ASStat::run(){
  int ret, vendor, product;
  struct usb_device *dev;
  char buf[1000];

  usb_init();
  usb_set_debug(255);
  usb_find_busses();
  usb_find_devices();

  vendor  = 0x03eb;
  product = 0x2013;
  dev = find_device(vendor, product);
  if (dev == NULL){
    printf("\nCouldn't find device 03eb:2013!\n\n");
    exit(1);
  }
  assert(dev);

  devh = usb_open(dev);
  assert(devh);
  
  signal(SIGTERM, release_usb_device);

  ret = usb_get_driver_np(devh, 0, buf, sizeof(buf));
  if (ret == 0) {
      printf("interface 0 already claimed by driver \"%s\", attempting to detach it\n", buf);
      ret = usb_detach_kernel_driver_np(devh, 0);
      printf("usb_detach_kernel_driver_np returned %d\n", ret);
  }
  ret = usb_claim_interface(devh, 0);
  if (ret != 0) {
      printf("claim failed with error %d\n", ret);
        exit(1);
  }
 
  ret = usb_set_altinterface(devh, 0);
  assert(ret >= 0);

  ret = usb_get_descriptor(devh, 0x0000001, 0x0000000, buf, 0x0000012);
  usleep(3*1000);
  ret = usb_get_descriptor(devh, 0x0000002, 0x0000000, buf, 0x0000009);
  usleep(2*1000);
  ret = usb_get_descriptor(devh, 0x0000002, 0x0000000, buf, 0x0000029);
  usleep(2*1000);
  ret = usb_release_interface(devh, 0);
  ret = usb_set_configuration(devh, 0x0000001);
  ret = usb_claim_interface(devh, 0);
  ret = usb_set_altinterface(devh, 0);
  usleep(34*1000);
  ret = usb_control_msg(devh, USB_TYPE_CLASS + USB_RECIP_INTERFACE, 0x000000a, 0x0000000, 0x0000000, buf, 0x0000000, 1000);
  usleep(11*1000);
  ret = usb_get_descriptor(devh, 0x0000022, 0x0000000, buf, 0x0000075);
  usleep(4*1000);
  ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
  ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);

  int c0 = 104;
  int c1 = 37;
  unsigned short iresult;
  while(0==0){
    usleep(2500*1000);
    memcpy(buf, "\x40\x68\x2a\x54\x52\x0a\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40", 0x0000010);
    buf[1] = (char) c0;
    c0++;
    if (c0 == 256) c0 = 103;
    ret = usb_interrupt_write(devh, 0x00000002, buf, 0x0000010, 1000);
    usleep(94*1000);
    ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
    // Seems to yield a realistic value...
    memcpy(&iresult,buf+2,2);
    //iresult /= 2;
    parent->newValue(iresult);
    usleep(14*1000);
    ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
    
    usleep(3*1000);
    memcpy(buf, "\x40\x30\x30\x30\x37\x46\x4c\x41\x47\x47\x45\x54\x3f\x0a\x40\x40", 0x0000010);
    buf[4] = (char) c1;
    c1++;
    if (c1 == 40) c1++;
    else if (c1 == 47) c1=30;
    ret = usb_interrupt_write(devh, 0x00000002, buf, 0x0000010, 1000);
    
    usleep(23*1000);
    ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
    usleep(14*1000);
    ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
    usleep(8*1000);
    ret = usb_interrupt_read(devh, 0x00000081, buf, 0x0000010, 1000);
  }
}

 void ASStat::shutdown_usb()
 {
  int ret = usb_release_interface(devh, 0);
  assert(ret == 0);
  ret = usb_close(devh);
  assert(ret == 0);
 }

QTime ASStat::upTime() const
{
    QTime t(0,0);
    return t;
}

class TimeScaleDraw: public QwtScaleDraw
{
public:
    TimeScaleDraw(const QTime &base):
        baseTime(base)
    {
    }
    virtual QwtText label(double v) const
    {
        QTime upTime = baseTime.addSecs((int)v);
        return upTime.toString();
    }
private:
    QTime baseTime;
};

class Background: public QwtPlotItem
{
public:
    Background()
    {
        setZ(0.0);
    }

    virtual int rtti() const
    {
        return QwtPlotItem::Rtti_PlotUserItem;
    }

    virtual void draw(QPainter *painter,
        const QwtScaleMap &, const QwtScaleMap &yMap,
        const QRect &rect) const
    {
        QColor c(Qt::red);
        QRect r = rect;

// set this to 0 if you want some gradient-color...
#if 0
        r.setBottom(yMap.transform(0));
        r.setTop(yMap.transform(AQ_1ST));
        painter->fillRect(r, Qt::green);

        r.setBottom(yMap.transform(AQ_1ST));
        r.setTop(yMap.transform(AQ_2ND));
        painter->fillRect(r, Qt::yellow);

        r.setBottom(yMap.transform(AQ_2ND));
        r.setTop(yMap.transform(AQ_MAX));
        painter->fillRect(r, c);
#else
        r.setBottom(yMap.transform(0));
        r.setTop(yMap.transform(AQ_1ST/2));
        painter->fillRect(r, Qt::green);

        r.setBottom(yMap.transform(AQ_1ST/2));
        r.setTop(yMap.transform(AQ_1ST + (AQ_2ND-AQ_1ST)/2));
        QPoint bot = r.bottomLeft();
        QPoint top = r.topRight();
        int cen = (top.x() + bot.x())/2;
        bot.setX(cen);
        top.setX(cen);
        QLinearGradient gradient(bot, top); 
        gradient.setColorAt(0, Qt::green);
        gradient.setColorAt(1, Qt::yellow);
        painter->fillRect(r, gradient);

        r.setBottom(yMap.transform(AQ_1ST + (AQ_2ND-AQ_1ST)/2));
        r.setTop(yMap.transform(AQ_2ND + (AQ_MAX-AQ_2ND)/2));
        QPoint bot2 = r.bottomLeft();
        QPoint top2 = r.topRight();
        int cen2 = (top2.x() + bot2.x())/2;
        bot2.setX(cen2);
        top2.setX(cen2);
        QLinearGradient gradient2(bot2, top2); 
        gradient2.setColorAt(0, Qt::yellow);
        gradient2.setColorAt(1, Qt::red);
        painter->fillRect(r, gradient2);


        r.setBottom(yMap.transform(AQ_2ND + (AQ_MAX-AQ_2ND)/2));
        r.setTop(yMap.transform(AQ_MAX));
        painter->fillRect(r, c);
#endif
    }
};

class CpuCurve: public QwtPlotCurve
{
public:
    CpuCurve(const QString &title):
        QwtPlotCurve(title)
    {
#if QT_VERSION >= 0x040000
        setRenderHint(QwtPlotItem::RenderAntialiased);
#endif
    }

    void setColor(const QColor &color)
    {
#if QT_VERSION >= 0x040000
        QColor c = color;
        c.setAlpha(150);

        setPen(c);
        setBrush(c);
#else
        setPen(color);
        setBrush(QBrush(color, Qt::Dense4Pattern));
#endif
    }
};

AirSensor::AirSensor(QWidget *parent):
    QwtPlot(parent),
    dataCount(0)
{
    setAutoReplot(false);

    newVal = false;

    write2file = false;
    plotFile = NULL;

    plotLayout()->setAlignCanvasToScales(true);

    QwtLegend *legend = new QwtLegend;
    legend->setItemMode(QwtLegend::CheckableItem);
    insertLegend(legend, QwtPlot::RightLegend);

//    setAxisTitle(QwtPlot::xBottom, " Time [h:m:s]");
    setAxisScaleDraw(QwtPlot::xBottom, new TimeScaleDraw(asStat.upTime()));
    setAxisScale(QwtPlot::xBottom, 0, HISTORY);
    setAxisLabelRotation(QwtPlot::xBottom, -50.0);
    setAxisLabelAlignment(QwtPlot::xBottom, Qt::AlignLeft | Qt::AlignBottom);

    /*
     In situations, when there is a label at the most right position of the
     scale, additional space is needed to display the overlapping part
     of the label would be taken by reducing the width of scale and canvas.
     To avoid this "jumping canvas" effect, we add a permanent margin.
     We don't need to do the same for the left border, because there
     is enough space for the overlapping label below the left scale.
     */

    QwtScaleWidget *scaleWidget = axisWidget(QwtPlot::xBottom);
    const int fmh = QFontMetrics(scaleWidget->font()).height();
    scaleWidget->setMinBorderDist(0, fmh / 2);

    // I looked it up: CO2-equiv. in ppm, range: 450 ppm - 2000 ppm
    setAxisTitle(QwtPlot::yLeft, "Air-Quality [ppm]");
    setAxisScale(QwtPlot::yLeft, AQ_MIN, AQ_MAX);

    Background *bg = new Background();
    bg->attach(this);

    CpuCurve *curve;

    curve = new CpuCurve("Air-Quality");
    curve->setColor(Qt::blue);
    curve->attach(this);
    data.curve = curve;

    showCurve(data.curve, true);

    for ( int i = 0; i < HISTORY; i++ )
        timeData[HISTORY - 1 - i] = i;

    (void)startTimer(1000); // 1 second

    connect(this, SIGNAL(legendChecked(QwtPlotItem *, bool)),
        SLOT(writeCurve(QwtPlotItem *, bool)));
//        SLOT(showCurve(QwtPlotItem *, bool)));


    asStat.setParent(this);
    asStat.start();
}

void AirSensor::newValue(unsigned short val)
{
    new_val = val;
    newVal = true;
}

void AirSensor::timerEvent(QTimerEvent *)
{

    if (!newVal) return;
    newVal = false;

    for ( int i = dataCount; i > 0; i-- )
    {
          if ( i < HISTORY )
             data.data[i] = data.data[i-1];
    }

    data.data[0] = new_val;
//    asStat.statistic(data.data[0]);

    if ( dataCount < HISTORY )
        dataCount++;

    for ( int j = 0; j < HISTORY; j++ )
        timeData[j]++;

    setAxisScale(QwtPlot::xBottom, 
        timeData[HISTORY - 1], timeData[0]);

      data.curve->setRawData(
          timeData, data.data, dataCount);

    if (write2file){
      fprintf(plotFile,"%12.2f %8.2f\n",timeData[0],(float)new_val);
      fflush(plotFile);
    }
    replot();
}

void AirSensor::writeCurve(QwtPlotItem *item, bool on)
{
  if (write2file){
    fclose(plotFile);
    printf("Close log-file 'airsensor.log'!\n");
  }else{
    plotFile = fopen("./airsensor.log","w");
    if (plotFile == NULL){
       printf("Could not open log-file!\n");
       write2file = true;
    }else{
       printf("Open log-file 'airsensor.log'!\n");
    }
  }
  write2file = !write2file;
}

void AirSensor::showCurve(QwtPlotItem *item, bool on)
{
    item->setVisible(on);
    QWidget *w = legend()->find(item);
    if ( w && w->inherits("QwtLegendItem") )
        ((QwtLegendItem *)w)->setChecked(on);
    
    replot();
}

int main(int argc, char **argv)
{
    QApplication a(argc, argv); 
    
    QWidget vBox;
#if QT_VERSION >= 0x040000
    vBox.setWindowTitle("AirSensor");
#else
    vBox.setCaption("AirSensor");
#endif

    AirSensor *plot = new AirSensor(&vBox);

    QVBoxLayout *layout = new QVBoxLayout(&vBox);
    layout->addWidget(plot);

#if QT_VERSION < 0x040000
    a.setMainWidget(&vBox);
#endif

    vBox.resize(600,200);
    vBox.show();

    return a.exec();  
}   

