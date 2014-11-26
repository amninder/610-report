import sys
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, \
                                       WebSocketClientProtocol, \
                                       connectWS
from time import mktime
import time
import datetime
import json


class BroadcastClientProtocol(WebSocketClientProtocol):
   """
   Simple client that connects to a WebSocket server, send a
   message and print everything it receives.
   """

   def sendMsg(self):
      client_time = float("%.20f"%time.time())
      self.sendMessage("{}".format(client_time).encode('utf8'))
      reactor.callLater(0.1, self.sendMsg)

   def onOpen(self):
      self.sendMsg()

   def onMessage(self, payload, isBinary):
      if not isBinary:
         dict = json.loads("{}".format(payload.decode('utf8')))
         client_time =  float(dict[u'client_time'])
         now = float("%.20f"%time.time())
         if client_time > now:
            diff = client_time - now
         else:
            diff = now - client_time
         with open("data_100.txt", "a+") as f:
            f.write("{}\n".format(diff))
         f.close()
         print diff


if __name__ == '__main__':

   if len(sys.argv) < 2:
      print("Need WebSocket server address, i.e. ws://localhost:9000")
      sys.exit(1)

   factory = WebSocketClientFactory(sys.argv[1])
   factory.protocol = BroadcastClientProtocol
   connectWS(factory)

   reactor.run()