#!/usr/bin/expect

set timeout 10
set host [lindex $argv 0]
set port [lindex $argv 1]
set token [lindex $argv 2]

spawn telnet $host $port
expect "OK"
send "auth $token\r"

for {set i 0} {$i <= 4} {incr i} {
	send "rotate\r"
	sleep 0.1
}
