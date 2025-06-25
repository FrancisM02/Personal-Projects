# This file is for scanning ports open on a given local IP address(HOST). You are required to input the HOST address, and if there is a error nothing will happened to prevent other
# potential problems. I have used outside resources 
import socket
import threading





def scanPort(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s variable is given the socket object for connection
    s.settimeout(3) # It will timeout after 3 seconds.

    try:
        s.connect((host,port)) # Will try to connect to the given host and port
        print(f"The port {port} is OPEN on {host}")
    except socket.error: # If a error occurs the PORT will be closed.
        pass

    finally:
        s.close() # This closes the SOCKET after its finished being used.



def scanAllPorts(host, startPort, endPort):

    threads = [] # This will create a thread helping streamline the scan process.
    for port in range(startPort,endPort + 1):

        t = threading.Thread(target=scanPort, args=(host,port))
        threads.append(t)
        t.start() 

    for t in threads:
        t.join()


def startScan(): # tHIS FUnction to help start the scanner

    host = input("Enter the hostname or address for scanning: ")
    startPort = int(input("Enter starting point for port numbers: "))
    endPort = int(input("Enter ending point for port numbers: "))

    # Starts scanning.
    print(f"Scan starting on HOST: {host} from ports {startPort} - {endPort}.....")
    scanAllPorts(host, startPort, endPort)
    print("Scan is complete.")

if __name__ == "__main__":
    startScan()
    