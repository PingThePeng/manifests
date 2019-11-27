import pandas

data = pandas.read_csv("images.csv")
with open("commands.sh", 'w') as f:
    f.write("#!/bin/bash")
    for gcr, ali in data[["gcr_uri", "ali_uri"]].values:
        f.write("\n")
        f.write("docker pull %s && docker tag %s %s && docker push %s" % (gcr, gcr, ali, ali))
