package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os"
    "strings"
    // "strconv"
)

var ops = map[string]string {
    string('🍡'): "add",
    string('🤡'): "clone",
    string('📐'): "divide",
    string('😲'): "if_zero",
    string('😄'): "if_not_zero",
    string('🏀'): "jump_to",
    string('🚛'): "load",
    string('📬'): "modulo",
    string('⭐'): "multiply",
    string('🍿'): "pop",
    string('📤'): "pop_out",
    string('🎤'): "print_top",
    string('📥'): "push",
    string('🔪'): "sub",
    string('🌓'): "xor",
    string('⛰'): "jump_top",
    string('⌛'): "exit",
    string('🥇'): "accumulator1",
    string('🥈'): "accumulator2",
    string('✋'): "STOP?",
    string('😐'): "UNKNOWN?",
    string('💰'): "MARKER?",
    string('🖋'): "MARKER?"
}

func main() {

    file, err := os.Open("program")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    b, err := ioutil.ReadAll(file)
    rom := strings.Split(string(b), " ")

    for i, c := range rom {
        fmt.Println("-------------------------------------")
        fmt.Println(i)
        fmt.Println(c) 
        fmt.Println(ops[c])
        for j, d := range c {
            fmt.Println(j, d)
        }
    }
}
