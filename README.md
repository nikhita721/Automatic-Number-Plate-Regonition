# 🚗 License Plate Recognition System

A modern Flask-based web application for automatic license plate recognition using AI-powered external APIs.

## ✨ Features

- **AI-Powered Recognition**: Advanced machine learning algorithms for accurate license plate detection
- **Modern Web Interface**: Responsive Bootstrap-based UI with real-time feedback
- **URL-Based Processing**: Simply provide an image URL for instant recognition
- **Confidence Scoring**: Get confidence levels for each recognition result
- **Error Handling**: Comprehensive error handling and user feedback
- **Security**: Input validation and secure API communication

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/nikhita721/Automatic-Number-Plate-Regonition.git
cd Automatic-Number-Plate-Regonition
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
cp env.example .env
# Edit .env with your API keys
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
- Open your browser and go to: http://localhost:5000

## 🛠 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
# License Plate Recognition API Configuration
RAPIDAPI_KEY=your_rapidapi_key_here
RAPIDAPI_HOST=zyanyatech1-license-plate-recognition-v1.p.rapidapi.com

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key_here

# Server Configuration
HOST=0.0.0.0
PORT=5000
```

### API Setup
1. Sign up for a RapidAPI account
2. Subscribe to the License Plate Recognition API
3. Get your API key
4. Update the `.env` file with your API key

## 📁 Project Structure

```
Automatic-Number-Plate-Regonition/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
├── .gitignore            # Git ignore file
├── README.md             # This file
├── templates/            # HTML templates
│   └── base.html         # Main template
├── static/               # Static files
│   ├── css/             # CSS files
│   ├── js/              # JavaScript files
│   └── images/          # Sample images
└── uploads/             # Upload directory (created automatically)
```

## 🔧 Usage

### Web Interface
1. Open the application in your browser
2. Enter an image URL containing a license plate
3. Click "Recognize License Plate"
4. View the results with confidence score

### API Endpoints

#### Health Check
```bash
GET /health
```

#### License Plate Recognition
```bash
POST /predict
Content-Type: application/x-www-form-urlencoded

output=https://example.com/car-image.jpg
```

## 🎯 Features

### **Modern UI/UX**
- Responsive Bootstrap 5 design
- Real-time feedback and loading indicators
- Flash messages for user feedback
- Example images for testing

### **Robust Error Handling**
- Input validation
- API error handling
- Timeout protection
- User-friendly error messages

### **Security Features**
- Input sanitization
- URL validation
- Secure API communication
- Environment variable protection

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker Deployment
```bash
# Build Docker image
docker build -t license-plate-recognition .

# Run container
docker run -p 5000:5000 license-plate-recognition
```

## 📊 API Integration

The application uses the ZyanyaTech License Plate Recognition API through RapidAPI:

- **Endpoint**: `https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url`
- **Method**: POST
- **Input**: Image URL
- **Output**: License plate text and confidence score

## 🔍 Error Handling

### **Input Validation**
- URL format checking
- Required field validation
- File size limits

### **API Error Handling**
- Network timeout protection
- HTTP error handling
- JSON parsing errors
- Empty response handling

### **User Feedback**
- Success messages with results
- Warning messages for no detection
- Error messages for failures
- Loading indicators during processing

## 🧪 Testing

### Manual Testing
1. Use the provided example images
2. Test with various image URLs
3. Test error scenarios (invalid URLs, network issues)

### Example Test URLs
- Use the sample images included in `static/images/`
- Test with different license plate formats
- Test with various image qualities

## 🔒 Security Considerations

- **API Key Protection**: Store API keys in environment variables
- **Input Validation**: Validate all user inputs
- **Rate Limiting**: Consider implementing rate limiting for production
- **HTTPS**: Use HTTPS in production environments

## 📈 Performance

- **Async Processing**: Non-blocking API calls
- **Timeout Handling**: 30-second timeout for API requests
- **Error Recovery**: Graceful error handling
- **Caching**: Consider implementing response caching

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the application logs for debugging
- Review the API documentation

## 🔮 Future Enhancements

- **File Upload**: Direct image file upload support
- **Batch Processing**: Multiple image processing
- **Database Integration**: Store recognition history
- **Advanced Analytics**: Recognition statistics and trends
- **Mobile App**: React Native or Flutter mobile app
- **Real-time Processing**: WebSocket support for live processing

---

**Built with ❤️ for automatic license plate recognition**