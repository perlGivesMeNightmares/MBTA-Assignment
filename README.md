# MBTA-Demo
Small POC of the MBTA API

### TODOs - Backend
- Basic caching
- Try out compression options
- Flesh out unit tests with error cases and better mocking of outbound requests

### TODOs - Frontend
- Better data flow so I don't pull stops so often
- Finish typing everything and move to strict mode in tsconfig
- Modularize my components

### TODOs - General
- Never develop in Windows again (no Makefiles? All my scripts blocked by default? bro...)

### Setup
Requires Python 3.9 (currently adding future.__annotations__ imports to make 3.8 back compatable). Also requires pip and npm (or yarn)

If running this in VSCode, be sure to add "python.defaultInterpreterPath": "/path/to/your/venv/bin/python" to your vscode settings.json. If using intelliJ, right click and mark the "flask_app" directory as a content root. Other IDEs, you'll have to manually add the flask_app path to your PYTHONPATH. Happy to help if there are issues.

If running this on Windows, activating the virtualenv may require `powershell Unblock-File -path \path\to\venv\Scripts\Activate.ps1`

### To Run
1. cd into flask_app
2. Create a virtualenv with your tool of choice
3. pip install the requirements.txt
4. cd into src
5. `flask run`.
6. in another tab, CD into react_app
7. run `npm i` (or the yarn equivalent, if preferred)
8. run `npm start`
9. Navigate to localhost:3000 (if not done automatically)
