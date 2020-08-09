package main

import (
  "fmt"
)

func main ()  {
  //_ underscore: descarta valores não utilizados
   numerodebytes , erros := fmt.Println("Hello world!", "Oi galera", "01")
   fmt.Println(numerodebytes, erros)
}
