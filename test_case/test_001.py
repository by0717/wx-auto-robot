import pytest
import os
import sys
import allure
import time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
try:
    from Common.logging_set import logging
    from Common.ip_get import get_ipv4_address
    from Common.ip_ping import ping_dut
    from Common.wifi_set import wifi_connect, wifi_diconnect
except Exception:
    raise


hostname = "192.168.51.1"
ifname = "WLAN"
wifi_ssid_2G = "Qrouter-E82E"
wifi_ssid_5G = "Qrouter-E82E-5G"
wifi_key_2G = "453453ML"
wifi_key_5G = "453453ML"


@allure.epic("By_wifi Test Demo")
@allure.feature("Test wifi reconnect")
@allure.story("Test wifi re-connect and ipv4 status")
class Test_WIFI_reconnect:
    @allure.title("Test_case_2G")
    def test_2G_connect(self):
        logging.info("Check ping host")
        if ping_dut(hostname) is True:
            logging.info("ping {} Pass".format(hostname))
        else:
            logging.info("ping {} Fail".format(hostname))
        logging.info("---------------Disconnect WIFI at first---------------------")
        wifi_diconnect()
        logging.info("---------------Begin to connect 2G wifi---------------------")
        wifi_connect_stauts = wifi_connect(wifi_ssid_2G, wifi_key_2G)
        time.sleep(5)
        if wifi_connect_stauts is True:
            logging.info("Connet {} Pass".format(wifi_ssid_2G))
            time.sleep(5)
            IP_Addr_V4 = get_ipv4_address(ifname)
            logging.info('ipv4:' + IP_Addr_V4)
            time.sleep(2)
            if ping_dut(hostname) is True:
                logging.info("ping {} Pass".format(hostname))
            else:
                logging.info("ping {} Fail".format(hostname))
            assert "192.168.51" in IP_Addr_V4
        else:
            logging.info("Connect {} Fail".format(wifi_ssid_2G))
            assert wifi_connect_stauts

    @allure.title("Test_case_5G")
    def test_5G_connect(self):
        logging.info("Check ping host")
        if ping_dut(hostname) is True:
            logging.info("ping {} Pass".format(hostname))
        else:
            logging.info("ping {} Fail".format(hostname))
        logging.info("---------------Disconnect WIFI at first---------------------")
        wifi_diconnect()
        logging.info("---------------Begin to connect 5G wifi--------------------")
        wifi_connect_status = wifi_connect(wifi_ssid_5G, wifi_key_5G)
        time.sleep(5)
        if wifi_connect_status is True:
            logging.info("Connet {} Pass".format(wifi_ssid_5G))
            time.sleep(5)
            IP_Addr_V4 = get_ipv4_address(ifname)
            logging.info('ipv4:' + IP_Addr_V4)
            time.sleep(2)
            if ping_dut(hostname) is True:
                logging.info("ping {} Pass".format(hostname))
            else:
                logging.info("ping {} Fail".format(hostname))
            assert "192.168.51" in IP_Addr_V4
        else:
            logging.info("Connect {} Fail".format(wifi_ssid_2G))
            assert wifi_connect_status


if __name__ == '__main__':
    pytest.main(['--count=200', '--repeat-scope=session', '--report=WIFI_ReConnect.thml', '--title=IPV4_Get_Test', '--tester=Barry_Bai', '--desc=Test WIFI connect get IPv4', '--template=2'])
