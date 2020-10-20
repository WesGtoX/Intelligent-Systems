package main

import (
	"fmt"
	"math"
	"time"
)

func sigmoid() {
}

func main() {

	start := time.Now()

	matrix_input := [][]float64{
		[]float64{0.0, 0.0},
		[]float64{0.0, 1.0},
		[]float64{1.0, 0.0},
		[]float64{1.0, 1.0},
	}

	w1 := 7.0
	w2 := 2.0
	w3 := 9.0
	w4 := 4.0
	w5 := 5.0
	w6 := 1.0

	t1 := 8.0
	t2 := 3.0
	t3 := 5.5

	for i := 0; i <= len(matrix_input)-1; i++ {
		s1 := matrix_input[i][0]*w1 + matrix_input[i][1]*w2
		o1 := 1.0 / (1.0 + math.Exp(10.0*(s1-t1)))

		s2 := matrix_input[i][0]*w3 + matrix_input[i][1]*w4
		o2 := 1.0 / (1.0 + math.Exp((20.0-10.0)*(s2-t2)))

		s3 := o1*w5 + o2*w6
		o3 := 1.0 / (1.0 + math.Exp((20.0-10.0)*(s3-t3)))
		fmt.Printf("O3: %v\n", o3)
	}

	runtime := time.Since(start)
	fmt.Printf("\nRuntime: %v secondsan\n", runtime)
}
