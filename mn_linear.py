from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.link import TCLink

class MyTopo( Topo ):
    
    def __init__( self ):
        Topo.__init__(self)

        A = self.addHost('A')
        B = self.addHost('B')

        # define links, BW and delay
        self.addLink(A, B, cls = TCLink, bw = 2, loss=15, delay='5ms')

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