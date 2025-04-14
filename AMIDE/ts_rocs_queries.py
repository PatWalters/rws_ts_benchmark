#!/usr/bin/env python

import sys
import os
try:
    base_path = os.environ["TS_BASE"]
except:
    print("Please define the TS_BASE environement variable",file=sys.stderr)
    print("TS_BASE should point to the directory with the TS repo",file=sys.stderr)
    sys.exit(1)
sys.path.append(base_path)
import pandas as pd
from ts_main import run_ts
import sys
import importlib
import json
from tqdm.auto import tqdm

def read_input(json_filename: str, ref_filename, ref_colname) -> dict:
    """
    Read input parameters from a json file
    :param json_filename: input json file
    :return: a dictionary with the input parameters
    """
    input_data = None
    with open(json_filename, 'r') as ifs:
        input_data = json.load(ifs)
        input_data['evaluator_arg']['ref_filename']=ref_filename
        input_data['evaluator_arg']['ref_colname']=ref_colname
        module = importlib.import_module("evaluators")
        evaluator_class_name = input_data["evaluator_class_name"]
        class_ = getattr(module, evaluator_class_name)
        evaluator_arg = input_data["evaluator_arg"]
        evaluator = class_(evaluator_arg)
        input_data['evaluator_class'] = evaluator
    return input_data

def run_benchmark(idx, dir_path):
    input_dict = read_input("ts_amide_rocs.json","amide_rocs.parquet",f"RUN_{idx:03d}")
    df_list = []
    for i in tqdm(range(0,10)):
        out_df = run_ts(input_dict,hide_progress=True)
        out_df = out_df.sort_values("score",ascending=False).head(100)
        out_df["idx"] = idx
        out_df["cycle"] = i
        df_list.append(out_df)
    pd.concat(df_list).to_csv(f"{dir_path}/ts_amide_{idx:03d}.csv",index=False)
    

def main():
    dir_path = "ts_results"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    for i in range(1,111):
        print(i)
        run_benchmark(i, dir_path)
    

if __name__ == "__main__":
    main()








