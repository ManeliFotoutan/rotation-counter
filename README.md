cat > README.md << EOF
# FET Current and Voltage Analysis Project

## Project Overview
This project includes code for calculating and analyzing drain current (ID) and gate-source voltage (VGS) in various operating states of P-Channel and N-Channel FET transistors.  
The \`graffic\` folder contains the GUI (graphical user interface) related code, while the main calculation files are outside this folder.

## Features
- Calculation of drain current (ID) and gate-source voltage (VGS) for different operating states of P-Channel FETs  
- Parameter extraction from circuit schematic images using OCR (pytesseract)  
- User-friendly GUI built with Tkinter for input and result display  
- Support for multiple circuit states and types of analyses  

## Prerequisites
- Python 3.x  
- Required Python packages: numpy, scipy, sympy, tkinter, pillow, pytesseract, pyttsx3  
- Installation of Tesseract-OCR engine on your system (e.g., located at \`/usr/bin/tesseract\` on Linux)  

## How to Run
1. Make sure all prerequisites are installed.  
2. Run the main program using:  
\`\`\`
python run.py
\`\`\`  
3. Choose the desired circuit state or upload a circuit image to extract parameters automatically.  
4. Results will be displayed as text and optionally read aloud using text-to-speech.

## More Information
For detailed explanations of the algorithms, design decisions, and analysis, please refer to the [problem_coloring graph.pdf](./problem_coloring%20graph.pdf) file included in this repository.

## Project Structure
- \`graffic/\` : GUI related code  
- \`dc_fet.py\` : Calculations for N-Channel FET  
- \`dc_fet_pnp.py\` : Calculations for P-Channel FET  
- \`input_n.py\`, \`input_p.py\` : GUI for image processing and input handling  
- \`run.py\` : Main executable file  

## Contact
For questions or support, please contact the developer.

EOF
