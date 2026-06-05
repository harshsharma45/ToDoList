# ToDoList
# Python CLI To-Do List: Daily Routine Tracker

## 📖 Overview
This project is a Command-Line Interface (CLI) To-Do List application built entirely in Python. Designed as a **Daily Routine Tracker**, it allows users to manage their tasks seamlessly through an interactive terminal menu. 

This project was developed as **Project 1: The To-Do List** for the **DecodeLabs Industrial Training Kit (Batch 2026)**[cite: 1]. It demonstrates foundational backend engineering principles, specifically focusing on data management and programmatic logic without relying on external databases.

---

## ✨ Key Features
* **Interactive CLI Menu:** A continuous `while True` loop keeps the application active until the user explicitly decides to quit.
* **Batch Task Addition:** Users are not limited to adding one task at a time; the program asks how many tasks to add and uses a `for` loop to append them sequentially.
* **Safe Task Removal:** Features built-in validation to check if a specific task exists in the list before executing the `remove()` operation, preventing runtime errors.
* **Live Task Viewing:** Instantly displays the current state of the routine tracker on demand.
* **Error Handling:** Implements a `try-except` block to catch `ValueError` exceptions, ensuring the program does not crash if a user inputs a non-integer value when navigating the menu.

---

## 🛠️ Under the Hood: Technical Architecture
This application is built on core computer science concepts highlighted in the DecodeLabs training:
* **The IPO Model:** The system follows the standard Input (Data Entry), Process (Modification), and Output (Display) architecture.
* **Dynamic Arrays (The Heap):** Tasks are stored in a standard Python list, which functions as a dynamic array in memory. 
* **Volatile Memory:** Because the application relies on RAM for storage, the list acts as a volatile container. This means that once the program is terminated, the data is cleared. 
* **The Gatekeeper:** The application logic is encapsulated in a `main()` function and triggered via the `if __name__ == "__main__":` block, ensuring professional script execution.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** must be installed on your operating system.
* No external libraries or dependencies are required (built entirely with standard Python).

### Installation
1. Clone this repository to your local machine using Git:
```bash
   git clone [https://github.com/harshsharma45/ToDoList.git](https://github.com/harshsharma45/ToDoList.git)

```

2. Open your terminal or command prompt.
3. Navigate to the project directory:

```bash
   cd ToDoList

```

### Execution

Run the following command to start the application:

```bash
python main.py

```

*(Note: If you named your file something else, replace `main.py` with your actual file name).*

---

## 💻 Usage Example

Upon running the script, you will see the main menu:

```text
To-Do List
welcome to your Daily Routine Tracker List 
Enter your choice
1.Add Task
2.Remove Task
3.View Task
4.Quit

```

**Scenario: Adding Tasks**

1. Type `1` and press **Enter**.
2. The program asks: `enter the number of tasks:`. Type `2` and press **Enter**.
3. It asks for the tasks sequentially. Type `Read documentation` and `Write Python code`.
4. The program will confirm: `Your Tasks = ['Read documentation', 'Write Python code']`.

**Scenario: Removing a Task**

1. Type `2` and press **Enter**.
2. The program asks: `Enter the task to remove:`. Type `Read documentation`.
3. The program will output the updated list: `Remaining Tasks = ['Write Python code']`.

---

## 🔮 Future Enhancements

* **Data Persistence:** Implement JSON serialization to save tasks to a disk file so data is not lost when the application closes.
* **Numbered List View:** Upgrade the viewing feature to use `enumerate()` for simultaneous indexing and value display.
* **Input Sanitization:** Add string formatting (like `.strip()` or `.lower()`) to handle accidental spaces or capitalization differences when removing tasks.
