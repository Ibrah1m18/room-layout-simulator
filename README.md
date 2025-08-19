# 🏠 Room Layout Simulator  

A simple Python OOP project that simulates arranging furniture in a room while respecting design constraints such as:  
- 🚪 Door position  
- 🪟 Window position  
- 📏 Room boundaries  
- 🚫 No overlap between furniture  
- 🔄 Automatic rotation if placement fails  

---

## ✨ Features
- Define a room with width, depth, door, and window.  
- Add furniture with name, dimensions, and position.  
- Automatic validation (boundaries, overlap, door/window).  
- Retry placement with rotation and adjustment.  
- ASCII map 🗺️ to visualize the room layout in the terminal.  

---

## 📂 Project Structure
room-layout-simulator/
│
├── room.py # Main code (Room & Furniture classes + example run)
├── README.md # Project description
└── .gitignore # Python ignore file

---

## 🚀 Getting Started  

### 1️⃣ Clone the repo
```
git clone https://github.com/Ibrah1m18/room-layout-simulator.git
cd room-layout-simulator
```
### 2️⃣ Run the project
python room.py

### 🖥️ Example Output
Room width 10m depth 8m, Door position (2, 0), Window position (8, 4)
BigTable added at (3, 1)
Chair added at (0, 0)
Sofa rotated: new size 3x3
Sofa still can't be placed even after rotation.
Furniture in the room:
- BigTable at (3, 1), size: 5x7
- Chair at (0, 0), size: 2x2

---

## 🛠️ Next Improvements
Graphical visualization (matplotlib or pygame).
Save/Load layouts from JSON or CSV.
Smarter placement suggestions.
Support for different furniture shapes (L-shape, circular, etc).

---

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.

Created by Ibrahim Ahmed 
https://www.linkedin.com/in/ibrahim-ahmed-572475143/

--- 

