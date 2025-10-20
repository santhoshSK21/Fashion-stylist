# AI-Fashion-Stylist

## Overview
AI-Fashion-Stylist is a project designed to provide fashion recommendations using artificial intelligence. The application consists of a backend service that handles data processing and a frontend interface for user interaction.

## Project Structure
```
AI-Fashion-Stylist
├── backend
│   ├── app.py
│   ├── models
│   │   └── __init__.py
│   ├── recommender
│   │   └── __init__.py
│   └── requirements.txt
├── frontend
│   ├── package.json
│   ├── src
│   │   ├── index.js
│   │   ├── App.js
│   │   ├── components
│   │   │   └── Header.js
│   │   └── styles
│   │       └── main.css
│   └── public
│       └── index.html
├── notebooks
│   └── fashion_feature_extraction.ipynb
├── data
│   ├── raw
│   └── processed
└── README.md
```

## Backend
The backend is built using Python and serves as the main entry point for the application. It includes:
- **app.py**: Initializes the web server and sets up routes and middleware.
- **models**: Contains data structure definitions.
- **recommender**: Implements the logic for fashion recommendations.
- **requirements.txt**: Lists the necessary Python dependencies.

## Frontend
The frontend is developed using React and provides an interactive user interface. It includes:
- **package.json**: Configuration for npm, including dependencies and scripts.
- **src/index.js**: Entry point for the React application.
- **src/App.js**: Main application component.
- **src/components/Header.js**: Header component for navigation.
- **src/styles/main.css**: Main styles for the application.
- **public/index.html**: Main HTML file for the frontend.

## Notebooks
The project includes a Jupyter notebook for feature extraction related to fashion data, which may include data processing and analysis steps.

## Data
The data directory is structured to hold both raw and processed data files used in the application.

## Setup Instructions
1. Clone the repository.
2. Navigate to the backend directory and install the required Python packages using:
   ```
   pip install -r requirements.txt
   ```
3. Start the backend server by running:
   ```
   python app.py
   ```
4. Navigate to the frontend directory and install the necessary npm packages using:
   ```
   npm install
   ```
5. Start the frontend application with:
   ```
   npm start
   ```

## Usage
Once both the backend and frontend are running, you can access the application through your web browser. The frontend will allow users to input their preferences and receive fashion recommendations based on the AI model.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.