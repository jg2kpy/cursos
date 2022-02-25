package main

import "fmt"

func main15() {
	channel := make(chan string)

	go func(channel chan string) {
		for {
			var name string
			fmt.Scanln(&name)
			channel <- name
		}
	}(channel)

	msg := <-channel

	fmt.Println(msg)

	msg2 := <-channel

	fmt.Println(msg2)
}
