import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pandas as pd

import joblib

# --------- AI MODEL LOADING ---------
model = joblib.load("logreg_winner_predictor_model.pkl")
le_group = joblib.load("logreg_encoder_group.pkl")
le_weather = joblib.load("logreg_encoder_weather.pkl")
le_season = joblib.load("logreg_encoder_season.pkl")

def predict_winner
# --------- INTENT DETECTION MODEL LOADING ---------
intent_model = joblib.load("intent_classifier_model.pkl")
intent_vectorizer = joblib.load("intent_vectorizer.pkl")


def detect_intent(text):
    vec = intent_vectorizer.transform([text])
    prediction = intent_model.predict(vec)[0]
    return prediction
    try:
        group_enc = le_group.transform([group])[0]
        weather_enc = le_weather.transform([weather])[0]
        season_enc = le_season.transform([season])[0]
        features = [[goals, rank, group_enc, weather_enc, season_enc]]
        prediction = model.predict(features)[0]
        return "مرشح للفوز" if prediction == 1 else "غير مرشح للفوز"
    except:
        return "حدث خطأ في التنبؤ، تحقق من البيانات المدخلة."


df = pd.read_csv("worldcup_data_sample.csv")

def predict_future():
    winner = df.loc[df['winner'] == 'yes', 'country'].values[0]
    gender_ratio = "60% ذكور / 40% إناث"
    attendance = "متوسط الحضور المتوقع: 75,000"
    season_mode = df['season'].mode()[0]
    weather_mode = df['weather'].mode()[0]
    return f"""الفريق المرجح للفوز: {winner}
الحضور المتوقع: {attendance}
نسبة الحضور حسب الجنس: {gender_ratio}
الطقس المتوقع: {weather_mode}, في {season_mode}
"""


places = {
    "الرياض": {
        "ar": ["البوليفارد وورلد،", "الدرعية", "برج المملكة","سوق الاولين"],
        "en": ["Boulevard Riyadh", "Entrecote Restaurant", "Kingdom Tower"]
    },
    "جدة": {
        "ar": ["البلد", "الواجهة البحرية", "نادي اليخوت","بروميناد جدة"],
        "en": ["Al-Balad", "Jeddah Waterfront"]
    },
    "العلا": {
        "ar": ["مدائن صالح", "صخرة الفيل","منتجع هابيتاس العلا","بلدة العلا القديمة"],
        "en": ["Madain Saleh", "Elephant Rock"]
    },
    "أبها": {
        "ar": ["ممشى الضباب", "المدينة العالية","شارع الفن","مزرعة الليوان"],
        "en": ["Green Mountain", "Abha Dam"]
    },
    "الدمام": {
        "ar": ["كورنيش الدمام", "سوق الحب ","جزيرة المرجان","تكية بحر"],
        "en": ["Dammam Corniche", "Dolphin Village", "Coral Island"]
    },
    "الخبر": {
        "ar": ["إثراء", "الظهران مول","مطل الخبر","قيصرية الراشد مول"],
        "en": ["Ithra", "Dhahran Mall"]
    },
    "الأحساء": {
        "ar": ["سوق القيصرية", "جبل القارة","مدينة جواثا السياحية","فولك الجبل"],
        "en": ["Qaisariah Souq", "Jabal Al Qarah"]
    }
}


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class GreenGoalChatBot(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("GreenGoal ChatBot")
        self.configure(bg="#1e3d32")
        self.language = "ar"

        self.logo_path = "greengoal_logo_avatar_circular.png"
        self.avatar_img = ctk.CTkImage(light_image=Image.open(self.logo_path), size=(35, 35))

        self.chat_frame = ctk.CTkScrollableFrame(self, width=550, height=560, fg_color="#1e3d32")
        self.chat_frame.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="اكتب رسالتك هنا / Type here...", width=400, height=40, font=("Arial", 16))
        self.entry.pack(side="left", padx=(20, 5), pady=10)
        self.entry.bind("<Return>", self.process_input)

        self.send_button = ctk.CTkButton(self, text="Send", command=self.process_input, width=80, height=40)
        self.send_button.pack(side="left", padx=(5, 20), pady=10)

        self.add_bot_message("مرحبًا بك في قرين قول! ماذا تود أن تعرف؟، نبذة عن قرين قول ، التحديات ، التنبؤ ، النقاط ،الأماكن السياحية")

    def process_input(self, event=None):
        user_msg = self.entry.get()
        if not user_msg.strip():
            return
        self.add_user_message(user_msg)
        self.entry.delete(0, "end")
        self.handle_input(user_msg)

    def add_bot_message(self, message):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="#2e5f4d", corner_radius=12)
        frame.pack(pady=5, anchor="w", padx=10)
        avatar_label = ctk.CTkLabel(frame, image=self.avatar_img, text="")
        avatar_label.pack(side="left", padx=5, pady=5)
        label = ctk.CTkLabel(frame, text=message, font=("Arial", 14), wraplength=400, justify="left")
        label.pack(side="left", padx=5, pady=5)

    def add_user_message(self, message):
        frame = ctk.CTkFrame(self.chat_frame, fg_color="#4caf50", corner_radius=12)
        frame.pack(pady=5, anchor="e", padx=10)
        label = ctk.CTkLabel(frame, text=message, font=("Arial", 14), wraplength=400, justify="right")
        label.pack(side="right", padx=5, pady=5)

    def show_places(self, city):
        spots = places[city][self.language]
        if self.language == "en":
            res = f"Top places in {city}:" + "
".join(f"- {spot}" for spot in spots)
        else:
            res = f"وجهات سياحية في {city}:" + "
".join(f"- {spot}" for spot in spots)
        self.add_bot_message(res)

    def handle_input(self, msg):
        msg = msg.strip().lower().replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")

        if any(word in msg for word in ["english", "انجليزي"]):
            self.language = "en"
            self.add_bot_message("Language set to English. You can ask about: GreenGoal, challenges, points, places, prediction.")
        elif any(word in msg for word in ["عربي", "arabic"]):
            self.language = "ar"
            self.add_bot_message("تم تعيين اللغة إلى العربية. يمكنك السؤال عن: قرين قول، التحديات، النقاط، الأماكن، التنبؤ.")
        elif any(word in msg for word in ["تعريف", "about", "green goal", "قرين قول"]):
            res = "GreenGoal is a smart app combining sports, tourism, and sustainability." if self.language == "en" else "قرين قول هو تطبيق ذكي يجمع بين الرياضة، السياحة، والاستدامة."
            self.add_bot_message(res)
        elif any(word in msg for word in ["challenge", "تحدي", "التحديات"]):
            ch = [
                "Use a reusable water bottle.",
                "Turn off unnecessary lights.",
                "Pick up 3 pieces of litter.",
                "Recycle at least one item.",
                "Plant a tree or a small plant.",
            ] if self.language == "en" else [
                "استخدم زجاجة ماء قابلة لإعادة الاستخدام.",
                "أطفئ الأنوار غير الضرورية.",
                "اجمع ثلاث قطع قمامة.",
                "أعد تدوير عنصر واحد.",
                "ازرع شجرة أو نبتة."
            ]
            self.add_bot_message(random.choice(ch))
        elif any(word in msg for word in ["points", "نقاط"]):
            res = "You earn points by completing daily eco challenges!" if self.language == "en" else "تكسب النقاط من خلال تنفيذ التحديات البيئية اليومية!"
            self.add_bot_message(res)
        elif any(word in msg for word in ["places", "اماكن", "الوجهات", "سياحي"]):
            self.add_bot_message("اختر مدينة لعرض الوجهات السياحية:")
            for city in places:
                ctk.CTkButton(
                    self.chat_frame,
                    text=city,
                    command=lambda c=city: self.show_places(c),
                    fg_color="#4caf50",
                    text_color="black",
                    hover_color="#81c784",
                    font=("Arial", 13),
                    corner_radius=8,
                    width=200
                ).pack(pady=2)
            return
        elif any(word in msg for word in ["تنبؤ", "prediction", "future"]):
            self.add_bot_message(predict_future())
        else:
            fallback = "I didn't understand. Try another phrase." if self.language == "en" else "لم أفهم، حاول عبارة أخرى."
            self.add_bot_message(fallback)

if __name__ == "__main__":
    app = GreenGoalChatBot()
    app.mainloop()