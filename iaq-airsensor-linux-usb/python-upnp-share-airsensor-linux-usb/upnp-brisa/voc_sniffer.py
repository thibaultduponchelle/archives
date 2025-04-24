# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php or see LICENSE file.
# Copyright 2007-2008 Brisa Team <brisa-develop@garage.maemo.org>

from brisa.core.reactors import install_default_reactor
reactor = install_default_reactor()

import os

from brisa.upnp.device import Device, Service


class VocSniffer(Service):

    def __init__(self):
        Service.__init__(self, 'VocSniffer',
                         'urn:schemas-upnp-org:service:VocSniffer:1',
                         '',
                         '/root/python-upnp-service/VocSniffer-scpd.xml')
        self.target = '/var/www/voc/values.txt'
        self.status = 440


    def readStatus(self) :
        file = open(self.target, "r")
        try:
          line = file.readline().rstrip('\n\r')
          file.close()
          return line
        except:
          file.close()
          return 335

    def soap_SetTarget(self, *args, **kwargs):
        self.target = kwargs['newTargetValue']
        print 'File path modified ' , self.target
        return {}

    def soap_GetTarget(self, *args, **kwargs):
        return {'RetTargetValue': self.target}

    def soap_GetStatus(self, *args, **kwargs):
        self.status = self.readStatus()
        return {'ResultStatus': self.status}



class SmartCharger(object):

    def __init__(self):
        self.server_name = 'Smart Charger Device'
        self.device = None

    def _create_device(self):
        project_page = 'https://www.polytech.unice.fr'
        self.device = Device('urn:schemas-upnp-org:device:SmartCharger:1',
                             self.server_name,
                             manufacturer='Polytech Nice Sophia',
                             manufacturer_url=project_page,
                             model_name='Smart Charger Device',
                             model_description='A UPnP Smart Charger Device',
                             model_number='1.0',
                             model_url=project_page)

    def _add_services(self):
        vs = VocSniffer()
        self.device.add_service(vs)

    def start(self):
        self._create_device()
        self._add_services()
        self.device.start()
        reactor.add_after_stop_func(self.device.stop)
        reactor.main()


if __name__ == '__main__':
    device = SmartCharger()
    device.start()
