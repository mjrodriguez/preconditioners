#!/bin/bash -l

#SBATCH -J gpu
#SBATCH -p 96x24gpu4
#SBATCH --gres=gpu:p100:1
#SBATCH --mem=24000
#SBATCH -t 1:00:00
#SBATCH --mail-user=mrodrig6@ucsc.edu
#SBATCH --mail-type=ALL

module load cuda
./query.out