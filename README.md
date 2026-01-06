# Enclose.Horse for ClassPad

<img width="409" height="668" alt="image" src="https://github.com/user-attachments/assets/0e3970ee-99e2-4b23-bc43-f0a7bcdc9b63" />

## Quick setup

If you just want to quickly test something, go with "Open in a codespace".

## Install to the calculator

Mount your classpad to your PC as USB storage device and copy the `mhorse.py` to the calculator.

Then, go into the HollyHock Launcher (under System, in the menu) and search for the PythonExtra addin.

Run in, and on the "Files" pane (using the `=` button) look for your python file. You can navigate using the arrow and enter a folder using `EXE` key.

Press `EXE` to run it, and you should have the bouncing logo or your program working !

### What is gint?
`gint` is the main module that powers **drawing**, **keyboard input**, and graphics control in PythonExtra.

You use it for:

- Drawing shapes and pixels (`gint.dpixel`)

- Reacting to key presses (`gint.pollevent()`)

- Controlling the screen update (`gint.dupdate()`)

Here’s a very simple example that draws a **blue rectangle** on screen:

```python
import gint

# Clear the screen with white color
gint.dclear(gint.C_WHITE)

# Draw a filled blue rectangle from (50, 50) to (150, 100)
gint.drect(50, 50, 150, 100, gint.C_BLUE)

# Send drawing to the screen
gint.dupdate()

# Wait for a key press to exit
gint.getkey()
```

> Read more:
>
> 👉 [Beginner Guide to PythonExtra](https://classpaddev.github.io/wiki/python/introduction)
>
> 👉 [gint module reference](https://git.planet-casio.com/Lephenixnoir/PythonExtra/src/branch/main/docs/sh/modgint-en.md)

## 💬 Need Help?

- 🧠 Ask ChatGPT:
    [PythonExtra Helper on ChatGPT](https://chatgpt.com/g/g-67fb8fb50e2c8191a7df1b814ad8fce9-pythonextra-helper)
- 💬 Ask real people on Discord: 
    [SnailMat Server (ClassPad Club)](https://discord.gg/jZQWY9DBKT)

## Project Structure
This repo contains:

- `mhorse.py`: The enclose.horse game

- `gint.py`: Simulator (using pygame) to test you game locally

- `.typings/` and `.vscode/`: are settings folder for PythonExtra to work on VS Code. Do not delete them.

- `/` and `.vscode/`: are settings folder for PythonExtra to work on VS Code. Do not delete them.


When deploying to your calculator, you only need to copy your code (`mhorse.py`, the file you created etc).

> Do NOT copy `gint.py` to your calculator, nor the ".typing" nor "tools" nor "_data". All of that is only useful when debugging locally.

## Debugging locally

If you have the `gint.py` file in the same place than your code (`mhorse.py`), you can try to run or even debug it with visual studio (or your favorite IDE)

You'd need pygame installed, you can do it with `pip install -r requirements.txt`

If using VS Code, you can simply place breakpoint on your code (`mhorse.py` for example) and press "F5", and choose "Python Debugger" then "Python File".
