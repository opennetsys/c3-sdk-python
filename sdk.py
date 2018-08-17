from ctypes import *
from queue import Queue
from threading import Thread
import socket
import json

# note: these files must first be built. see the make file
hashing = CDLL('./lib/hashing/hashing.so')
hexutil = CDLL('./lib/hexutil/hexutil.so')
config = CDLL('./lib/config/config.so')

ErrMethodAlreadyRegistered = Exception("method already registered")
ErrMethodNotExists = Exception("method does not exist")
ErrIncorrectNumberOfArgs = Exception("method requires two arguments")

class C3():
    def __init__(self, statefile):
        self.methods = {}
        self.state = {}
        self.q = Queue(maxsize=0)
        self.statefile = statefile

    def registerMethod(self, methodName, types, ifn):
        methodNameHash = c_char_p(hashing.HashToHexString(methodName).value.decode('utf-8')
        if methodNameHash in self.methods:
            raise ErrMethodAlreadyExists

        self.methods[methodNameHash] = lambda ifn, *args:
            if len(args) != 2:
                raise ErrIncorrectNumberOfArgs

            key = args[0]
            keyBytes = hexutil.DecodeString(keyHex)
            key = keyBytes.decode('utf-8')

            val = args[1]
            valBytes = hexutil.DecodeString(valHex)
            val = valBytes.decode('utf-8')

            try:
                res = ifn(key, val)
                print("[c3] result", res)
            except Exception as inst:
                print("[c3] invokation failed", inst)
            
    def setInitialState(self):
        currState = ""

        file = open(self.statefile, “r”) 
        currState = file.read() 

        if len(currState) == 0:
            print("no current state")
            return

        b = bytearray()
        b.extend(map(ord, t.inp))
        arr = (c_byte * len(b))(*b)

        res = stringutil.CompactJSON(arr)

        self.state = json.loads(res.decode("utf-8"))
        print("initial state loaded")

    def process(self, payloadBytes):
        payload = json.loads(payloadBytes)

        if len(payload) <= 1:
            return

        # ifc format is [a, b, c]
        if isinstance(payload[0], str):
            self.invoke(payload[0], payload[1:])

        # ifc format is [[a, b, c], [a, b, c]]
        for ifc in payload:
            self.invoke(ifc[0], *ifc[1:])

    def invoke(self, method, params):
        if method not in self.methods:
            raise ErrMethodNotExists

        fn = self.methods[method]
        try:
            fn(*params)
        except Exception as inst:
            print("[c3] err invoking method", inst)
            return
    
    def listen(self):
        while True:
            self.process(self.q.get())
            q.task_done()

    def serve():
        host = c_char_p(config.ServerHost()).value
        port = c_int(config.ServerPort()).value

        server = Server(host, port, self.q)

        worker = Thread(target=server.run)
        # worker.setDaemon(True)
        worker.start()

def NewC3():
    stateFilePath = c_char_p(config.TempContainerStateFilePath()).value
    c3 = C3(stateFilePath)

    c3.setInitialState()

    worker = Thread(target=c3.listen)
    # worker.setDaemon(True)
    worker.start()

    return c3

class Server():
    def __init__(self, host, port, q):
        self.host = host
        self.port = port
        self.q = q

    def run():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(1)  # max backlog of connections

        print 'Listening on {}:{}'.format(bind_ip, bind_port)


        def handle_conn(conn):
            data = []
            while 1:
                tmp = conn.recv(1024)
                if not tmp: break
                data.append(tmp)

            self.q.put(''.join(data))
            conn.close()

        while True:
            client_sock, address = server.accept()
            print 'Accepted connection from {}:{}'.format(address[0], address[1])
            client_handler = threading.Thread(
                target=handle_conn,
                args=(client_sock,)  # note: comment required!
            )

            client_handler.start()
