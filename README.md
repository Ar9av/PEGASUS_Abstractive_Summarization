# PEGASUS_Abstractive_Summarization

Run these commands sequentially-:

`
git clone https://github.com/Ar9av/PEGASUS_Abstractive_Summarization
`

`
cd PEGASUS_Abstractive_Summarization/
`
<br />

`
git clone https://github.com/google-research/pegasus
`

<br />
`
sh run.sh
`

<br />
`
pip3 install -e pegasus
`
<br />

`
cp changed_files/public_params.py pegasus/pegasus/params/
`
<br />

`
sh run2.sh
`
<br />

`
python3 create_input_tfrecord.py
`
<br />
