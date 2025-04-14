# rws_ts_benchmark
Benchmark Comparisons of RWS and TS

### Import note
This repo contains a couple of files that are ~150MB.  Please install [Git Large File Storage](https://git-lfs.com/) before cloning this repo.

### Requirements
The scripts in this repo depend on the [TS](https://github.com/PatWalters/TS) and [TS_Enhanced](https://github.com/WIMNZhao/TS_Enhanced) repos.  Please clone both of these repositories before running the scripts below. 

### Files
This repository contains the benchmarking files used in the paper "Enhanced Thompson Sampling by Roulette Wheel Selection for Screening Ultralarge Combinatorial Libraries".

AMIDE - Benchmarks for the amide library   
QUINAZOLINE - Benchmarks for the quinazoline library   
query_mols.smi - the query molecules used for the ROCS search

### Setting enviroment variables

To run the benchmark scripts below, environment variable must be set to point to the locations of the TS and TS_Enhanced repos.
```
export TS_BASE=$HOME/software/TS
export RWS_BASE=$HOME/software/TS_Enhanced_PW/src_multiprocess
```
The file env_vars.txt provides an example.

### Running the benchmarks

There are four scripts required to run the benchmarks
```
AMIDE/rws_rocs_queries.py
AMIDE/ts_rocs_queries.py
QUINAZOLINE/rws_rocs_queries.py
QUINAZOLINE/ts_rocs_queries.py
```

### Analysis

After running benchmarks, the results can be analyzed with the notebook 








