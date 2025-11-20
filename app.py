from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List
from fastapi.responses import FileResponse


from pyngrok import ngrok

#
# MEM_FILE = "memory.json"
#
# # ---- Load persistent memory ----
# if os.path.exists(MEM_FILE):
#     with open(MEM_FILE, "r", encoding="utf-8") as f:
#         try:
#             memory = json.load(f)
#         except:
#             memory = {}
# else:
memory = {}

# ---- Hardcoded Q&A with keywords ----
qa_pairs = [
        {
            "keywords": ["how to play qanun", "teach me"],
            "answer": "Strum, smile, repeat! 🙂 Hold the qanun on your lap, attach the little plectra to your index fingers, and pluck near the bridge. Start with simple arpeggios like C–E–G and keep your wrist relaxed. Practice slowly, then speed up."
        },
        {
            "keywords": ["teach qanun", "play qanun", "how to use string"],
            "answer": "Yes! Put on the plectra, tune a course to C, practice plucking C–E–G slowly, then move to small scales. Repeat daily — 5 minutes a day keeps the sour notes away."
        },
        {
            "keywords": ["string", "which string", "play qanun"],
            "answer": "The qanun's strings are grouped in courses (usually triples). Each course is tuned to a note; to change sharps/flats use the mandal levers. Example: to play C#, pluck the C course and flip the C mandal up. Tell me the specific note and I'll point to the exact course."
        },
        {
            "keywords": ["eastern", "what is eastern music",],
            "answer": "Absolutely — it’s made for eastern music and microtones. With different tuning it can also play western, jazz, pop, or other styles. Name a style and I’ll explain how the qanun would do it."
        },
        {
            "keywords": ["expressive", "melodies"],
            "answer": "Expressive melodies are musical sentences full of feeling — timing, ornamentation, dynamics and microtones shape emotion. On the qanun, mandals and gentle plucks make the melody expressive."
        },
        {
            "keywords": ["heavy", "is qanun heavy", 'qanun weight'],
            "answer": "Not heavy like gym gear, but not weightless. Light enough to carry with one arm carefully, heavy enough to respect."
        },
        {
            "keywords": ["big", "small", "is qanun big or small"],
            "answer": "Middle-sized: big enough to look impressive, small enough to carry with care. Think of a shallow wooden tray with strings."
        },
        {
            "keywords": ["how many strings", "strings of qanun"],
            "answer": "Typically around 78 strings arranged in grouped courses (usually triples). Configurations can vary."
        },
        {
            "keywords": ["creator", "creator of qanun", "who is the creator"],
            "answer": "No single inventor — the qanun evolved over centuries in the ancient Middle East (Mesopotamia and neighboring regions)."
        },
        {
            "keywords": ["first qanun player"],
            "answer": "Lost to time — early players weren’t recorded. The instrument emerged gradually and many cultures contributed to it."
        },
        # {
        #     "keywords": ["video"],
        #     "answer": "I don’t store videos here, but I can give step-by-step text lessons. For videos, search 'qanun beginner lesson' and follow along while I guide you."
        # },
        {
            "keywords": ["saleh", "why are you called that",'why is your name saleh','why are you called like that'],
            "answer": "I'm named Saleh as a tribute to the qanun player Mohamed Abdo Saleh who performed with Umm Kulthum — a musical nod to a great tradition.",
            "image": "http://127.0.0.1:8000/saleh"
        },
        {
            "keywords": ["Umm Kulthum"],
            "answer": "The Star of the East (كوكب الشرق),An Egyptian singer, songwriter, and cultural legend (born 1904, died 1975).",
            "image": "http://127.0.0.1:8000/Kulthum"
        },
        {
            "keywords": ["why qanun is so famous"],
            "answer": "The qanun is famous because of its beautiful, unique sound, its ability to play microtones found in Middle Eastern music, and its long history as an important lead instrument in Arabic, Turkish, and Armenian traditions.",
        },
        {
        "keywords": ["types of qanun", "famous types of qanun", "qanun types"],
        "types": [
             {"answer": "1. Arabic Qanun \n Used in countries like Egypt, Lebanon, Syria, and Iraq, Has 72–81 strings \n Known for a warm, rich tone Uses mandals for Arabic maqams",
              "image": "http://127.0.0.1:8000/type1"},
            {"answer": "2. Turkish Qanun \n Slightly smaller and lighter than the Arabic one, \n Has a brighter, sharper sound \n More mandals, allowing very fine microtone control",
            "image": "http://127.0.0.1:8000/type2" }
        ]
        },
{
            "keywords": ["qanun old","how old is qanun","how old is the qanun"],
            "answer": "The qanun is over 1,000 years old! 🕰️\n It originated in the Middle East, especially in regions like Egypt, Turkey, and Iraq, and is believed to date back to around the 9th century.",
        },
{
  "keywords": ["how to play", "play qanun", "play qanun video", "video of qanun","qanun video"],
  "answer": "here's a qanun player for the famous song 'enta umri' by Umm Kulthum",
  "video": "https://www.youtube.com/watch?v=vm1zHervgkQ"
}
    ]
# def save_memory():
#     with open(MEM_FILE, "w", encoding="utf-8") as f:
#         json.dump(memory, f, ensure_ascii=False, indent=2)
# atexit.register(save_memory)


# ---- FastAPI setup ----
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    sender: str
    message: str

def get_greeting() -> str:
    hour = datetime.now().hour
    if hour < 12:
        return "☀️ Good morning"
    elif hour < 18:
        return "🌞 Good afternoon"
    else:
        return "🌙 Good evening"

# ---- Serve MP3 files directly ----
@app.get("/sound1")
def qanun_sound1():
    return FileResponse("QanunSound1.mp3")

@app.get("/sound2")
def qanun_sound2():
    return FileResponse("QanunSound2.mp3")

# ---- Serve images directly ----
@app.get("/image1")
def qanun_image1():
    return FileResponse("qanun_image1.webp")

@app.get("/image2")
def qanun_image2():
    return FileResponse("qanun_image2.jpeg")
@app.get("/saleh")
def saleh_image():
    return FileResponse("mohamed-abdo-saleh.webp")
@app.get("/julien")
def julien_image():
    return FileResponse("Julien_Jalaleddin_Weiss.jpg")
@app.get("/Kulthum")
def kulthum_image():
    return FileResponse("umm_khalthom.jfif")
@app.get("/type1")
def qanun_type1():
    return FileResponse("arabic-qanun.webp")
@app.get("/type2")
def qanun_type2():
    return FileResponse("turkish-qanun.webp")

# ---- Chat logic ----
@app.post("/chat")
def chat(msg: Message):
    sender = msg.sender.strip().lower()
    raw = msg.message or ""
    text = raw.strip().lower()
    # sender_name = memory.get(sender, {}).get("name") or None

    for item in qa_pairs:
        if any(word.lower() in text for word in item["keywords"]):

            # --- Case 1: regular single-answer questions ---
            if "answer" in item:
                response = [{"text": item["answer"]}]
                if "image" in item:
                    response.append({"image": item["image"]})
                if "video" in item:
                    response.append({"video": item["video"]})
                return response

            # --- Case 2: special multi-type answers (like qanun types) ---
            if "types" in item:
                response = []
                for t in item["types"]:
                    response.append({"text": t["answer"]})
                    if "image" in t:
                        response.append({"image": t["image"]})
                return response


    # Initialize memory
    if sender not in memory:
        memory[sender] = {"name": None, "topic": None}
    user_state = memory[sender]
    responses: List[Dict[str, str]] = []

    # 1. --- Initial Greeting & Name Detection (Highest Priority) ---
    if user_state["name"] is None:
        # ... (Your existing Name Detection logic: /greet, my name is X, bare name, etc.) ...

        # --- (Existing name detection logic block goes here) ---
        name = None
        words = text.split()
        greetings = ["hi", "hello", "hey", "salam", "/greet"]  # Include /greet for frontend init

        # If the input is just the bare /greet command (from frontend initialization)
        if text == "/greet":
            greeting = get_greeting()
            return [{"text": f"{greeting}! I’m Saleh 🎵, your Qanun teacher.\nMay I know your name? 😊","sender_name": name}]

        # Pattern 1: "my name is ..."
        if "my name is" in text:
            name_candidate = text.split("my name is", 1)[-1].strip()
            if name_candidate:
                name = name_candidate.split()[0].title()

        # Pattern 2: "I am ..." or "I'm ..." or "Im ..."
        elif text.startswith(("i am ", "i'm ", "im ")):
            name_candidate = text.split(" ", 2)[-1].strip()
            if name_candidate:
                name = name_candidate.split()[0].title()

        # Pattern 3: Greeting + Name
        else:
            for greet in greetings:
                if text.startswith(greet):
                    remainder = text[len(greet):].strip()
                    if remainder:
                        first_word = remainder.split()[0]
                        if first_word.isalpha() and first_word.lower() not in {"facts", "history", "players", "sound",
                                                                               "image", "menu"}:
                            name = first_word.title()
                    break

        # Pattern 4: Single-word name
        if not name and len(words) == 1:
            clean_text = ''.join(c for c in text if c.isalpha())
            if clean_text.lower() not in greetings and clean_text.lower() not in {"facts", "history", "players",
                                                                                  "sound", "image", "menu"}:
                name = clean_text.title()

        # ✅ If a name is detected
        if name:
            user_state["name"] = name
            # save_memory()
            return [
                {"text": f"🎶 Nice to meet you, {name}!"},
                {
                    "text": "🎵 What would you like to learn today?\n"
                            "1️⃣ Facts\n"
                            "2️⃣ History\n"
                            "3️⃣ Famous Players\n"
                            "4️⃣ Qanun Sound\n"
                            "5️⃣ Qanun Images\n"
                            " (Please type one option, e.g., 'facts' or type any question i will try to answer.) "
            }
            ]

        # ❌ If no name found, and it wasn't the initial /greet, ask again.
        return [{"text": "I didn’t quite catch your name — could you tell me again? 😊"}]

    # quick instrument guard
    other_instruments = {"oud", "piano", "guitar", "violin", "drums"}
    if any(instr in text for instr in other_instruments):
        return [{"text": "I only have qanun info in my knowledge base — I can’t answer about other instruments here."}]



    # -------------------------------------------------------------------------
    # --- LOGIC BELOW THIS LINE RUNS ONLY IF user_state["name"] IS KNOWN ---
    # -------------------------------------------------------------------------

    # 2. --- Menu --- (Should be checked early)
    if any(x in text for x in ["menu", "show menu", "main menu", "back to menu"]):
        user_state["topic"] = None  # Clear topic after menu request
        # save_memory()
        responses.append({"text": "📜 Sure! Here's the menu again:"})
        responses.append({
            "text": (
                "🎶 What would you like to learn about?\n"
                "1️⃣ Facts about the Qanun\n"
                "2️⃣ History of the Qanun\n"
                "3️⃣ Famous Players\n"
                "4️⃣ Qanun Sound\n"
                "5️⃣ Qanun Images\n"
                "(Please type one option, e.g., 'facts' or type any question i will try to answer.)"
            )
        })
        return responses

    # 3. --- Topic Handlers (The core functionality) ---
    if "fact" in text:
        user_state["topic"] = "facts"
        # save_memory()
        return [{
            "text": "🎼 The Qanun is a trapezoid-shaped string instrument with about 78 strings, producing a bright, harp-like tone."}]

    if "history" in text:
        user_state["topic"] = "history"
        # save_memory()
        return [{
            "text": "🏺The qanun is over 1,000 years old and has roots in the Middle East, especially in regions like Egypt, Turkey, and Iraq. Some say it dates back to the 9th century!"}]

    if "player" in text or "famous player" in text:
        user_state["topic"] = "famous players"
        # save_memory()
        return [
            {"text": "🎵 One of the most famous Qanun players is Mohamed Abdo Saleh, who performed with Umm Kulthum."},
            {"image": "http://127.0.0.1:8000/saleh"}]

    if any(w in text for w in ["sound", "audio"]):
        user_state["topic"] = "sound"
        # save_memory()
        return [
            {"text": "🎧 The Qanun produces a bright, zither-like sound — elegant and full of resonance."},
            {"audio": "http://127.0.0.1:8000/sound1"},
        ]

    if any(w in text for w in ["image", "picture", "photo"]):
        user_state["topic"] = "images"
        # save_memory()
        return [
            {"text": "🎨 Here's how a Qanun looks:"},
            {"image": "http://127.0.0.1:8000/image1"}
        ]

    # 4. --- More info ---
    if any(w in text for w in ["more", "continue", "another","what else"]):
        # ... (Your existing 'more info' logic) ...
        topic = user_state.get("topic")
        if topic == "facts":
            responses.append({
                "text": "📚 It typically has 72 to 81 strings, grouped in courses of 3, which gives it a shimmering, harp-like sound. Pluck one course and you hear a triad of harmony instantly."})
        elif topic == "history":
            responses.append({
                "text": "🕰️ The name “qanun” comes from the Greek word “kanon”, meaning “rule” or “law,” reflecting the instrument’s structured, mathematical design."})
        elif topic == "famous players":
            responses.append({
                "text": "🎶 Another renowned player is Julien Jalaleddin Weiss, who mastered the instrument’s microtonal tuning.",
                "image": "http://127.0.0.1:8000/julien"})
        elif topic == "sound":
            responses.append({
                "text": "🎵 Each note on the Qanun can be tuned using small levers, creating intricate scales unique to Arabic music."})
            responses.append({"audio": "http://127.0.0.1:8000/sound2"})
        elif topic == "images":
            responses.append({"text": "📷 Here’s another view of the Qanun:"})
            responses.append({"image": "http://127.0.0.1:8000/image2"})
        else:
            responses.append({"text": "Let's go back to the menu! 😊 Type 'menu' to choose again."})
        return responses

    # 5. --- Positive reactions ---
    positive_words = [
        "nice", "great", "amazing", "cool", "wow", "good", "lovely",
        "beautiful", "awesome", "fantastic", "wonderful", "ok", "okay", "alright", "the qanun is sounds great", "hmmm", "hmm",'looks great'
    ]
    if any(w in text for w in positive_words):
        topic = user_state.get("topic")
        if topic:
            return [{"text": f"😊 I'm glad you think so! Want to know more about the {topic}? Type 'more' or 'menu'."}]
        else:
            return [{"text": "😊 I'm happy you liked it! Type 'menu' to explore more."}]

    # 6. --- Greeting for Returning Users (Lowest priority before Fallback) ---
    if any(token in text for token in ["/greet", "hi", "hello", "hey", "salam"]):
        greeting = get_greeting()
        return [{
            "text": f"{greeting}, {user_state['name']}! What would you like to learn today? Type 'menu' for options. 😊"
        }]

    # 7. --- Farewell handling ---
    farewells = ["bye", "goodbye", "see you", "talk later", "farewell", "exit"]
    if any(word in text for word in farewells):
        user_state["topic"] = None
        # save_memory()
        return [
            {"text": "👋 Goodbye! It was nice teaching you the Qanun today. See you next time!"}
        ]

    # 8. --- Fallback ---
    return [{"text": "🤖 Hmm, I didn’t quite get that. Try typing 'menu' or 'more'."}]


# ---- Run the app ----
if __name__ == "__main__":
    # from pyngrok import ngrok
    # public_url = ngrok.connect(8000)
    # print("🔥 Public URL:", public_url)

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)