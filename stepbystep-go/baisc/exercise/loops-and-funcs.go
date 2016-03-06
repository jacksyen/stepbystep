package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	var z float64 =10
	for  i:=0;i<10 ;i++  {
		z_temp:= z - (math.Pow(z,2)-x)/(z *2)
		if z_temp- z ==0 {
			return z
		}else{
			z =z_temp
		}
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
}
