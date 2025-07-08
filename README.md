# ☁️ Word Cloud Generator

This project is a **Python-based web application** that generates a **word cloud visualization** from a given file or paragraph. It reads textual input, processes the content by filtering out common words and articles, and displays the most significant words in a visually compelling cloud format.

Built with **Flask**, **Pandas**, and **Matplotlib**, this tool is ideal for **text analysis**, **NLP preprocessing**, and **data visualization** applications.

---

## 📌 Features

- Upload or input a text paragraph or file  
- Automatically filters out **common stop words**, **punctuation**, and **articles**  
- Counts and visualizes the most frequent words  
- Displays a word cloud based on word frequency  
- Lightweight and easy to run locally with **Flask**

---

## 🛠️ Technologies Used

- **Language**: Python  
- **Web Framework**: Flask  
- **Data Processing**: Pandas  
- **Visualization**: Matplotlib, WordCloud  
- **Others**: OS, string, collections

---

## 📁 Folder Structure

```text
word-cloud/
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # HTML template for input form
├── static/
│   └── wordcloud.png      # Output image (generated)
├── stopwords.txt          # List of stop words to exclude
├── requirements.txt       # Python dependencies
````

---

## 🚀 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/word-cloud.git
   cd word-cloud
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and go to:

   ```
   http://localhost:5000
   ```

---

## 🖼️ Sample Output

![Word Cloud Example](static/wordcloud.png)

---

## 🔮 Possible Enhancements

* Support for different shapes, colors, and fonts in the cloud
* Allow CSV file upload and selection of text column
* Add text cleaning options (lemmatization, case sensitivity toggle)
* Export cloud as PNG or PDF

---

## 👨‍💻 Author

**Haasitha Kodali**
[Email](mailto:kodalihaasitha@gmail.com) | [LinkedIn](https://linkedin.com/in/KodaliHaasitha)

---

## 📜 License

This project is licensed under the MIT License and intended for educational and personal use.
