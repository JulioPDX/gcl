# Learning a Little about Containerlab

Hello all. This is the respository based on this [blog post](https://juliopdx.com/2021/12/10/my-journey-and-experience-with-containerlab/) and this [one](https://overlaid.net/2019/01/27/arista-bgp-evpn-configuration-example/)!.

## Getting Started

Feel free to use this example. You will need access to the same version of cEOS image I used. If you use another version, just make sure those changes are reflected in the `net.clab.yaml` file, as well as any configuration differences in the `/configs/post` directory.

## Installing requirements

```bash
# Downlad and install Containerlab
bash -c "$(curl -sL https://get-clab.srlinux.dev)"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Deploy topology

```bash
sudo containerlab deploy -t net.clab.yaml
```

## Run Deployment Script

You may need to alter the deployment script to point to the correct configuration files and inventory!

```bash
python3 deploy.py
```

## Deploying Clos Topology for VXLAN BGP EVPN

![Clos Topo](/images/topo.png)

If you would like to work with the Clos topology, please follow these directions. Creating the python virtual environment is still required! Build is based on the great blog post by [David Varnum](https://overlaid.net/2019/01/27/arista-bgp-evpn-configuration-example/), although this one is a bit smaller!

## Deploy Clos Topology

```bash
sudo containerlab deploy -t clos.clab.yaml
```

## Configure Deployment

If the startup configurations are not set, run the included python script to deploy the configurations.

```python
(venv) juliopdx@drone:~/git/gcl$ python3 deploy.py 
deploy_network******************************************************************
* client1 ** changed : False ***************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* client2 ** changed : False ***************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* client3 ** changed : False ***************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* client4 ** changed : False ***************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* ext ** changed : False *******************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring ext! ** changed : False --------------------------------------- INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* leaf1 ** changed : False *****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring leaf1! ** changed : False ------------------------------------- INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* leaf2 ** changed : False *****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring leaf2! ** changed : False ------------------------------------- INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* leaf3 ** changed : False *****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring leaf3! ** changed : False ------------------------------------- INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* leaf4 ** changed : False *****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring leaf4! ** changed : False ------------------------------------- INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* spine1 ** changed : False ****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring spine1! ** changed : False ------------------------------------ INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* spine2 ** changed : False ****************************************************
vvvv deploy_network ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
---- Configuring spine2! ** changed : False ------------------------------------ INFO
^^^^ END deploy_network ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(venv) juliopdx@drone:~/git/gcl$ 
```

In my case the deployments are already complete. Please note, you will still have to configure any client addresses.

## Check Neighbors

```bash
(venv) juliopdx@drone:~/git/gcl$ ssh admin@spine1
Password: 
spine1>en
spine1#show ip bgp summary 
BGP summary information for VRF default
Router identifier 10.0.250.1, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  10.0.1.1         4 65001             42        42    0    0 00:29:27 Estab   3      3
  10.0.1.3         4 65001             44        43    0    0 00:29:26 Estab   3      3
  10.0.1.5         4 65002             39        42    0    0 00:29:26 Estab   2      2
  10.0.1.7         4 65002             40        40    0    0 00:29:27 Estab   2      2
spine1#show bgp evpn summary 
BGP summary information for VRF default
Router identifier 10.0.250.1, local AS number 65000
Neighbor Status Codes: m - Under maintenance
  Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  10.0.250.11      4 65001             44        53    0    0 00:29:52 Estab   2      2
  10.0.250.12      4 65001             48        53    0    0 00:29:51 Estab   2      2
  10.0.250.13      4 65002             47        54    0    0 00:29:49 Estab   4      4
  10.0.250.14      4 65002             49        51    0    0 00:29:50 Estab   4      4
spine1#exit
Connection to spine1 closed.
(venv) juliopdx@drone:~/git/gcl$ ssh admin@leaf1
Password: 
leaf1>en
leaf1#show ip bgp summary 
BGP summary information for VRF default
Router identifier 10.0.250.11, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  10.0.1.0         4 65000             43        43    0    0 00:30:33 Estab   4      4
  10.0.2.0         4 65000             41        42    0    0 00:30:33 Estab   4      4
  10.0.3.1         4 65001             43        42    0    0 00:30:33 Estab   7      7
leaf1#show bgp evpn summary 
BGP summary information for VRF default
Router identifier 10.0.250.11, local AS number 65001
Neighbor Status Codes: m - Under maintenance
  Neighbor         V AS           MsgRcvd   MsgSent  InQ OutQ  Up/Down State   PfxRcd PfxAcc
  10.0.250.1       4 65000             54        45    0    0 00:30:50 Estab   8      8
  10.0.250.2       4 65000             54        52    0    0 00:28:43 Estab   8      8
leaf1#
```

## Testing L2

Client1(10.40.40.1) and Client3(10.40.40.3) are assigned to VLAN 40. There is no gateway involved at this point. 

```bash
(venv) juliopdx@drone:~/git/gcl$ docker exec -it client1 bash
bash-5.0# ifconfig eth1 10.40.40.1 netmask 255.255.255.0 up
bash-5.0# exit
exit
(venv) juliopdx@drone:~/git/gcl$ docker exec -it client3 bash
bash-5.0# ifconfig eth1 10.40.40.3 netmask 255.255.255.0 up
bash-5.0# ping -c 4 10.40.40.1
PING 10.40.40.1 (10.40.40.1) 56(84) bytes of data.
64 bytes from 10.40.40.1: icmp_seq=1 ttl=64 time=155 ms
64 bytes from 10.40.40.1: icmp_seq=2 ttl=64 time=24.9 ms
64 bytes from 10.40.40.1: icmp_seq=3 ttl=64 time=22.7 ms
64 bytes from 10.40.40.1: icmp_seq=4 ttl=64 time=23.0 ms

--- 10.40.40.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 22.742/56.382/154.891/56.879 ms
bash-5.0#
```

## Testing L3

Client2(10.12.12.10) and Client4(10.34.34.10) are on different networks. Lets validate connectivity over the fabric. 

```bash
(venv) juliopdx@drone:~/git/gcl$ docker exec -it client2 bash
bash-5.0# ifconfig eth1 10.12.12.10 netmask 255.255.255.0 up
bash-5.0# route add default gw 10.12.12.1
bash-5.0# ping -c 4 10.12.12.1
PING 10.12.12.1 (10.12.12.1) 56(84) bytes of data.
64 bytes from 10.12.12.1: icmp_seq=1 ttl=64 time=54.1 ms
64 bytes from 10.12.12.1: icmp_seq=2 ttl=64 time=11.4 ms
64 bytes from 10.12.12.1: icmp_seq=3 ttl=64 time=8.39 ms
64 bytes from 10.12.12.1: icmp_seq=4 ttl=64 time=10.3 ms

--- 10.12.12.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 8.391/21.055/54.143/19.133 ms
bash-5.0# exit
exit
(venv) juliopdx@drone:~/git/gcl$ docker exec -it client4 bash
bash-5.0# ifconfig eth1 10.34.34.10 netmask 255.255.255.0 up
bash-5.0# route add default gw 10.34.34.1
bash-5.0# ping -c 4 10.34.34.1
PING 10.34.34.1 (10.34.34.1) 56(84) bytes of data.
64 bytes from 10.34.34.1: icmp_seq=1 ttl=64 time=35.8 ms
64 bytes from 10.34.34.1: icmp_seq=2 ttl=64 time=8.96 ms
64 bytes from 10.34.34.1: icmp_seq=3 ttl=64 time=8.51 ms
64 bytes from 10.34.34.1: icmp_seq=4 ttl=64 time=9.30 ms

--- 10.34.34.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 8.514/15.643/35.807/11.644 ms
bash-5.0# ping -c 4 10.12.12.10
PING 10.12.12.10 (10.12.12.10) 56(84) bytes of data.
64 bytes from 10.12.12.10: icmp_seq=1 ttl=62 time=60.0 ms
64 bytes from 10.12.12.10: icmp_seq=3 ttl=62 time=52.8 ms

--- 10.12.12.10 ping statistics ---
4 packets transmitted, 2 received, 50% packet loss, time 3021ms
rtt min/avg/max/mdev = 52.771/56.362/59.954/3.591 ms
bash-5.0# 
```

## Testing external connectivity

I added some bogus default route on the ext node. This is then advertised into BGP but only under the vrf where Client2 and Client4 reside. Lets see if they can reach "10.80.40.1".

```bash
(venv) juliopdx@drone:~/git/gcl$ docker exec -it client4 bash
bash-5.0# ping -c 4 10.80.40.1
PING 10.80.40.1 (10.80.40.1) 56(84) bytes of data.
64 bytes from 10.80.40.1: icmp_seq=1 ttl=63 time=46.4 ms
64 bytes from 10.80.40.1: icmp_seq=2 ttl=63 time=39.5 ms
64 bytes from 10.80.40.1: icmp_seq=3 ttl=63 time=34.5 ms
64 bytes from 10.80.40.1: icmp_seq=4 ttl=63 time=29.9 ms

--- 10.80.40.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 29.869/37.571/46.415/6.128 ms
bash-5.0# 
```

## Conclusion

Feel free to use this and play around with these really awesome technologies. I cant stress this enough, the blog series by David is awesome and led to the creation of this lab topology. Thank you David!
