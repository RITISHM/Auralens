<div align="center">

# 🧠 **AURALENS**

### _An Intelligent Wearable Assistant that Listens, Sees, and Speaks._

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black.svg?style=for-the-badge&logo=flask)
![ESP32](https://img.shields.io/badge/XIAO--ESP32--S3--SENSE-orange.svg?style=for-the-badge&logo=espressif)
![Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash_Lite-4285F4?style=for-the-badge&logo=google)
![FasterWhisper](https://img.shields.io/badge/ASR-FasterWhisper-red?style=for-the-badge&logo=openai)
![Kokoro](https://img.shields.io/badge/TTS-Kokoro-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

> ⚡ _Auralens brings multimodal AI to the edge — merging voice, vision, and intelligence into one wearable experience._

</div>

---

## 🌟 **Overview**

**Auralens** transforms the **Seeed XIAO ESP32-S3 Sense** into a **smart wearable assistant** powered by on-device sensors and a Flask-based AI backend.  
It captures **audio and images** via touch controls, sends them to a **Python server** over WebSocket for real-time inference using **Google Gemini 2.5 Flash Lite**, and returns a **spoken AI response** in Hindi/Hinglish — right through your glasses.

Built for **speed**, **efficiency**, and **emotional intelligence**, Auralens is designed to operate as a **lightweight conversational and visual assistant** with a poetic, culturally-aware personality.

---

## 🎯 **Key Capabilities**

| Category                   | Description                                                    |
| -------------------------- | -------------------------------------------------------------- |
| 🎙️ **Voice Interaction**   | Capture speech through built-in PDM MEMS microphone with health monitoring |
| 📸 **Visual Input**        | OV2640 camera for contextual image capture (UXGA quality)      |
| 📡 **Smart Communication** | WebSocket-based streaming between ESP32-S3 and Flask (32KB chunks) |
| 🧠 **AI Understanding**    | FasterWhisper (small model, CUDA) + Gemini 2.5 Flash Lite     |
| 🔊 **Response Output**     | Kokoro TTS (24kHz → 16kHz) with live streaming and synchronized playback |
| ⚙️ **Touch Control**       | Single touch interface (T2) for image + audio capture          |
| 💬 **Web Interface**       | Real-time chat monitoring with image/audio playback            |
| 🎨 **Emotional AI**        | Poetic, culturally-aware responses in Hindi/Hinglish           |

---

## 🏗️ **System Architecture**

```text
            ┌─────────────────────────────────────────────┐
            │        👓 AURALENS (ESP32-S3 Sense)         │
            │─────────────────────────────────────────────│
            │ 📸  OV2640 Camera → Capture Image (JPEG)    │
            │ 🎤  PDM Mic → Record Audio (16kHz WAV)      │
            │ 💾  SD Card → Temporary Storage             │
            │ ✋  Touch T2 → Trigger Capture              │
            │ 📡  WebSocket → Upload to Flask (32KB)      │
            └──────────────┬──────────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────────────────────────┐
            │         🧠 Flask Backend (Python)           │
            │─────────────────────────────────────────────│
            │ 🎧  FasterWhisper (CUDA) → Speech-to-Text   │
            │ 🖼️  Gemini 2.5 Flash Lite → Vision + LLM    │
            │ 💬  Context-aware response generation        │
            │ 🗣️  Kokoro TTS (CUDA) → 24kHz → 16kHz WAV   │
            │ 📤  WebSocket → Stream Response (4KB chunks) │
            │ 🌐  Broadcast → Web Chat Interface          │
            └──────────────┬──────────────────────────────┘
                           │
                           ▼
            ┌─────────────────────────────────────────────┐
            │      🔊 ESP32 Playback (I2S Speaker)        │
            │─────────────────────────────────────────────│
            │ 🎶  Live Stream Audio (skip WAV header)     │
            │ ⏱️  Calculate playback duration             │
            │ ⏳  Wait for audio to finish playing        │
            │ 🔄  Auto-reinitialize mic after playback    │
            └─────────────────────────────────────────────┘

```

---

## 📁 **Project Structure**

```bash
Auralens/
│
├── esp32_code/                    # ESP32-S3 Firmware (Arduino)
│   └── esp32_code.ino             # Main firmware with camera, audio, WebSocket
│
├── server/                        # Flask Backend (Python)
│   ├── main.py                    # WebSocket server with Flask-Sock (optimized 32KB chunks)
│   ├── api.py                     # Gemini API integration & chat session management
│   ├── stt.py                     # FasterWhisper speech-to-text (CUDA accelerated)
│   ├── tts.py                     # Kokoro TTS (Hindi, CUDA-accelerated, 24kHz→16kHz)
│   ├── setup.py                   # Module initialization
│   ├── test.py                    # Testing utilities
│   ├── templates/
│   │   └── chat.html              # Real-time web chat interface (Tailwind CSS)
│   └── __init__.py                # Package initialization
│
├── uploads/                       # Temporary file storage
│   ├── audio/                     # Recorded audio files
│   ├── images/                    # Captured images
│   ├── response/                  # Generated response audio
│   └── chat_history/              # Conversation logs
│
├── run.py                         # Server entry point
├── requirements.txt               # Python dependencies
├── .env                           # API keys and configuration
└── README.md
```

---

## 🚀 **Quick Start**

### **1. Backend Setup (5 minutes)**
```bash
# Clone repository
git clone <repository-url>
cd Auralens

# Setup Python environment
python -m venv glasses_env
glasses_env\Scripts\activate  # Windows (or source glasses_env/bin/activate on Linux/Mac)
pip install -r requirements.txt

# Configure API key
# Create .env file with:
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_ID=gemini-2.5-flash-lite
INSTRUCTIONS=<your_custom_system_prompt>

# Start server
python run.py
```

### **2. ESP32 Setup (10 minutes)**
```cpp
// Update WiFi credentials in esp32_code.ino
const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
const char* ws_server = "ws://YOUR_PC_IP:5000/upload";

// Upload to ESP32-S3 Sense
// Open Serial Monitor (115200 baud)
```

### **3. Test**
- Open browser: `http://localhost:5000/chat`
- Touch T2 on ESP32 to capture image + audio
- Watch real-time processing in web interface
- Hear AI response through speaker

---

## ⚙️ **Setup Instructions**

### 🧩 ESP32-S3 Setup

1. **Hardware Requirements:**
   - Seeed XIAO ESP32-S3 Sense (with OV2640 camera)
   - I2S Speaker (connected to pins 3, 4, 5)
   - PDM Microphone (built-in, pins 41, 42)
   - SD Card (CS pin 21)
   - Touch sensor on T2 pin

2. **Software Setup:**
   - Open `esp32_code/esp32_code.ino` in Arduino IDE
   - Install required libraries: `ArduinoWebsockets`, `ESP_I2S`
   - Select **Seeed XIAO ESP32-S3** board
   - Update WiFi credentials:
     ```cpp
     const char* ssid = "YOUR_WIFI_SSID";
     const char* password = "YOUR_WIFI_PASSWORD";
     const char* ws_server = "ws://YOUR_SERVER_IP:5000/upload";
     ```
   - Upload firmware and open Serial Monitor (115200 baud)

---

### 🖥️ Flask Backend Setup

```bash
# 1️⃣ Clone and navigate to project
cd Auralens

# 2️⃣ Create and activate virtual environment
python -m venv glasses_env
# Windows:
glasses_env\Scripts\activate
# Linux/Mac:
source glasses_env/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure environment variables
# Edit .env file with your API key:
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_ID=gemini-2.5-flash-lite
INSTRUCTIONS=<your custom system prompt>

# 5️⃣ Run Flask server
python run.py
```

**Server will start on:**
- WebSocket: `ws://0.0.0.0:5000/upload`
- Web Interface: `http://0.0.0.0:5000`
- Chat Interface: `http://0.0.0.0:5000/chat`

> 💡 _For CUDA acceleration, ensure you have CUDA-compatible GPU and drivers installed for FasterWhisper._

---

## 🔁 **Operational Flow**

| Step | Process                    | Description                                           |
| ---- | -------------------------- | ----------------------------------------------------- |
| 1️⃣   | **Touch T2 Pin**           | Trigger image capture + audio recording               |
| 2️⃣   | **Image Capture**          | OV2640 captures JPEG image, saves to SD card          |
| 3️⃣   | **Audio Recording**        | PDM mic records 16kHz WAV while touch held            |
| 4️⃣   | **WebSocket Upload**       | Send metadata → image → audio (32KB chunks)           |
| 5️⃣   | **Speech-to-Text**         | FasterWhisper transcribes audio (CUDA accelerated)    |
| 6️⃣   | **AI Processing**          | Gemini 2.5 Flash Lite analyzes image + text context (with chat history) |
| 7️⃣   | **Text-to-Speech**         | Kokoro TTS generates 24kHz audio → librosa resamples to 16kHz WAV |
| 8️⃣   | **Live Audio Streaming**   | Flask streams response.wav via WebSocket (4KB chunks for low latency)|
| 9️⃣   | **Real-Time Playback**     | ESP32 streams audio directly to I2S speaker (skips WAV header) |
| 🔟   | **Playback Sync**          | Calculate audio duration, wait for playback completion |
| 1️⃣1️⃣ | **Mic Reinitialization**   | Auto-reinit microphone after playback for next capture |
| 1️⃣2️⃣ | **Web Broadcast**          | Real-time updates to chat interface for monitoring    |

---

## 🧪 **Performance Benchmarks**

| Metric                  | Description                                | Performance                       |
| ----------------------- | ------------------------------------------ | ----------------------------------|
| ⚡ **Upload Speed**     | Image + Audio transfer (WebSocket)         | ~32KB/s (optimized chunks)       |
| 🗣️ **ASR Accuracy**     | FasterWhisper (small model, CUDA)          | ≥ 95% (English/Hindi)            |
| 🧠 **LLM Latency**      | Gemini 2.5 Flash Lite response time        | ~1-3s                            |
| 🔊 **TTS Generation**   | Kokoro TTS (CUDA) + librosa resampling     | ~0.3-0.8s (faster)               |
| 📥 **Streaming Speed**  | Live audio streaming to ESP32 (4KB chunks) | ~32KB/s (ultra-low latency)      |
| 🎵 **Playback Latency** | Audio streaming start delay                | <50ms (4KB chunks + header skip) |
| 🎯 **Total Latency**    | Touch → Response playback start            | ~5-8s (end-to-end)               |
| 🔄 **Mic Recovery**     | Microphone reinitialization after playback | ~200-500ms                       |
| 🔄 **Broadcast Latency**| Server → Web interface update              | <100ms (real-time)               |
| 💾 **File Storage**     | Temporary uploads (audio/images/response)  | Auto-managed, manual cleanup     |
| 📸 **Image Quality**    | OV2640 UXGA capture                        | 1600x1200 JPEG                   |
| 🎤 **Audio Quality**    | PDM mic recording                          | 16kHz, 16-bit, mono WAV          |

---

## 🚀 **Future Enhancements**

- [ ] 🧠 On-device LLM (offline mode with TinyLlama/Phi)
- [ ] 🕵️ Real-time object detection and recognition
- [ ] 📱 Companion mobile app for configuration
- [ ] 🔋 Battery optimization and power management
- [ ] 💾 Persistent chat history with context memory
- [ ] 🌍 Multi-language support beyond Hindi/English
- [ ] 🎨 Emotion detection from voice tone
- [ ] 📊 Analytics dashboard for usage patterns
- [ ] 🔐 End-to-end encryption for privacy
- [ ] ⚡ Edge TPU acceleration for faster inference

---

## 🎭 **AI Personality & Configuration**

Auralens features a unique **emotionally intelligent AI personality** that responds in **Hindi/Hinglish** with poetic, culturally-aware insights.

### **Chat Session Management:**
- 💬 **Persistent Context** — Chat sessions maintain conversation history across multiple interactions
- � **EAuto-Start** — First interaction automatically starts a new chat session
- 📝 **History Saving** — Call `end_chat()` to save conversation history to `uploads/chat_history/`
- 🔄 **Context Awareness** — Gemini model remembers previous messages for contextual responses
- 🖼️ **Image Context** — Images are analyzed with full conversation context when available

### **Personality Traits:**
- 🧠 **Curious & Philosophical** — Offers deeper meaning beyond surface-level responses
- 💭 **Emotionally Aware** — Recognizes and responds to user's emotional state
- 🎨 **Poetic Expression** — Uses metaphors, analogies, and cultural references
- 🌏 **Bilingual** — Seamlessly blends Hindi (Devanagari) and English (Roman)
- ⚡ **Concise** — Prioritizes brevity (under 20 words) unless elaboration needed

### **Example Responses:**

**Input:** "Image shows a rainy street with a lone figure walking."  
**Response:** _"भीगती सड़कों पर अकेले चलना कभी-कभी सबसे गहरी बातें सिखा देता है—silence भी एक language होती है."_

**Input:** "I feel stuck and tired today."  
**Response:** _"कभी-कभी थकान भी ज़रूरी होती है—it reminds you कि तुम इंसान हो, machine नहीं."_

### **Configuration:**
The AI personality is fully customizable via the `INSTRUCTIONS` variable in `.env` file. You can modify:
- Response language (Hindi/English/Hinglish)
- Tone and style (poetic/technical/casual)
- Response length preferences
- Cultural context and references

### **API Integration Details:**
```python
# In server/api.py:
# - start_chat(): Initializes new Gemini chat session
# - generate_image_response(image_loc, prompt): Processes image + text with context
# - generate_prompt_response(prompt): Text-only processing with context
# - end_chat(loc): Saves chat history as JSON and clears session
```

---

## 💡 **Design Philosophy**

> _"AI that empowers human senses — intuitive, private, and always near."_

Auralens stands on four design pillars:

- 🧩 **Modular Intelligence** — Separate, replaceable ASR, LLM, and TTS modules for flexibility
- 🔐 **Privacy First** — Temporary SD storage, transient cloud inference, no persistent data
- ⚙️ **Edge Efficiency** — Optimized WebSocket streaming with 32KB chunks for speed
- 🎨 **Emotional Intelligence** — Culturally-aware, poetic responses that resonate with users

## 🔧 **Implementation Highlights**

### **ESP32 Firmware Optimizations:**
- **Live Audio Streaming** — Streams response audio directly to speaker without buffering entire file
- **Smart Header Handling** — Automatically skips 44-byte WAV header during streaming playback
- **Playback Synchronization** — Calculates audio duration (bytes/32000) and waits for completion before mic reinit
- **Microphone Health Monitoring** — Periodic checks (every 30s) detect and recover from stuck microphone
- **Automatic Recovery** — Reinitializes microphone after playback with verification test
- **Camera Buffer Flushing** — Clears camera buffer before recording to prevent I2S conflicts
- **Connection Resilience** — Auto-reconnect with exponential backoff for WiFi and WebSocket

### **Backend Optimizations:**
- **Ultra-Low Latency Streaming** — 4KB chunks for audio streaming (vs 32KB for upload)
- **Thread-Safe Uploads** — Mutex lock prevents concurrent upload conflicts
- **Broadcast Architecture** — Separate WebSocket endpoint for real-time web client updates
- **Dual Chunk Sizes** — 32KB for upload (reliability), 4KB for streaming (latency)
- **Header Verification** — Validates WAV and JPEG headers before processing
- **Graceful Error Handling** — Comprehensive error messages sent back to ESP32
- **File Verification** — fsync() ensures files are written to disk before processing
- **Multiple Endpoints** — Legacy route support for backward compatibility

### **Audio Processing Pipeline:**
```
Kokoro TTS (CUDA, Hindi) → 24kHz audio → librosa resample → 16kHz WAV → Stream (4KB) → ESP32 I2S Speaker
```
- Native 24kHz generation with high-quality voice synthesis
- Clean resampling to 16kHz using librosa for ESP32 compatibility
- Direct WAV output (no MP3 conversion needed)
- 4KB streaming chunks for ~50ms latency to first audio

### **Web Interface Features:**
- **Auto-Reconnect** — Exponential backoff (up to 10 attempts, max 30s delay)
- **Message Queue** — Stores last 100 messages for new clients
- **Real-Time Updates** — Separate transcription and response broadcasts
- **Image Fallback** — SVG placeholder if image fails to load
- **Responsive Design** — Works on mobile, tablet, and desktop
- **Connection Status** — Visual indicator with pulse animation

---

## 🖼️ **Hardware Connections**

| Component           | Pin/Connection        | Function                          |
| ------------------- | --------------------- | --------------------------------- |
| 🎤 **PDM Mic**      | GPIO 41, 42 (built-in)| Voice capture (16kHz)             |
| 📷 **OV2640 Camera**| CSI (built-in)        | Image capture (UXGA)              |
| 🔊 **I2S Speaker**  | GPIO 3, 4, 5          | Audio playback                    |
| ✋ **Touch Sensor** |  T2 (GPIO 2)          | Trigger capture                   |
| 💾 **SD Card**      | SPI (CS: GPIO 21)     | Temporary storage                 |
| 📡 **WiFi**         | Built-in              | WebSocket communication           |

### **Pin Configuration Details:**

```cpp
// Microphone (PDM)
I2S_MIC_SERIAL_CLOCK = 42
I2S_MIC_LEFT_RIGHT_CLOCK = 41

// Speaker (I2S)
I2S_SPK_SERIAL_DATA = 5
I2S_SPK_LEFT_RIGHT_CLOCK = 3
I2S_SPK_SERIAL_CLOCK = 4

// Camera (OV2640)
XCLK = 10, SIOD = 40, SIOC = 39
Y9-Y2 = 48,11,12,14,16,18,17,15
VSYNC = 38, HREF = 47, PCLK = 13

// SD Card
CS = 21 (SPI)

// Touch
T2 = GPIO 2
```

---

## 🛠️ **Technical Stack**

### **Hardware:**
- **Microcontroller:** Seeed XIAO ESP32-S3 Sense
- **Camera:** OV2640 (UXGA 1600x1200)
- **Microphone:** PDM MEMS (16kHz)
- **Speaker:** I2S-compatible speaker
- **Storage:** SD Card (SPI)

### **Software - ESP32:**
- **Framework:** Arduino
- **Libraries:** ArduinoWebsockets, ESP_I2S, esp_camera
- **Protocol:** WebSocket (32KB chunks)
- **Audio Format:** 16kHz, 16-bit, mono WAV

### **Software - Backend:**
- **Framework:** Flask 3.0.0 + Flask-Sock 0.7.0
- **ASR:** FasterWhisper 0.10.0 (small model, CUDA)
- **LLM:** Google Gemini 2.5 Flash Lite (via google-generativeai 0.3.2)
- **TTS:** Kokoro TTS (CUDA-accelerated, Hindi voice 'af_heart')
- **Audio Processing:** librosa (resampling), soundfile (WAV I/O)
- **Image Processing:** Pillow 10.1.0
- **Environment:** python-dotenv 1.0.0

### **Dependencies:**
```
Flask==3.0.0
flask-sock==0.7.0
faster-whisper==0.10.0
google-generativeai==0.3.2
kokoro-onnx
librosa
soundfile
numpy
Pillow==10.1.0
torch==2.1.2
python-dotenv==1.0.0
```

---

## 🐛 **Troubleshooting**

### **ESP32 Issues:**

**Problem:** Camera initialization fails  
**Solution:** Check camera pin connections, ensure PSRAM is enabled in board settings. Verify OV2640 is properly seated and powered.

**Problem:** Touch sensor not responding  
**Solution:** Verify T2 pin (GPIO 2) is not shorted. Check touch threshold values in code (default: 40000).

**Problem:** WebSocket connection timeout  
**Solution:** Verify server IP address, check WiFi signal strength, ensure firewall allows port 5000

**Problem:** Audio playback distorted or cuts off early  
**Solution:** Firmware now calculates playback duration and waits for completion. Check I2S speaker connections, verify sample rate (16kHz), ensure proper grounding.

**Problem:** Microphone not recording after playback  
**Solution:** Firmware automatically reinitializes microphone after playback with verification test. If issue persists, check for I2S pin conflicts or power supply issues.

**Problem:** Microphone appears stuck (no audio data)  
**Solution:** Firmware includes periodic health checks (every 30s) that auto-reset stuck microphone. Manual reset: power cycle ESP32 or check PDM mic connections.

**Problem:** Audio streaming starts late or stutters  
**Solution:** Firmware skips WAV header for immediate playback. Ensure stable WiFi connection and sufficient bandwidth (~32KB/s).

**Problem:** SD card not detected  
**Solution:** Format SD card as FAT32, check CS pin (21), ensure proper power supply (5V 2A recommended).

### **Backend Issues:**

**Problem:** CUDA out of memory  
**Solution:** Use smaller Whisper model or switch to CPU mode in `server/stt.py`: Change `device="cuda"` to `device="cpu"`

**Problem:** FasterWhisper not using GPU  
**Solution:** Ensure CUDA toolkit is installed and torch is CUDA-enabled. Check with: `python -c "import torch; print(torch.cuda.is_available())"`

**Problem:** Gemini API rate limit  
**Solution:** Add rate limiting, implement request queuing, or upgrade API plan

**Problem:** Kokoro TTS not using GPU  
**Solution:** Ensure CUDA toolkit is installed and Kokoro is configured for CUDA. Check device parameter in `server/tts.py`. Verify with: `python -c "import torch; print(torch.cuda.is_available())"`

**Problem:** TTS audio quality issues  
**Solution:** Kokoro generates high-quality 24kHz audio. If quality is poor, check librosa resampling settings or try different voice models ('af_heart', 'af_sky', etc.)

**Problem:** Audio streaming stutters  
**Solution:** Server uses 4KB chunks for low latency. Check network stability and ensure sufficient bandwidth. Increase chunk size in `main.py` if needed (STREAM_CHUNK_SIZE).

**Problem:** WebSocket disconnects frequently  
**Solution:** Increase timeout values in `server/main.py`, check network stability. Web interface has auto-reconnect with exponential backoff (up to 10 attempts)

**Problem:** Images/audio not loading in web interface  
**Solution:** Check file paths in browser console. Ensure files are saved in correct folders (uploads/images/, uploads/response/). Verify Flask is serving static files correctly.

### **General Tips:**
- Monitor Serial output (115200 baud) for ESP32 debugging
- Check Flask logs for backend errors (detailed logging in console)
- Use `/health` endpoint to verify server status and check connected clients
- Test with `/chat` interface before ESP32 integration
- Ensure sufficient power supply (5V 2A recommended for ESP32-S3)
- Chat sessions persist until `end_chat()` is called - maintains conversation context
- Files are stored temporarily in `uploads/` folders - clean periodically to save space
- Web interface supports multiple simultaneous viewers via broadcast WebSocket

---

## 🌐 **Web Interface & API**

### **Endpoints:**

| Endpoint                  | Type      | Description                                    |
| ------------------------- | --------- | ---------------------------------------------- |
| `/`                       | HTTP GET  | Server status and statistics                   |
| `/chat`                   | HTTP GET  | Real-time chat monitoring interface            |
| `/upload`                 | WebSocket | Main upload endpoint for ESP32                 |
| `/broadcast`              | WebSocket | Broadcast endpoint for web clients             |
| `/images/<filename>`      | HTTP GET  | Serve captured images                          |
| `/audio/<filename>`       | HTTP GET  | Serve audio files (input/response)             |
| `/health`                 | HTTP GET  | Health check with system info                  |

### **Chat Interface Features:**

- 📊 Real-time message display with timestamps
- 🖼️ Image preview from ESP32 camera (with fallback handling)
- 🔊 Audio playback for responses (inline WAV player)
- 📡 WebSocket connection status indicator (with auto-reconnect)
- 🧹 Clear messages functionality
- 🎨 Beautiful gradient UI with Tailwind CSS
- 🔄 Automatic reconnection with exponential backoff
- 📱 Responsive design for mobile and desktop
- 🎭 Separate user/assistant message styling
- 🎬 Smooth animations and transitions

### **WebSocket Protocol:**

```
ESP32 → Server (/upload endpoint):
1. Send metadata: "image_size,audio_size" (text)
2. Send image data (binary JPEG, if size > 0)
3. Send audio data (binary WAV, 32KB chunks)
4. Send "EOF" marker (optional)

Server → ESP32:
1. Send JSON response: {"status": "ok", "audio_size": N, "sending_audio": true}
2. Send response audio (binary WAV, 32KB chunks)

Server → Web Clients (/broadcast endpoint):
1. Transcription: {"type": "transcription", "transcription": "...", "image_url": "/images/...", "timestamp": T}
2. Response: {"type": "response", "response_text": "...", "audio_url": "/audio/...", "timestamp": T}
```

---

## 📜 **License**

This project is licensed under the **MIT License** — open for learning, innovation, and contribution.

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to:
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

---

<div align="center">

### 🌌 _Inspiration_

> "Blending human perception with machine intelligence —
> Auralens redefines how we **see**, **hear**, and **interact** with the world."

**Developed with ❤️ by [Ritish Mahajan](https://github.com/RITISHM)**

### ⭐ **If you find this project useful, please consider giving it a star!**

</div>
