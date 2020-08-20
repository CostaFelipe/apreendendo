package main

import (
  "fmt"
)

//string tem dois tipos o intepreter string literals e o raw string literals

func main()  {
  x := "Olá tudo bem?\n Espero que\ttudo esteja bem." //intepreter
  //raw
  y := `
  "oi tudo bem fidhfdhfudhfu

  dhfudhfudhfduhf"

  `
  fmt.Println(x)
  fmt.Println(y)
}
