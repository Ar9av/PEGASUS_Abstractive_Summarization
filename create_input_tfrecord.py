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

save_path = "pegasus/pegasus/data/testdata/test_pattern_1.tfrecord"
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


subprocess.call(['sh', 'run_python_file.sh'])