#!/usr/bin/env bash

wsk -i property set --auth $2
wsk -i property set --namespace $1

wsk -i action delete prime-number
wsk -i action create prime-number ../functions/js/prime-number/prime-number.js --web true -t 300000

wsk -i action delete matrix
wsk -i action create matrix ../functions/js/matrix/matrix.js --web true -t 300000 -m 128

wsk -i action delete weather
wsk -i action create weather ../functions/js/weather/weather.js --web true -t 300000

wsk -i action delete db-get
wsk -i action create db-get --kind nodejs:6 ../functions/js/db-get/action.zip --web true -t 300000

wsk -i action delete payload-size
wsk -i action create payload-size ../functions/js/payload-size/payload-size.js --web true -t 300000

wsk -i action delete prime-number-java
wsk -i action create prime-number-java ../functions/java/prime-number.jar --main PrimeNumber --web true -t 300000

wsk -i action delete matrix-java
wsk -i action create matrix-java ../functions/java/matrix.jar --main Matrix --web true -t 300000 -m 128

wsk -i action delete weather-java
wsk -i action create weather-java ../functions/java/weather.jar --main Weather --web true -t 300000
