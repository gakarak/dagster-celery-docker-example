import pandas as pd
import numpy as np
from joblib import Parallel, delayed
from tqdm import tqdm
import fire


def process_file(x: str):
    pass


def main(
    path_idx: str = '/home/ar/github.com_ext/dagster-celery-docker-example/data/idx-mitosis.txt',
    njobs: int = 1
):
    df = pd.read_csv(path_idx)
    
    ret = Parallel(n_jobs=njobs)(delayed(process_file)(x) for x in tqdm(df['path']))


    print('-')


if __name__ == '__main__':
    fire.Fire(main)
