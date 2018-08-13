#sudo mn --custom extras/sflow.py --custom ~/learn/py/test.py --topo mytopo --link tc
from mininet.topo import Topo
from mininet.link import TCLink,TCIntf
from mininet.net import Mininet
class MyTopo( Topo ):
    "My first topology example."

    def __init__( self ):
        "Create my first  topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches

        switch_1 = self.addSwitch( 'S1',dpid='0000000000000001' )
        switch_2 = self.addSwitch( 'S2',dpid='0000000000000002' )
        switch_3 = self.addSwitch( 'S3',dpid='0000000000000003' )
        switch_4 = self.addSwitch( 'S4',dpid='0000000000000004' )
        switch_5 = self.addSwitch( 'S5',dpid='0000000000000005' )
        switch_6 = self.addSwitch( 'S6',dpid='0000000000000006' )
        switch_7 = self.addSwitch( 'S7',dpid='0000000000000007' )
        switch_8 = self.addSwitch( 'S8',dpid='0000000000000008' )
        #switch_1_hosts
        switch_1_host_1 = self.addHost( 'h1' )
        switch_1_host_2 = self.addHost( 'h2' )
       
        #switch_2_hosts
        switch_2_host_1 = self.addHost( 'h3' )
        switch_2_host_2 = self.addHost( 'h4' )
       
        #switch_3_hosts
        switch_3_host_1 = self.addHost( 'h5' )
        switch_3_host_2 = self.addHost( 'h6' )
        
        #switch_4_hosts
        switch_4_host_1 = self.addHost( 'h7' )
        switch_4_host_2 = self.addHost( 'h8' )
       
        #switch_5_hosts
        switch_5_host_1 = self.addHost( 'h9' )
        switch_5_host_2 = self.addHost( 'h10')
        
        #switch_6_hosts
        switch_6_host_1 = self.addHost( 'h11' )
        switch_6_host_2 = self.addHost( 'h12' )
        
        #switch_7_hosts
        switch_7_host_1 = self.addHost( 'h13' )
        switch_7_host_2 = self.addHost( 'h14' )
        
        #switch_8_hosts
        switch_8_host_1 = self.addHost( 'h15' )
        switch_8_host_2 = self.addHost( 'h16' )
       

        # Add links
        self.addLink( switch_1, switch_2,bw=100)
        self.addLink( switch_1, switch_3,bw=100)
        self.addLink( switch_1, switch_4,bw=100)
        self.addLink( switch_2, switch_5,bw=100)
        self.addLink( switch_3, switch_4,bw=100)
        self.addLink( switch_3, switch_6,bw=100)
        self.addLink( switch_4, switch_8,bw=100)
        self.addLink( switch_5, switch_8,bw=100)
        self.addLink( switch_6, switch_8,bw=100)
        self.addLink( switch_6, switch_7,bw=100)
        self.addLink( switch_8, switch_7,bw=100)

        self.addLink( switch_1_host_1 , switch_1 )
        self.addLink( switch_1_host_2 , switch_1 )
        

        self.addLink( switch_2_host_1, switch_2 )
        self.addLink( switch_2_host_2, switch_2 )
        

        self.addLink( switch_3_host_1, switch_3 )
        self.addLink( switch_3_host_2, switch_3 )
        

        self.addLink( switch_4_host_1, switch_4 )
        self.addLink( switch_4_host_2, switch_4 )
        

        self.addLink( switch_5_host_1, switch_5 )
        self.addLink( switch_5_host_2, switch_5 )
        

        self.addLink( switch_6_host_1, switch_6 )
        self.addLink( switch_6_host_2, switch_6 )
        

        self.addLink( switch_7_host_1, switch_7 )
        self.addLink( switch_7_host_2, switch_7 )
        

        self.addLink( switch_8_host_1, switch_8 )
        self.addLink( switch_8_host_2, switch_8 )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }
