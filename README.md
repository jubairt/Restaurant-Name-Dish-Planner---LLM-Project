# 🍽️ Restaurant Name & Menu Generator

This is a simple and fun AI-powered Streamlit web app that generates a **fancy restaurant name** and a **list of traditional dishes** based on the selected cuisine.

Built using:
- 🧠 [LangChain](https://github.com/langchain-ai/langchain)
- ⚡ [Together AI](https://www.together.ai/)
- 🌐 [Streamlit](https://streamlit.io/)
- 🔗 Mistral-7B-Instruct model

---

## 🚀 Features

- Choose from 5 popular cuisines: Indian, Italian, Mexican, Arabic, American.
- Automatically generate:
  - A creative restaurant name
  - A list of popular dishes for that cuisine
- Clean and minimal UI with Streamlit

---

## 🧠 How It Works

1. **You select a cuisine** from the sidebar.
2. The app sends a prompt to the LLM using `langchain_together`.
3. The LLM returns:
   - A restaurant name.
   - A list of dishes for that restaurant.
4. Both are displayed on the Streamlit page.

---

## 📁 Project Structure

