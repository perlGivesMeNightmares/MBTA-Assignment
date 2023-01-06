# MBTA-Demo
Small POC of the MBTA API for the PaymentWorks demo

### TODOs - Backend
- Better caching
- Try out compression options
- Return actual errors to the front end
- Flesh out unit tests with error cases and better mocking of outbound requests

### TODOs - Frontend
- Make the UI less ugly
- Better data flow so I don't pull stops so often
- Finish typing everything and move to strict mode in tsconfig
- Modularize my components

### TODOs - General
- Never develop in Windows again (no Makefiles? All my scripts blocked by default? bro...)

### Setup
If running this in VSCode, be sure to add "python.defaultInterpreterPath": "/path/to/your/venv/bin/python" to your vscode settings.json. If using intelliJ, right click and mark the "flask_app" directory as a content root. Other IDEs, you'll have to manually add the flask_app path to your PYTHONPATH. Happy to help if there are issues.

If running this on Windows, activating the virtualenv may require `powershell Unblock-File -path \path\to\venv\Scripts\Activate.ps1`

Create a virtualenv with your tool of choice, pip install the requirements.txt, cd into flask_app/src, and then `flask run`.

CD into the react_app, run `npm i`, and then `npm start` (or the yarn equivalents, if preferred). It should open localhost:3000 automatically.
