mkdir ckpt
gsutil cp gs://pegasus_ckpt/model.ckpt-1500000.index pegasus/ckpt/
gsutil cp gs://pegasus_ckpt/model.ckpt-1500000.meta pegasus/ckpt/
gsutil cp gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.model pegasus/ckpt/
gsutil cp gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.vocab pegasus/ckpt/
gsutil cp -r gs://pegasus_ckpt/cnn_dailymail pegasus/ckpt/
cd ..