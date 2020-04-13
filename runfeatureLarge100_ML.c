#include "mpi.h"
#include <string.h>
#include <bits/stdc++.h> 
int main (int argc, char *argv[])
{
    int i, rank, size, namelen;
    char name [MPI_MAX_PROCESSOR_NAME];

    MPI_Init (&argc, &argv);

    MPI_Comm_size (MPI_COMM_WORLD, &size);
    MPI_Comm_rank (MPI_COMM_WORLD, &rank);
    MPI_Get_processor_name (name, &namelen);

    char str1[300]="./CBSH2 -m instances/lak503d.map -o run_large_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-";
    char str2[300]=".agents -u 1"
    char strnum[300];
    printf ("Running from task %d on %s!\n", rank, name);
    sprintf(strnum, "%d", rank);
    char command[300];
    memset(command,0,sizeof(command));
    strcat(command,str1);
    strcat(command,strnum);
    strcat(command,str2);
    system(command);
    
    if (rank == 0 )
       printf ("MPI World size = %d processes\n", size);

    MPI_Finalize ();

}
/*
 ./CBSH2 -m instances/lak503d.map -o run_large_comb.csv -t 3600 -s 1 -h WDG -a instances/lak503dmap-100agents-0.agents -u 1
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-10.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-11.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-12.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-13.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-14.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-15.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-16.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-17.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-18.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-19.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-20.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-21.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-22.agents -u 4
#./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-23.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-42.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-43.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-44.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-45.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-46.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-47.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-48.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-49.agents -u 4
sleep 72000
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-24.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-25.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-26.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-27.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-28.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-29.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-30.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-31.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-32.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-33.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-34.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-35.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-36.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-37.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-38.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-39.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-40.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-41.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-42.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-43.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-44.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-45.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-46.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-47.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-48.agents -u 4
./CBSH_Large_ML3 -m instances/lak503d.map -o runML_large_100_4.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-49.agents -u 4




./CBSH_Large_ML3 -m instances/lak503d.map -o tp.csv -t 5400 -s 1 -h WDG -a instances/lak503dmap-100agents-22.agents -u 4

*/
