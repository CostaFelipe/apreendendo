package main
//inicialização, declaração e atribuição
import (
  "fmt"
)

//var x int //declaração
/**
   ints : 0
   float: 0.00
   booleano: false
   strings: ""
   pointers, functions, Interfaces, slices, channels, maps: nil
*/

var (
  a int
  b float64
  c string
  d bool
)

func main()  {
  //x = 10 //inicialização e inicialização
  fmt.Printf("%v, %T\n", a, a )
  fmt.Printf("%v, %T\n", b, b )
  fmt.Printf("%v, %T\n", c, c )
  fmt.Printf("%v, %T\n", d, d )
  //x = 20 //atribuição
  //fmt.Println(x)
}
