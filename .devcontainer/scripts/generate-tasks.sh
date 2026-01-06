#!/bin/bash

# Construct the Codespace URL
VNC_URL="https://$CODESPACE_NAME-6080.app.github.dev"

# Create the .vscode directory if it doesn't exist
mkdir -p .vscode

# Generate the tasks.json file
cat > .vscode/tasks.json <<EOF
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Open VNC in Simple Browser",
            "type": "shell",
            "command": "\${input:openVNC}",
            "problemMatcher": []
        }
    ],
    "inputs": [
        {
            "id": "openVNC",
            "type": "command",
            "command": "simpleBrowser.show",
            "args": "${VNC_URL}"
        }
    ]
}
EOF

# Generate keybind for it
cat > .vscode/keybindings.json <<EOF
[
    {
        "key": "ctrl+shift+b",
        "command": "workbench.action.tasks.runTask",
        "args": "Open VNC in Simple Browser"
    }
]
EOF

# Install Pygame
pip install -r requirements.txt