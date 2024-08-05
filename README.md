# For Windows
Download the folder
Extract it
Open the terminal in the folder
sudo apt update [optional]
Install/upgrade Python/Pip [sudo apt install python3-pip]
Install virtual environment [sudo pip3 install virtualenv] (optional)
Create virtual environmnet [python -m venv eppenv]
Activate python environment [eppenv/Scripts/activate]
pip install --no-cache-dir --upgrade -r requirements.txt
Run the ipynb file
streamlit run streamlit.py
