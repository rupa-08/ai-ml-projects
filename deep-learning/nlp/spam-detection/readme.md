# Spam and Ham Email Classifier

This project classifies emails as either **Spam** or **Ham** using two methods:

1. **Sklearn-based Model**: A Naive Bayes classifier trained on a labeled dataset.
2. **Agentic Classifier with Groq API**: Uses a Groq pre-trained model with custom prompt engineering.

Built with **Streamlit** for an interactive UI, users can input email text and receive classification results instantly.

---

## Features

- **Email Classification**: Distinguishes spam (e.g., scams, phishing) from ham (e.g., work emails, personal messages).
- **Streamlit UI**: Simple input interface.
- **Groq API Integration**: Advanced classification with a language model agent.
- **Scikit-learn Model**: Local model using TF-IDF + Naive Bayes.

---

## Groq Agent Details

The **Groq-based agent** classifies emails using prompt-engineering and returns a **JSON** output:

```json
{
  "email_type": "spam" or "ham",
  "reason": "brief reason for classification"
}
