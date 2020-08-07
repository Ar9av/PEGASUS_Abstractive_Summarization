mkdir ckpt
gsutil cp gs://pegasus_ckpt/model.ckpt-1500000.index ckpt/
gsutil cp gs://pegasus_ckpt/model.ckpt-1500000.meta ckpt/
gsutil cp gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.model ckpt/
gsutil cp gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.vocab ckpt/
gsutil cp -r gs://pegasus_ckpt/cnn_dailymail ckpt/
cd ..