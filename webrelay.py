from machine import Pin
from time import sleep
import network
import socket

relay = Pin(2, Pin.OUT)

ssid = ""
password = ""

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        sleep(1)
    
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(state):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form action="./toggle">
            <input type="submit" value="toggle" />
            </form>
            <p>Relay is {state}</p>
            </body>
            </html>
            """
    return str(html)

def toggle(state):
    if state == "OFF":
        return "ON"
    if state == "ON":
        return "OFF"
    raise Exception("state not ON or OFF")

def serve(connection):
    state = 'OFF'
    relay.value(1)
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/toggle?':
            relay.toggle()
            state = toggle(state)
            html = "<!DOCTYPE html><html><head><meta http-equiv=\"refresh\" content=\"0; url=/\" /></head></html>"
            client.send(html)
            client.close()
            continue

        print(request)
        html = webpage(state)
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
