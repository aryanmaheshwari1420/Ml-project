python3 --version
wget https://bootstrap.pypa.io/get-pip.py
python3  get-pip.py
python3 -m pip -V
python3 -m pip install flask
python3 -m pip install scikit-learn
python3 -m pip install pandas 
python3 -m pip install numpy
export FLASK_APP=app.py
export FLASK_ENV=development
python3 -m flask run
