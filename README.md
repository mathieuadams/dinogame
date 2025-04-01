# 🦖 Dino Game Bot (Python)

This is a simple Python bot that plays the Chrome Dino game automatically by analyzing a portion of the screen and pressing the spacebar when it detects an obstacle.

---

## 📦 Requirements

Make sure you have Python installed, then install the required packages:

```bash
pip install pillow pyautogui
```

---

## 🚀 How It Works

1. Captures a small region of your screen in front of the dino using `ImageGrab`.
2. Counts the number of dark pixels (indicating an obstacle like a cactus or bird).
3. If enough dark pixels are found, simulates a spacebar press using `pyautogui`.

---

## 🖥️ Screen Region

The obstacle detection region is defined in the script as:

```python
obstacle_region = (173, 699, 259, 772)
```

This should be adjusted based on your screen resolution and where your game window is placed.

> 💡 Tip: Use the commented-out `pyautogui.position()` lines to find your own coordinates.

---

## ▶️ Usage

1. Open Chrome and go to the [Dino game](https://elgoog.im/t-rex/).
2. Move the game window to your **main screen**.
3. Update `obstacle_region` if needed.
4. Run the script:

```bash
python dino.py
```

5. Watch the bot play! 🎮

---

## 🧪 Debugging

The script prints the number of dark pixels detected in real time:

```text
Dark pixels: 0
Dark pixels: 27
```

You can fine-tune the detection threshold by modifying the pixel RGB condition inside `detect_obstacle()`.

---

## 🛠️ Possible Improvements

- Dynamic region scaling as the game speeds up
- Auto-restart after crash
- Support for multiple monitors using `mss` instead of `ImageGrab`
- Visual overlay for detection area

---

## 📸 Screenshot Capture (Optional)

To see what your bot sees:

```python
img = ImageGrab.grab(bbox=obstacle_region)
img.save("debug_view.png")
```

---

## 📄 License

MIT License — free to use and modify.
