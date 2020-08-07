cd pegasus
mkdir ckpt
gsutil cp -r gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.model ckpt/pegasus_ckpt
gsutil cp -r gs://pegasus_ckpt/c4.unigram.newline.10pct.96000.vocab ckpt/pegasus_ckpt
gsutil cp -r gs://pegasus_ckpt/model.ckpt-1500000.data-00000-of-00001 ckpt/pegasus_ckpt
gsutil cp -r gs://pegasus_ckpt/model.ckpt-1500000.index ckpt/pegasus_ckpt
gsutil cp -r gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.data-00000-of-00001 ckpt/pegasus_ckpt/cnn_dailymail/
gsutil cp -r gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.index ckpt/pegasus_ckpt/cnn_dailymail/
gsutil cp -r gs://pegasus_ckpt/cnn_dailymail/model.ckpt-210000.meta ckpt/pegasus_ckpt/cnn_dailymail/