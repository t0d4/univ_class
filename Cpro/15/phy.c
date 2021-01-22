#include <stdio.h>
#include <stdlib.h>
#include "coordinate.h"

int main(int argc, char *argv[]){

  double v = 0.0;
  double theta = 0.0;
  double t = 0.0;
  double x = 0.0;
  double y = 0.0;

  if(argc != 2){
    printf("Usage: ./phy [output file name]\n");
    exit(1);
  }

  char *file = argv[1];
  FILE* fp = fopen(file, "w");
  if(fp == NULL){
    printf("Couldn't open the file.\n");
    exit(1);
  }

  printf("Please input\n");

  printf("Initial velocity (m/s) (double):");
  scanf("%lf", &v);

  printf("Angular (0-360 degree) (double):");
  scanf("%lf", &theta);

  while(y >= 0){

    x = xcoordinate(v, theta, t);
    y = ycoordinate(v, theta, t);

    // printf("t = %lf, x = %lf, y = %lf\n", t, x, y);
    fprintf(fp, "%.2f, %.2f, %.2f\n", t, x, y);

    t += 0.1;
  }

  return 0;

}
