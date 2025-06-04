# Python_Projects

Bu depoda çeşitli Python örnekleri yer almaktadır.

## WebSocket Desktop Server

`websocket_server.py` dosyası, Android istemcilerin bağlanabileceği basit bir WebSocket sunucusudur.

### Gereksinimler

- Python 3.8+
- websockets kütüphanesi (`pip install websockets`)

### Çalıştırma

```bash
python websocket_server.py
```

Sunucu `ws://0.0.0.0:8765` adresinde dinlemeye başlar.

### Android İstemci Örneği

Android tarafında [OkHttp](https://square.github.io/okhttp/) kütüphanesiyle WebSocket bağlantısı açabilirsiniz:

```kotlin
val client = OkHttpClient()
val request = Request.Builder().url("ws://SERVER_IP:8765").build()
client.newWebSocket(request, object : WebSocketListener() {
    override fun onOpen(webSocket: WebSocket, response: Response) {
        webSocket.send("Hello from Android!")
    }

    override fun onMessage(webSocket: WebSocket, text: String) {
        Log.d("WS", "Received: $text")
    }
})
```

Bu kod, sunucuya mesaj gönderir ve gelen mesajları log'a yazar.
