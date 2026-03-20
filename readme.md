# 🧠 Coding Judge RL Environment (OpenEnv)

## 🚀 Overview

This project is a **minimal Reinforcement Learning (RL) environment** built using the **OpenEnv philosophy**.

It simulates a **coding judge system** (like LeetCode), where:

* An agent submits code
* The environment evaluates it
* A reward is returned based on correctness

---

## 🎯 Goal

To understand how RL environments work in production by:

* Separating environment from training logic
* Using API-based interaction (FastAPI)
* Implementing reward-based evaluation

---

## 🧠 Core RL Loop

```python
observation = env.reset()

while not done:
    action = agent(observation)
    result = env.step(action)
    observation = result["observation"]
```

---

## 🏗️ Project Structure

```
coding_env/
├── models.py              # Data models (Action, Observation, State)
├── client.py              # API client for interacting with env
├── app.py                 # Streamlit UI
└── server/
    ├── environment.py     # Core logic (problem + evaluation)
    ├── app.py             # FastAPI server
    └── Dockerfile         # Container setup
```

---

## ⚙️ How It Works

### 1. Reset Environment

```http
POST /reset
```

Returns:

* Coding problem
* Initial feedback
* reward = 0

---

### 2. Submit Code

```http
POST /step
```

Request:

```json
{
  "code": "def add(a,b): return a+b"
}
```

---

### 3. Evaluation Logic

The environment:

1. Executes submitted code using `exec()`
2. Extracts function (`add`)
3. Runs predefined test cases
4. Compares output with expected results

---

### 4. Reward Calculation

```python
reward = passed_test_cases / total_test_cases
```

Example:

* 3/3 passed → reward = 1.0
* 1/3 passed → reward = 0.33
* 0/3 passed → reward = 0

---

## 🧪 Example

### Input:

```python
def add(a,b): return a+b
```

### Output:

```json
{
  "feedback": "3/3 test cases passed",
  "reward": 1.0
}
```

---

### Incorrect Input:

```python
def add(a,b): return a-b
```

### Output:

```json
{
  "feedback": "0/3 test cases passed",
  "reward": 0
}
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description           |
| -------- | ------ | --------------------- |
| `/reset` | POST   | Start new episode     |
| `/step`  | POST   | Submit code           |
| `/state` | GET    | Get environment state |

---

## 💻 Running the Project

### 1. Install dependencies

```bash
pip install fastapi uvicorn streamlit requests pydantic
```

---

### 2. Start backend server

```bash
uvicorn server.app:app --reload
```

---

### 3. Open API docs

```
http://127.0.0.1:8000/docs
```

---

### 4. Run Streamlit UI

```bash
streamlit run app.py
```

---

## ⚠️ Constraints & Limitations

### 1. Unsafe Code Execution

* Uses `exec()` → NOT secure
* Can run arbitrary code
* Only safe for local/demo use

---

### 2. Single Problem

* Only one hardcoded problem (`add`)
* No dynamic task generation

---

### 3. No Sandboxing

* Code runs in main process
* No isolation (Docker/sandbox not used yet)

---

### 4. One-Step Episode

* Environment ends after one submission (`done = True`)

---

### 5. No Timeout Handling

* Infinite loops in user code can hang server

---

## 🧠 Key Concepts Demonstrated

* RL Environment Design
* Reward-based evaluation
* API-driven environments (OpenEnv)
* Separation of client and server
* Type-safe contracts using Pydantic

---

## 🚀 Future Improvements

* Multiple coding problems
* Hidden test cases
* Code execution sandbox (Docker / subprocess)
* Time limits
* Difficulty levels
* LLM integration for automated agents
* WebSocket support (real OpenEnv style)

---

## 🎯 Summary

This project demonstrates how to:

> Build a production-style RL environment where agents interact via APIs instead of direct function calls.

---

## 👥 Team Notes

* This is a **base prototype**
* Focus is on understanding OpenEnv architecture
* Next step: scale this into a full RL training environment

---

## 📌 Status

✅ Working prototype
🚧 Needs scaling and security improvements
