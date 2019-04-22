#include <math.h> // C std

#include <iostream> // C++ std

#include "Rectangle.h" // Custom

namespace shapes {

    // Default constructor
    Rectangle::Rectangle () {}

    // Overloaded constructor
    Rectangle::Rectangle (int x0, int y0, int x1, int y1) {
        this->x0 = x0;
        this->y0 = y0;
        this->x1 = x1;
        this->y1 = y1;
    }

    // Destructor
    Rectangle::~Rectangle () {}

    // Return the area of the rectangle
    int Rectangle::getArea () {
        return (this->x1 - this->x0) * (this->y1 - this->y0);
    }

    // Get the size of the rectangle.
    // Put the size in the pointer args
    void Rectangle::getSize (int *width, int *height) {
        (*width) = x1 - x0;
        (*height) = y1 - y0;
    }

    // Move the rectangle by dx dy
    void Rectangle::move (int dx, int dy) {
        this->x0 += dx;
        this->y0 += dy;
        this->x1 += dx;
        this->y1 += dy;
    }
}

/*  Compute the pointwise cross-correlation between two arrays and store in  
 *  out_array. */
void cross_correlation(double * X, double * Y, double * bins, int * C, 
                       int size_x, int size_y, int size_bins, int size_c) {
    double diff;
    for (int yi=0; yi<size_y; ++yi){
        for (int bi=0; bi+1<size_bins; ++bi){
            for (int xi=0; xi<size_x; ++xi){
                diff = X[xi] - Y[yi];
                if(diff <= bins[bi+1]) {
                    if(diff > bins[bi]) {
                        C[bi] = C[bi] + 1;
                    }
                }
            }
        }
    }
}
