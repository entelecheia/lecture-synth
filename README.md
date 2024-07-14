# LectureSynth

LectureSynth is an AI-powered tool that generates and presents lectures using a 3D talking head avatar and dynamic slide backgrounds. It combines cutting-edge natural language processing, text-to-speech technology, and 3D animation to create engaging, interactive educational experiences.

## Features

- AI-generated lecture content based on user-specified topics and durations
- 3D talking head avatar with realistic lip-syncing and facial expressions
- Dynamic slide generation and display synchronized with lecture content
- Text-to-speech synthesis for natural-sounding audio
- Customizable avatars using Ready Player Me models
- Web-based interface for easy access and use

## Technology Stack

- Backend: Python with Flask, LangChain, OpenAI API
- Frontend: HTML5, CSS3, JavaScript (ES6+)
- 3D Rendering: Three.js
- Avatar Animation: TalkingHead library
- Text-to-Speech: Google Cloud Text-to-Speech API
- Containerization: Docker

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- Docker and Docker Compose (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/entelecheia/lecture-synth.git
   cd lecture-synth
   ```

2. Set up the backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_credentials_file.json
   ```

### Running the Application

1. Start the backend server:
   ```
   cd backend
   python app/main.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:8080`

## Usage

1. Enter a lecture topic and desired duration in the web interface.
2. Click "Generate Lecture" to create the AI-generated content.
3. The 3D avatar will appear and begin delivering the lecture, with synchronized slide backgrounds.
4. Use the controls to pause, resume, or restart the lecture as needed.

## Development

- Backend code is located in the `backend/` directory.
- Frontend code is in the `frontend/` directory.
- Run tests with `pytest` in the backend directory.
- Use `npm run build` to create a production build of the frontend.

## Contributing

We welcome contributions to LectureSynth! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on how to get involved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for their powerful language models
- [Ready Player Me](https://readyplayer.me/) for 3D avatar creation
- [Three.js](https://threejs.org/) for 3D rendering capabilities
- [TalkingHead](https://github.com/met4citizen/TalkingHead) project for avatar animation

## Contact

For questions or support, please open an issue in the GitHub repository or contact the maintainers directly.
