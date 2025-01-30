import keyboard
import pyautogui
import json
import os
import tkinter as tk
import requests
import easyocr
import threading
import webbrowser

class ScreenRegionSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Select Region")
        self.attributes("-fullscreen", True)
        self.attributes("-alpha", 0.3)
        self.canvas = tk.Canvas(self, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.region = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = event.x, event.y
        if end_x < self.start_x:
            self.start_x, end_x = end_x, self.start_x
        if end_y < self.start_y:
            self.start_y, end_y = end_y, self.start_y
        start_screen_x, start_screen_y = self.get_screen_coordinates(self.start_x, self.start_y)
        end_screen_x, end_screen_y = self.get_screen_coordinates(end_x, end_y)
        self.region = (start_screen_x, start_screen_y, end_screen_x - start_screen_x, end_screen_y - start_screen_y)
        self.quit()

    def get_screen_coordinates(self, canvas_x, canvas_y):
        window_x = self.winfo_rootx()
        window_y = self.winfo_rooty()
        return (window_x + canvas_x, window_y + canvas_y)

def ocr_space_file(filename, api_key, language='eng'):
    payload = {'isOverlayRequired': False,
               'apikey': api_key,
               'language': language,
               'OCREngine': 1
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
            files={filename: f},
            data=payload,
        )
    return r.content.decode()

def on_shortcut():
    print("Shortcut activated!")
    app.ai_working = True
    app.update_overlay_button()
    if 'overlay' in globals():
        overlay.update_button_text()
    
    def get_screenshot_positions():
        if os.path.exists('memory.txt'):
            with open('memory.txt', 'r') as file:
                data = json.load(file)
                if not data or 'A1' not in data or 'B1' not in data:
                    print("No valid regions found in memory.txt. Please select new regions.")
                    return None
                return data
        else:
            print("No memory.txt file found. Please select new regions.")
            return None

    positions = get_screenshot_positions()
    if not positions:
        positions = {}
        regions = ['A1', 'B1']
        for region in regions:
            print(f"Select the {region} region.")
            root = ScreenRegionSelector()
            root.mainloop()
            positions[region] = root.region
        with open('memory.txt', 'w') as file:
            json.dump(positions, file, ensure_ascii=False, indent=4)

    screenshots = {key: pyautogui.screenshot(region=pos) for key, pos in positions.items()}

    for key, screenshot in screenshots.items():
        screenshot.save(f'{key}_screenshot.png')

    use_api = 'easyocr'
    raw_text = {}

    if use_api == 'ocr_space':
        print('Working with OCR Space')
        for key, screenshot in screenshots.items():
            screenshot.save(f'{key}_screenshot.png')
            response = ocr_space_file(f'{key}_screenshot.png', api_key='your-api-key', language='eng')
            raw_text[key] = json.loads(response)['ParsedResults'][0]['ParsedText']
    elif use_api == 'easyocr':
        print('Working with EasyOCR')
        reader = easyocr.Reader(['en'])
        for key, screenshot in screenshots.items():
            screenshot.save(f'{key}_screenshot.png')
            result = reader.readtext(f'{key}_screenshot.png', detail=1)
            if key == 'B1':
                sorted_result = sorted(result, key=lambda x: x[0][0][1])
                raw_text[key] = [text for (_, text, _) in sorted_result]
            else:
                raw_text[key] = ' '.join([text for (_, text, _) in result])
    else:
        print("Invalid OCR method selected. Please choose 'ocr_space', 'easyocr'")

    prompt = (f"""This is a dialogue (Dialogue) from the game. Of course, you must already know it. Your task is to translate all dialogues and analogs into natural Thai, making them sound like real conversations with proper emotions based on the context. You must focus only on the character dialogues in the game and format the output as JSON as follows:

The data I provide comes from using computer vision to read in-game screenshots. 

Normally, in games with dialogue, players don't get only one response choice. However, when I provide you with the extracted text, it may appear merged together—even if they are separate response options. Your job is to differentiate them and determine which ones are similar in meaning, as they could be distinct player responses.

You must think and process everything in either English or Thai only—absolutely no other languages.

For player responses, if the translated sentence naturally includes polite endings like ครับ/ค่ะ and DON'T use XX ผม or นาย XX **USE ฉัน เธอ intends**, you must omit them to avoid making the response unnatural or confusing.

If A1 is has something wrong maybe it's alien word, you can skip it. You should understand it's a computer vision and maybe it missing or ghost detected and if wrong **if you can make it right, please do it**.

**Only some word, If it's a Game's specifically vocab you can skip that word for translation, BUT YOU NEED to continue translate conversation.**
**"A1" is a A1 from character, so you need to translate this too and "B1" is all B1 that game give player select you need to translate too, if "B1" is nothing that mean no option, So you can make it null. YOU NEED TO TRANSLATE BOTH**
DATA I GIVE YOU: {json.dumps(raw_text, ensure_ascii=False, indent=4)} 

THIS IS JUST A FORMAT EXAMPLE:

"A1": "",
"B1": [""],[""],[""] "unlimit if it have more (please parse it becareful and separate it with array)"
]


Each response should contain only one JSON set at a time. If you think there are multiple, you may have misread or incorrectly separated the text.

**Don't text anymore without json and without data i sent you, Because my program listening your answer and it support just json format.** """).replace("\n", "")

    print(json.dumps(raw_text, ensure_ascii=False, indent=4))
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma2:latest",
        "prompt": prompt,
        "stream": True
    }, stream=True)

    try:
        if response.status_code == 200:
            def display_json_overlay():
                overlay = tk.Tk()
                overlay.overrideredirect(True)
                overlay.attributes("-topmost", True)
                overlay.attributes("-alpha", 0.7)
                overlay.configure(bg='black')
                overlay.geometry("600x400+{}+{}".format(
                    overlay.winfo_screenwidth() // 2 - 300,
                    overlay.winfo_screenheight() // 2 - 200
                ))

                json_text = tk.Text(overlay, wrap=tk.WORD, bg='black', fg='white', font=("Arial", 12))
                json_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

                def close_overlay():
                    response.close()
                    overlay.destroy()

                # Bind close event click to the overlay
                overlay.bind("<Button-1>", lambda event: close_overlay())

                # Start processing the response data
                for line in response.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8')
                        parsed_json = json.loads(decoded_line)
                        response_text = parsed_json.get('response', '')
                        done = parsed_json.get('done', False)
                        print(response_text)
                        
                        # Update the text widget
                        json_text.config(state=tk.NORMAL)
                        json_text.insert(tk.END, response_text)
                        json_text.config(state=tk.DISABLED)
                        json_text.see(tk.END)

                        # Update the tkinter window to reflect changes
                        overlay.update()

                        if done:
                            break

                # Start the tkinter main loop after the UI is set up
                overlay.mainloop()

            display_json_overlay()
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        pass
    finally:
        app.ai_working = False
        app.update_overlay_button()
        if 'overlay' in globals():
            overlay.update_button_text()

class ResizableOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.7)
        self.configure(bg='black')
        self.geometry("100x50+{}+{}".format(
            self.winfo_screenwidth() - 220,
            self.winfo_screenheight() - 120
        ))

        self.start_button = tk.Button(self, text="Start", command=self.start_ai, font=("Arial", 8))
        self.start_button.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.bind("<Button-3>", self.close_overlay)  # Right-click to close the overlay
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<ButtonPress-3>", self.start_resize)
        self.bind("<B3-Motion>", self.do_resize)
        self.bind("<ButtonRelease-3>", self.stop_resize)

        self._offsetx = 0
        self._offsety = 0
        self._resizex = 0
        self._resizey = 0

    def close_overlay(self, event=None):
        self.destroy()

    def start_move(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry(f"+{x}+{y}")

    def stop_move(self, event):
        self._offsetx = 0
        self._offsety = 0

    def start_resize(self, event):
        self._resizex = event.x
        self._resizey = event.y

    def do_resize(self, event):
        delta_x = event.x - self._resizex
        delta_y = event.y - self._resizey
        new_width = self.winfo_width() + delta_x
        new_height = self.winfo_height() + delta_y
        self.geometry(f"{new_width}x{new_height}")

    def stop_resize(self, event):
        self._resizex = 0
        self._resizey = 0

    def start_ai(self):
        if not app.ai_working:
            threading.Thread(target=on_shortcut).start()
            self.update_button_text()

    def update_button_text(self):
        if app.ai_working:
            self.start_button.config(text="Loading...", state=tk.DISABLED)
        else:
            self.start_button.config(text="Start", state=tk.NORMAL)

def create_overlay_button():
    global overlay
    overlay = ResizableOverlay()
    overlay.mainloop()

# Listen for hotkey press
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DeepAlogue")
        self.geometry("800x600")
        
        # Add Start and Stop buttons at the bottom
        self.start_button = tk.Button(self, text="Start", command=self.start_listening, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=20, pady=20, expand=True)
        
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_listening, font=("Arial", 14))
        self.stop_button.pack(side=tk.RIGHT, padx=20, pady=20, expand=True)
        
        self.overlay_button = tk.Button(self, text="Overlay", command=create_overlay_button, font=("Arial", 14))
        self.overlay_button.pack(side=tk.BOTTOM, padx=20, pady=20, expand=True)
        
        self.listener = None
        self.xquit = False
        self.ai_working = False  # Variable to track if AI is working

    def start_listening(self):
        self.listener = threading.Thread(target=self.listen_for_hotkey)
        self.listener.start()
        print("Listening for F12 key...")

    def stop_listening(self):
        self.xquit = True
        keyboard.unhook_all()
        print("Stopped listening.")
        self.quit()
        self.destroy()
        if 'overlay' in globals():
            overlay.close_overlay()

    def listen_for_hotkey(self):
        while not self.xquit:
            if keyboard.is_pressed('f12'):
                self.ai_working = True
                on_shortcut()
                self.ai_working = False
                while keyboard.is_pressed('f12'):
                    pass  # Wait until the key is released to avoid multiple triggers

    def update_overlay_button(self):
        if self.ai_working:
            self.overlay_button.config(text="Loading...", state=tk.DISABLED)
        else:
            self.overlay_button.config(text="Overlay", state=tk.NORMAL)

def check_for_updates():
    response = requests.get("https://api.github.com/repos/kang49/deepalogue/releases/latest")
    latest_version = response.json()["tag_name"]
    current_version = "v1.0.1"  # Replace with your current version

    if latest_version > current_version:
        def open_github_releases():
            webbrowser.open("https://github.com/kang49/deepalogue/releases")

        update_popup = tk.Tk()
        update_popup.title("Update Available")
        update_popup.geometry("300x150")
        label = tk.Label(update_popup, text=f"A new version {latest_version} is available!")
        label.pack(pady=10)
        button_github = tk.Button(update_popup, text="Go to GitHub Releases", command=open_github_releases)
        button_github.pack(pady=5)
        button_not_now = tk.Button(update_popup, text="Not Now", command=update_popup.destroy)
        button_not_now.pack(pady=5)
        update_popup.mainloop()

if __name__ == "__main__":
    check_for_updates()
    app = App()
    while not app.xquit:
        try:
            app.mainloop()
        except:
            pass