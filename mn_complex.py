from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.link import TCLink

class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__(self)

        C1 = self.addHost('C1')
        S1 = self.addHost('S1')
        S2 = self.addHost('S2')
        S3 = self.addHost('S3')
        S4 = self.addHost('S4')
        R1 = self.addSwitch('R1')
        R2 = self.addSwitch('R2')

        # define links, BW and delay
        self.addLink(C1, R1, cls = TCLink, bw = 10, delay = '1ms')
        self.addLink(R1, R2, cls = TCLink, bw = 8, delay = '1ms')
        self.addLink(R2, S1, cls = TCLink, bw = 10, delay = '1ms')
        self.addLink(R2, S2, cls = TCLink, bw = 10, delay = '1ms')
        self.addLink(R2, S3, cls = TCLink, bw = 10, delay = '1ms')
        self.addLink(R2, S4, cls = TCLink, bw = 10, delay = '1ms')

def Test():
    topo = MyTopo()
    net = Mininet(topo=topo)
    net.start()
    dumpNodeConnections(net.hosts)
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    Test()

# client: iperf -c 10.0.0.1 -t 120
# server: iperf -s