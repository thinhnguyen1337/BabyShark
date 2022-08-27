import os, sys, time

import core.config
from core.packet import *
from core.frame import NetworkFrame
from core.optformat import *
import babyshark
from core.babyshark_http.esphttpsniff import *

from scapy.all import *

def process_http_packet(http_packet):
    esp = Babyshaek()
    try:
        if http_packet.haslayer(HTTPRequest) or http_packet.haslayer(IP):
            core.config.source_ip_address = http_packet[IP].src
            core.config.destination_ip_address = http_packet[IP].dst 
            #url = http_packet[HTTPRequest].Host.decode() 
            esp.print_babyshark_notab(f"{core.config.source_ip_address} (requested) {core.config.destination_ip_address} with HTTP/HTTPS")
    except IndexError as ie:
        pass