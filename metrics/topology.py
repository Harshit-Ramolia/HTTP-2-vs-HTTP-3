import subprocess
import multiprocessing
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.util import dumpNodeConnections

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
        
def launch_server():
    S1.cmd('cd ../HTTP2')
    result = S1.cmd('pwd')
    print(result)

    print("Starting server")
    result = S1.cmd('node server.js')
    print(result)
    return

def launch_client():
    result = C1.cmd('cd ../../dash.js')
    result = C1.cmd('pwd')
    print(result)

    # result = C1.cmd('npm run start')
    return

def launch_scraper():
    result = C1_.cmd('pwd')
    print(result)
    result = C1_.cmd('python scraper.py')
    print(result)
    return


topo = Topology()
net = Mininet(topo=topo)
# net.addNAT().configDefault()
net.start()
dumpNodeConnections(net.hosts)
# CLI(net)
S1, C1, C2, C3, C4 = net.get('S1', 'C1', 'C2', 'C3', 'C4')    
C1_ = net.get('C1')

### trying popen

# proc = subprocess.Popen(['sudo', 'mn'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
# proc.stdin.write('ls')
# print(proc.stdout.readline())



### trying pexpect

# child = pexpect.spawn('xterm S1')
# child.sendline('pwd')
# print(child.read())
# child.interact()



### trying multiprocessing

# s1 = multiprocessing.Process(target = launch_server) 
# c1_client = multiprocessing.Process(target = launch_client) 
# c1_scraper = multiprocessing.Process(target = launch_scraper) 

# s1.start()
# c1_client.start()
# c1_scraper.start()



### trying CLI

# S1.cmd('cd ../Express')
# result = S1.cmd('pwd')
# print(result)
# result = S1.cmd('npm install')
# print(result)

# launch_scraper()

# S1.cmd('cd ../HTTP2')
# result = S1.cmd('pwd')
# print(result)

# result = S1.cmd('node server.js')
# print(result)
# print("Server started")

# result = S1.cmd('cd metrics')
# result = S1.cmd('python scraper.py')
# print(result)

# result = C1.cmd('cd dash.js')
# result = C1.cmd('python scraper.py')
# print("Metrics being captured")
# result = C1.cmd('npm run start')

# print(result)
# result = S1.cmd('ifconfig')
# print(result)

net.stop()
