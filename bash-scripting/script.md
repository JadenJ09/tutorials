### First setup
!#!/bin/bash !This tells the computer which type of interpreter to use for the script
chmod +x script.sh !The script files also need to have the “execute” permission to allow them to be run.
PATH=~/bin:$PATH !To ensure that scripts in ~/bin/ are available, you must add this directory to your PATH within your configuration file.

### Calling variables
phrase="Hello to you!"
echo $phrase

### if Conditionals
first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=1

if [ $greeting_occasion -lt 1 ]
then
  echo $first_greeting
else
  echo $later_greeting
fi

### Loops
#### for loops
for word in $paragraph
do
  echo $word
done

#### while loops
- Note that arithmetic in bash scripting uses the $((...)) syntax and within the brackets the variable name is not prepended with a $.
while [ $index -lt 5 ]
do
  echo $index
  index=$((index + 1))
done

#### until loops
until [ $index -eq 5 ]
do
  echo $index
  index=$((index + 1))
done

### while loops with if
first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=0
while [ $greeting_occasion -lt 3 ]
do
  if [ $greeting_occasion -lt 1 ]
  then
    echo $first_greeting
  else
    echo $later_greeting
  fi
  greeting_occasion=$((greeting_occasion + 1))
done

### Inputs
#### read
first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=0
echo "How many times should I greet?"
read greeting_limit
while [ $greeting_occasion -lt $greeting_limit ]
do
  if [ $greeting_occasion -lt 1 ]
  then
    echo $first_greeting
  else
    echo $later_greeting
  fi
  greeting_occasion=$((greeting_occasion + 1))
done

#### "$@"
- to accept an indefinite number of input arguments

#### *
- to get all files in a directory, you can use the * character

### Aliases = shortcuts
alias saycolors='./saycolors.sh'
alias saycolors='./saycolors.sh "green"' -> "green" as the first input


