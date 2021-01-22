#include <math.h>
#define g 9.8

double xcoordinate(double v, double theta, double t){
  return v*cos((theta/180.0)*M_PI)*t;
}

double ycoordinate(double v, double theta, double t){
  return v*sin((theta/180.0)*M_PI)*t - 0.5*g*pow(t, 2);
}
