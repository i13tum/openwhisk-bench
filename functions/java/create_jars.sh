#!/usr/bin/env bash

rm prime-number.jar
rm PrimeNumber.class
rm matrix.jar
rm Matrix.class
rm weather.jar
rm Weather.class

javac -cp gson-2.8.1.jar:. PrimeNumber.java
jar cvf prime-number.jar PrimeNumber.class

javac -cp gson-2.8.1.jar:. Matrix.java
jar cvf matrix.jar Matrix.class

javac -cp gson-2.8.1.jar:. Weather.java
jar cvf weather.jar Weather.class