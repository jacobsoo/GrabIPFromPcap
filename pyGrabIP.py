from scapy.all import *
import operator

# Main Program
def main(fPcap):
    packets = rdpcap(fPcap)
    stats = {}
    for packet in packets:
        try:
            dst = packet.payload.dst
            if dst not in stats: stats[dst] = 0
            stats[dst] += 1
        except:
            pass
    for k,v in sorted(stats.iteritems(), key=operator.itemgetter(1))[::-1]:
        import pygeoip
        gi = pygeoip.GeoIP('.\\GeoIP\\GeoIP.dat')
        print k
        print "GeoIP: %s" % gi.country_code_by_addr(k)

# Banner
def Banner():
    print("=================================================")
    print("GrabIP from PCAP v0.1                            ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <Name_of_PCAP_File.pcap>\n") % (cmd)

if __name__ == '__main__':
    Banner()
    if len(sys.argv)<2:
        help_menu(sys.argv[0])
    else:
        fPcap = sys.argv[1]
        main(fPcap)