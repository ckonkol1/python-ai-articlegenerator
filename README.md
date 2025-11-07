# AI Article Generator

An intelligent article generation application powered by OpenAI's GPT models. Generate compelling, well-researched articles on any topic using advanced AI technology.

![AI Article Generator](/static/img/ai_generator.png)

## Features

- **AI-Powered Content Generation** - Uses OpenAI GPT models to create high-quality articles
- **Multiple AI Models** - Support for GPT-5, GPT-3.5, Claude, and Gemini
- **Professional UI** - Modern Bootstrap-based interface with responsive design
- **Real-time Generation** - Live article creation with loading indicators
- **Copy to Clipboard** - Easy content sharing and export
- **Article Research** - Automatically finds and summarizes professional sources
- **Reference Integration** - Includes citations and links to source materials

## Prerequisites

- Python 3.7 or higher
- OpenAI API key (required for article generation)
  - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
  - You'll need to create an account and add billing information
  - Keep your API key secure and never commit it to version control

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-ai-articlepilot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root directory. You can use the provided template:
   
   ```bash
   # Copy the example file and edit it with your values
   cp .env.example .env
   ```
   
   On Windows:
   
   ```cmd
   copy .env.example .env
   ```
   
   Then edit the `.env` file with your actual values:
   
   ```env
   # OpenAI API Configuration
   OPENAI_API_KEY="your-openai-api-key-here"
   
   # Available AI Models Configuration (optional)
   # Configure which models appear in the dropdown
   AVAILABLE_MODELS=[{"value": "gpt5", "label": "GPT-5"}, {"value": "gpt35", "label": "GPT-3.5"}, {"value": "claude", "label": "Claude"}, {"value": "gemini", "label": "Gemini"}]
   ```
   
   **Alternative: Set environment variables directly**
   
   On Linux/Mac:
   
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```
   
   On Windows:
   
   ```cmd
   set OPENAI_API_KEY=your-openai-api-key-here
   ```

## Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```
   
   Or use the batch script (Windows):
   ```cmd
   run.bat
   ```

2. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## Available Routes

- `/` - Main article generator interface
- `/user/<name>` - Personalized greeting page
- `/create` - API endpoint for article generation (POST)
- `/api/status` - Application status endpoint

## How to Use

1. **Enter a Topic** - Type any subject you want to write about
2. **Select AI Model** - Choose from available AI models (GPT-5, GPT-3.5, etc.)
3. **Generate Article** - Click the generate button and wait for AI processing
4. **Review & Copy** - Review the generated content and copy to clipboard if needed

## API Usage

### Generate Article (POST /create)

```javascript
fetch('/create', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        model: 'gpt5',
        topic: 'Artificial Intelligence in Healthcare'
    })
})
```

**Response:**
```json
{
    "status": "success",
    "message": "Post created successfully",
    "post": {
        "model": "gpt5",
        "topic": "Artificial Intelligence in Healthcare",
        "response": "Generated article content..."
    }
}
```

## Project Structure

```
python-ai-articlepilot/
├── app.py                  # Main Flask application
├── models/
│   └── Post.py            # Post data model
├── services/
│   └── PostService.py     # Article generation service
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   └── css/
│       └── styles.css     # Custom CSS styles
├── requirements.txt        # Python dependencies
├── run.bat                # Windows startup script
├── README.md              # This documentation
├── .env                   # Environment variables (create this)
└── .env.example           # Environment variables template
```

## Dependencies

- **Flask** - Web framework
- **OpenAI** - AI model integration
- **Bootstrap 5** - UI framework
- **Bootstrap Icons** - Icon library

## Configuration

### Available AI Models

- `gpt5` - GPT-5 (Recommended for best quality)
- `gpt35` - GPT-3.5 (Faster, cost-effective)
- `claude` - Claude (Alternative AI model)
- `gemini` - Google Gemini (Alternative AI model)

### Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `AVAILABLE_MODELS` - JSON array of available AI models (optional, defaults to empty array)

## Development

The application runs in debug mode by default, providing:
- Automatic code reloading
- Detailed error messages
- Interactive debugging

To modify the application:
1. Edit the relevant files
2. The server will automatically restart
3. Refresh your browser to see changes

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Invalid requests
- AI model failures
- Network connectivity issues

## Security Notes

- Keep your OpenAI API key secure
- Don't commit API keys to version control
- Use environment variables for sensitive data
- Consider rate limiting for production use

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions, please visit the project repository or contact the development team.

---

**Powered by OpenAI GPT Models** 🤖
