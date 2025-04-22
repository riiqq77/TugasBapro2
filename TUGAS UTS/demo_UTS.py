import time

class Sim:
    def __init__(self, name):
        self.name = name
        self.mood = "Neutral"
        self.environment = "normal"
        self.activity = None

    def update_environment(self, env):
        self.environment = env
        print(f"[INFO] {self.name} sekarang berada di lingkungan: {env}")

    def update_activity(self, act):
        self.activity = act
        print(f"[INFO] {self.name} baru saja melakukan aktivitas: {act}")

    def check_mood(self):
        if self.activity == "habis_olahraga":
            self.mood = "berenergi"
        elif self.environment == "bersih_dan_dekoratif":
            self.mood = "terinspirasi"
        else:
            self.mood = "Neutral"

        print(f"[MOOD] Mood saat ini: {self.mood}")

    def reset_conditions(self):
        self.environment = "normal"
        self.activity = None
        print(f"[RESET] Lingkungan dan aktivitas disetel ulang.")

# --- Simulasi ---
simmu = Sim("Alex")

# Coba kasus lingkungan bagus dulu
simmu.update_environment("bersih_dan_dekoratif")
simmu.check_mood()
time.sleep(1)

# Tambahkan aktivitas olahraga
simmu.update_activity("habis_olahraga")
simmu.check_mood()
time.sleep(1)

# Reset semua
simmu.reset_conditions()
simmu.check_mood()
