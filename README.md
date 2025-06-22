# 🍽️ AI Restaurant Name & Menu Generator

![App Screenshot](Web_Interface.png)

Welcome to the **AI Restaurant Name & Menu Generator** — a fun and creative tool that uses the power of **LLMs (Large Language Models)** to suggest **fancy restaurant names** and a **menu of traditional dishes** based on the cuisine you choose. Built using **LangChain**, **Together AI (Mistral-7B)**, and **Streamlit**.

---

## ✨ Features

- One-click generation of restaurant names based on cuisine
- Smart and culturally accurate dish suggestions
- Uses Together AI's `mistralai/Mistral-7B-Instruct-v0.1`
- LangChain for chaining prompts with ease
- Clean Streamlit interface
- Bullet-style output for clear presentation
- Lightweight and easy to run

---

## 🧠 Tech Stack

- **Streamlit** – UI interface
- **LangChain** – LLM prompt chaining
- **Together AI** – LLM inference (Mistral)
- **Python** – Backend logic

---

## 🧪 How It Works

### 1. User picks a cuisine (e.g., "Indian").

### 2. Prompt 1 (Restaurant Name):
```text
Suggest only one fancy name (no description or explanation) for a restaurant that serves {cuisine} food.
```

➡️ Output: `"The Royal Thali"`

### 3. Prompt 2 (Dish Menu):
```text
Suggest a list of traditional and popular {cuisine} dishes served at a restaurant named "{restaurant_name}".
Only return the dish names in bullet-point format.
```

➡️ Output:
- Butter Chicken  
- Paneer Tikka  
- Biryani  
- Chole Bhature

---

## 🗂️ Code Overview

### 🔸 main.py
- Displays title and sidebar in Streamlit
- Lets users choose cuisine
- Calls `generate_restaurant_name_and_items()` from helper
- Displays restaurant name and list of dishes

### 🔹 langchain_helper.py
- Uses `PromptTemplate` and `Together` LLM
- First prompt → generates a name
- Second prompt → uses that name to generate menu
- Returns name and dishes as a dictionary

---

## 🔐 Security Notes

- ✅ Your API key is stored in `secret_key.py`
- 🛑 Don’t upload your API key to GitHub!
- ✅ Add it to `.gitignore`:

```
secret_key.py
```

---

## 🧠 What I Learned

- LangChain’s `PromptTemplate` and chaining
- Streamlit for LLM UIs
- How to structure multi-step LLM pipelines
- Use of `Together` inference API
- Prompt engineering basics
  
---

### ✅ Conclusion

Through this project, I learned how to integrate Large Language Models (LLMs) like **Mistral-7B** using the `langchain` framework to build an end-to-end AI application. I practiced **prompt engineering**, designed **modular LLM chains**, and created a clean and interactive **web UI using Streamlit**. 

This helped me understand how to bridge backend AI logic with a user-friendly frontend — turning powerful models into practical tools like a restaurant name and menu generator.

---

## 🙌 Credits

- [LangChain](https://www.langchain.com/)
- [Together AI](https://www.together.ai/)
- [Mistral](https://mistral.ai/)
- [Streamlit](https://streamlit.io/)
