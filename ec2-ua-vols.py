import boto3
import pandas as pd

def main():
    vdf = pd.DataFrame(boto3.client('ec2').describe_volumes()['Volumes'])
    print (vdf[vdf.State=='available'].VolumeId.unique().tolist())

if __name__ == "__main__":
    main()
