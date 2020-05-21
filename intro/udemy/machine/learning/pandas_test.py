import pandas as pd
import numpy as geek
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('/Users/vn04q89/Documents/Luigi/projects/Coursera/MathematicsForML/deep_learning/data/titanic-train.csv')
    print(type(df))
    print("HEAD: \n{0}".format(df.head()))
    print("INFO: \n{0}".format(df.info()))
    print("DESCRIBE: \n{0}".format(df.describe()))
