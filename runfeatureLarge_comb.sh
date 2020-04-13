#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --time=40:00:00




./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-0.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_0.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-1.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_1.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-2.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_2.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-3.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_3.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-4.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_4.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-5.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_5.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-6.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_6.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-7.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_7.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-8.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_8.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-9.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_9.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-10.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_10.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-11.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_11.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-12.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_12.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-13.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_13.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-14.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_14.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-15.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_15.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-16.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_16.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-17.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_17.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-18.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_18.txt
./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 7200 -s 1 -h WDG -a instances/lak503dmap-100agents-19.agents -u 1 --collect 1 --feature featureLarge100/featureLarge100comb_19.txt

#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-0.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-1.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-2.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-3.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-4.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-5.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-6.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-7.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-8.agents -u 0
#./CBSH22 -m instances/lak503d.map -o tmplarge100_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-9.agents -u 0
