# PEGASUS_Abstractive_Summarization
git clone https://github.com/google-research/pegasus
sh run.sh
pip3 install -r requirements.txt
pip3 install -e pegasus
cp changed_files/public_params.py pegasus/params/
cd ..
sh run2.sh