import pandas as pd
import subprocess
import tensorflow as tf

x = input("Type : (F) for file input , (T) for text input")
if "F" in x:
    fn = input("Input File (with extension):")
    with open("{fn}", r) as f:
        inp = f.read()
elif "T" in x:
    inp = input("Enter Text")

input_dict = dict(
    inputs=[inp],
    targets=[""]
    )

save_path = "./pegasus/data/testdata/test_pattern_1.tfrecord"
data = pd.DataFrame(input_dict)
with tf.io.TFRecordWriter(save_path) as writer:
    for row in data.values:
        inputs, targets = row[:-1], row[-1]
        example = tf.train.Example(
            features=tf.train.Features(
                feature={
                    "inputs": tf.train.Feature(bytes_list=tf.train.BytesList(value=[inputs[0].encode('utf-8')])),
                    "targets": tf.train.Feature(bytes_list=tf.train.BytesList(value=[targets.encode('utf-8')])),
                }
            )
        )
        writer.write(example.SerializeToString())


subprocess.call(['sh', 'python3 pegasus/bin/evaluate.py --params=cnn_dailymail_transformer --param_overrides=vocab_filename=pegasus/ckpt/pegasus_ckpt/c4.unigram.newline.10pct.96000.model,batch_size=1,beam_size=2,beam_alpha=0.6 --model_dir=pegasus/ckpt/pegasus_ckpt/cnn_dailymail/model.ckpt-210000.data-00000-of-00001'])