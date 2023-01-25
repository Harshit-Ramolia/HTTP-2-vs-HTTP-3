from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.link import TCLink

class Topology( Topo ):
    
    def __init__( self ):
        Topo.__init__(self)

        S1 = self.addHost('S1')
        C1  = self.addHost('C1')
        C2  = self.addHost('C2')
        C3  = self.addHost('C3')
        C4  = self.addHost('C4')
        R1 = self.addSwitch('R1')
        R2 = self.addSwitch('R2')

        #add links
        self.addLink(S1, R1, cls = TCLink, bw = 20)
        self.addLink(R1, R2, cls = TCLink, bw = 8)
        self.addLink(R2, C1, cls = TCLink, bw = 10)
        self.addLink(R2, C2, cls = TCLink, bw = 10)
        self.addLink(R2, C3, cls = TCLink, bw = 10)
        self.addLink(R2, C4, cls = TCLink, bw = 10)
        
def Run():
    topo = Topology()
    net = Mininet(topo=topo)
    net.start()
    dumpNodeConnections(net.hosts)
    CLI(net)
    S1, C1, C2, C3, C4 = net.get('S1', 'C1', 'C2', 'C3', 'C3')    
    result = S1.cmd('cd HTTP-2-vs-HTTP-3/HTTP2')
    result = S1.cmd('pwd')
    print(result)
    # result = S1.cmd('node server.js')
    # print("Server started")

    # result = C1.cmd('cd dash.js')
    # result = C1.cmd('python scraper.py')
    # print("Metrics being captured")
    # result = C1.cmd('npm run start')

    # print(result)
    # result = S1.cmd('ifconfig')
    # print(result)

    net.stop()

Run()