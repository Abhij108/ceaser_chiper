# 🔐 Caesar Cipher Web Application

A modern, user-friendly web application for encrypting and decrypting text using the Caesar cipher algorithm. Built with Flask backend and an interactive HTML/CSS/JavaScript frontend.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [How Caesar Cipher Works](#how-caesar-cipher-works)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- 🎨 **Beautiful Modern UI** - Gradient design with smooth animations
- 🔐 **Encrypt/Decrypt Text** - Caesar cipher encryption and decryption
- 🎚️ **Flexible Shift Control** - Use slider or number input (0-25)
- 📋 **Copy to Clipboard** - One-click copying of results
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- ⚡ **Real-time Processing** - Instant encryption/decryption
- 🔄 **Error Handling** - User-friendly error messages
- 🌐 **CORS Enabled** - Can be used as an API for other applications

## 📦 Requirements

- Python 3.6+
- Flask
- Flask-CORS

## 🚀 Installation

### Step 1: Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd caesar-cipher-app

# Or manually download and extract the files
```

### Step 2: Install Dependencies

```bash
pip install flask flask-cors
```

Or using requirements.txt (if available):
```bash
pip install -r requirements.txt
```

### Step 3: Verify File Structure

Make sure your project looks like this:

```
caesar-cipher-app/
├── app.py
├── README.md
└── templates/
    └── index.html
```

## 📂 Project Structure

```
project-root/
│
├── app.py                 # Flask backend with cipher logic
├── templates/
│   └── index.html        # Web UI (HTML/CSS/JavaScript)
└── README.md            # This file
```

### Files Description

**app.py**
- Flask application setup
- Caesar cipher encryption function: `ceaser_chiperE()`
- Caesar cipher decryption function: `ceaser_chiperD()`
- API endpoints: `/`, `/encrypt`, `/decrypt`, `/health`

**index.html**
- Complete interactive UI
- Client-side JavaScript for API communication
- Responsive styling with CSS
- Copy to clipboard functionality

## 🎯 Usage

### Starting the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Using the Web Interface

1. **Open your browser** and navigate to: `http://localhost:5000`

2. **Enter text** in the text area
   - Works with any characters (letters, numbers, special characters)
   - Only alphabetic characters are shifted

3. **Set the shift value**
   - Use the number input (0-25) or drag the slider
   - Shift 1 = A→B, B→C, etc.

4. **Encrypt or Decrypt**
   - Click 🔒 **Encrypt** to encrypt your text
   - Click 🔓 **Decrypt** to decrypt your text

5. **Copy the result**
   - Click 📋 **Copy Result** to copy to clipboard

### Example

**Input Text:** "Hello World"  
**Shift Value:** 3  
**Encrypted:** "Khoor Zruog"

Shifting each letter by 3 positions in the alphabet.

## 🔌 API Endpoints

### 1. GET `/`

Returns the web UI

```bash
curl http://localhost:5000/
```

### 2. POST `/encrypt`

Encrypts text using Caesar cipher

**Request:**
```bash
curl -X POST http://localhost:5000/encrypt \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World", "shift": 3}'
```

**Response:**
```json
{
  "result": "Khoor Zruog",
  "status": "success"
}
```

### 3. POST `/decrypt`

Decrypts text using Caesar cipher

**Request:**
```bash
curl -X POST http://localhost:5000/decrypt \
  -H "Content-Type: application/json" \
  -d '{"text": "Khoor Zruog", "shift": 3}'
```

**Response:**
```json
{
  "result": "Hello World",
  "status": "success"
}
```

### 4. GET `/health`

Checks if server is running

```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "Server is running"
}
```

## 🔒 How Caesar Cipher Works

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet.

### Algorithm

1. For each character in the text:
   - If it's a letter (A-Z or a-z):
     - Shift it by the specified amount
     - Wrap around the alphabet (Z→A)
     - Preserve case (uppercase stays uppercase)
   - If it's not a letter (numbers, symbols, spaces):
     - Keep it unchanged

### Example with Shift 3

```
Plain:     A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher:    D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

**Text:** "ABC XYZ"  
**Encrypted:** "DEF ABC"

## ⌨️ Keyboard Shortcuts

- **Ctrl + Enter** in text area = Encrypt (coming soon)
- **Tab** = Navigate between inputs

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solution:** Install Flask
```bash
pip install flask flask-cors
```

### Error: "Port 5000 is already in use"

**Solution:** Either close other apps using port 5000 or change the port in app.py:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change 5000 to 8000
```

### UI doesn't load

**Solution:** Make sure the folder structure is correct:
- `templates/` folder must be in the same directory as `app.py`
- `index.html` must be inside the `templates/` folder

### API returns 400 error

**Solution:** Check that:
- Text field is not empty
- Shift value is between 0-25
- Request body is valid JSON

## 🔐 Security Notes

- This is a simple cipher for educational purposes
- Caesar cipher is NOT secure for real-world data encryption
- Do not use for sensitive information
- For production use, consider stronger encryption methods (AES, RSA, etc.)

## 📝 Example Use Cases

- Educational purposes - Learn about cryptography
- Text obfuscation - Hide simple messages
- Programming practice - Understand API design
- Teaching - Demonstrate client-server communication

## 🎨 Customization

### Change Port

Edit `app.py`:
```python
app.run(debug=True, port=8000)  # Default is 5000
```

### Change Theme Colors

Edit `index.html` (in the `<style>` section):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Change these hex colors to your preference */
```

### Disable Debug Mode

For production, edit `app.py`:
```python
app.run(debug=False, port=5000)
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Caesar Cipher - Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## 📄 License

This project is open source and available for educational and personal use.

## 👤 Author

Created for learning Flask web development and cryptography basics.

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Improve documentation

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section
2. Verify file structure and file names
3. Check that all dependencies are installed
4. Ensure Python version is 3.6 or higher

---

**Happy Encrypting! 🔐**
