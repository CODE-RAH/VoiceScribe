import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence
import speech_recognition as sr
from pydub import AudioSegment
import threading
import os
import random

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("450x350")
root.title("music_player")
root.resizable(False, False)

frame = ctk.CTkFrame(root)
frame.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- نمایش گیف متحرک ------------------
# ---------------- نمایش گیف متحرک ------------------
try:
    gif = Image.open("Shocked13.gif")
    new_size = (450, 380)  # سایز دلخواه

    gif_frames = [
        ImageTk.PhotoImage(frame.resize(new_size, Image.Resampling.LANCZOS))
        for frame in ImageSequence.Iterator(gif)
    ]

    gif_label = ctk.CTkLabel(frame, text="")
    gif_label.place(x=0, y=0)

    def animate(index=0):
        frame_image = gif_frames[index]
        gif_label.configure(image=frame_image)
        gif_label.image = frame_image
        root.after(50, animate, (index + 1) % len(gif_frames))

    animate()
except Exception as e:
    print("گیف بارگذاری نشد:", e)


# ---------------------------------------------------

entry_path = ctk.CTkEntry(frame, placeholder_text="مسیر آهنگ را وارد کن یا دکمه میکروفن را بزن",
                          font=("B Kamran", 20, "bold"), height=50)
entry_path.place(x=20, y=20, relwidth=0.60)

progress = ctk.CTkProgressBar(frame, mode='determinate')
progress.place(x=20, y=120, relwidth=0.92)
progress.set(0)

is_recording = False

def transcribe_with_google_chunked(audio_path):
    recognizer = sr.Recognizer()
    try:
        if audio_path.endswith(".mp3"):
            sound = AudioSegment.from_mp3(audio_path)
        else:
            sound = AudioSegment.from_wav(audio_path)

        sound = sound.set_frame_rate(16000)
        chunk_length_ms = 30 * 1000
        chunks = [sound[i:i + chunk_length_ms] for i in range(0, len(sound), chunk_length_ms)]

        final_text = ""
        for i, chunk in enumerate(chunks):
            progress.set((i + 1) / len(chunks))
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")

            with sr.AudioFile(chunk_path) as source:
                audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data, language="fa-IR")
                max_line_length = 80
                lines = [text[j:j + max_line_length] for j in range(0, len(text), max_line_length)]
                formatted_text = '\n'.join(lines)
                final_text += f"\n--- 🎧 بخش {i + 1} ---\n{formatted_text}\n"
            except sr.UnknownValueError:
                final_text += f"\n🤷‍♂️ بخش {i + 1}: صدایی شناسایی نشد.\n"
            except sr.RequestError as e:
                final_text += f"\n❌ خطا در بخش {i + 1}: {e}\n"
            finally:
                if os.path.exists(chunk_path):
                    os.remove(chunk_path)

        base_name = os.path.basename(audio_path)
        name_without_ext = os.path.splitext(base_name)[0]
        file_name = f"{name_without_ext}_transcription.txt"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(final_text.strip())
        os.startfile(file_name)

    except Exception as ex:
        with open("error.txt", "w", encoding="utf-8") as f:
            f.write(f"🔥 خطای پیش‌بینی‌نشده: {str(ex)}")
        os.startfile("error.txt")

def transcribe_audio_file():
    file_path = entry_path.get().strip()
    if not file_path:
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        entry_path.delete(0, "end")
        entry_path.insert(0, file_path)

    if file_path and os.path.exists(file_path):
        entry_path.delete(0, "end")
        entry_path.configure(placeholder_text="مسیر آهنگ را وارد کن یا دکمه میکروفن را بزن")
        progress.set(0)

        def task():
            transcribe_with_google_chunked(file_path)
            progress.set(1)

        threading.Thread(target=task).start()
    else:
        with open("error.txt", "w", encoding="utf-8") as f:
            f.write("⚠️ مسیر فایل نامعتبر است!")
        os.startfile("error.txt")

def generate_unique_voice_filename():
    while True:
        rand_num = random.randint(1000, 9999)
        file_name = f"voice_{rand_num}.txt"
        if not os.path.exists(file_name):
            return file_name

recognized_text = ""
recording_thread = None

def transcribe_microphone():
    global is_recording, recognized_text, recording_thread
    is_recording = True
    recognized_text = ""
    btn_mic.place_forget()
    btn_stop.place(x=370, y=20)

    def task():
        global recognized_text
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=10)
            except sr.WaitTimeoutError:
                recognized_text = "⏱️ زمان ضبط تمام شد یا هیچ صدایی نبود."
                return

        if is_recording:
            try:
                recognized_text = recognizer.recognize_google(audio, language="fa-IR")
            except sr.UnknownValueError:
                recognized_text = "🤷‍♂️ صدایی شناسایی نشد."
            except sr.RequestError as e:
                recognized_text = f"❌ خطا در اتصال به Google API: {e}"
            except Exception as ex:
                recognized_text = f"🔥 خطای غیرمنتظره: {str(ex)}"

    recording_thread = threading.Thread(target=task)
    recording_thread.start()

def stop_recording():
    global is_recording, recognized_text, recording_thread
    is_recording = False
    btn_stop.place_forget()
    btn_mic.place(x=370, y=20)

    def wait_and_save():
        if recording_thread:
            recording_thread.join()

        if recognized_text.strip():
            file_name = generate_unique_voice_filename()
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(recognized_text.strip())
            os.startfile(file_name)
        else:
            with open("error.txt", "w", encoding="utf-8") as f:
                f.write("⚠️ صدایی برای پردازش ذخیره نشده.")
            os.startfile("error.txt")

    threading.Thread(target=wait_and_save).start()

try:
    mic_img = ctk.CTkImage(light_image=Image.open("mic (1).png"), size=(50, 50))
except:
    mic_img = None

btn_mic = ctk.CTkButton(frame, text="", image=mic_img,  fg_color="gray"
                      , width=50, command=transcribe_microphone)
btn_mic.place(x=370, y=20)

btn_stop = ctk.CTkButton(frame, text="⏹️",  command=stop_recording,
                         font=("B Kamran", 37), fg_color="darkred", width=47)

btn_file = ctk.CTkButton(frame, text="🎵",  command=transcribe_audio_file,
                         font=("B Kamran", 38), width=20, fg_color="gray" )
btn_file.place(x=300, y=20)

root.mainloop()

