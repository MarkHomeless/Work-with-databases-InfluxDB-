import socket 
class Sender_SOCKET:
    '''
    Сlass responsible for transmitting data over the network 
    It uses the TCP Protocol for data transmission
    Default IP and Port - local host(127.0.0.1) and port 5001
    Default timeout - 5 second
    '''
    def __init__(self, ip= '127.0.0.1', port = 5001, timeout = 5):
        '''
        Initialize the sender object next parameters:
            -self - link to object of class
            -ip - IP-adress of the server to connect to
            -port - the port to connect to
            -timeout - time of waining of connection
        '''
        self.ip = ip
        self.port = port
        self.timeout = timeout
    
    def close(self):
        '''
        break the connection
        '''
        self.sock.close()
    
    def send(self, message):
        '''
        Create conection and send message 
        If conection is lost - close the communication channel 
        '''
        #self.sock.settimeout(2)
        try:
            self.sock = socket.create_connection((self.ip, self.port), self.timeout)
            self.sock.sendall(message.encode('utf8'))
        except socket.timeout:
            print('send data timeout')
            self.close()
        except socket.error as ex:
            print('send data error: {}'.format(ex))
            self.close()
    