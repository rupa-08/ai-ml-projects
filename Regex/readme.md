## What is Regex?

Regex is a **pattern-matching tool**.  
We use it to find specific word, number, email, date, or any custom format from a big text.

The program allows you to enter a text and a regex pattern. It will then show you which parts of the text match your pattern. This is useful for learning and practicing regex, especially for tasks like:

- Email and phone number extraction
- Pattern searching in text
- Input validation

---

## 🧪 Some Useful Regex Patterns

| Purpose                    | Regex Pattern                      | Example Match                   |
|---------------------------|-------------------------------------|----------------------------------|
| Phone Number (10 digits)  | `\d{10}`                            | 9876543210                      |
| Email Address             | `\b\w+@\w+\.\w+\b`                  | hello@example.com               |
| Date (dd/mm/yyyy or -)    | `\b\d{2}[-/]\d{2}[-/]\d{4}\b`        | 13/06/2025, 01-01-2020          |
| PAN Number (Nepal)        | `^\d{9}$`                           | 123456789                       |
| Only Alphabets            | `^[A-Za-z]+$`                       | Nepal, Python                   |
| Lowercase Only            | `^[a-z]+$`                          | regex                           |
| Integer or Float Numbers  | `^-?\d+(\.\d+)?$`                   | 99, -3.14, 0.5                  |
| URL                       | `https?:\/\/(www\.)?\w+\.\w+`       | https://github.com              |
| Username Validation       | `^[a-zA-Z0-9_]{3,16}$`              | rupa_01, student123             |
| Hashtags                  | `#\w+`                              | #Nepal, #StudentLife            |
| File Name with Extension  | `\w+\.(jpg|png|pdf|txt)`            | file.pdf, image.png             |

---
