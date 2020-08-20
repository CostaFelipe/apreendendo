package main

import (
  "fmt"
)

var x int = 10
var y int

func main()  {
    y = 20
    fmt.Printf("%v, %T\n", x, x)
    fmt.Printf("%v, %T", y, y)
}
