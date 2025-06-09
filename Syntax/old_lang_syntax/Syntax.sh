# Assign value 3 to variable x
x=3
# Print the value of x and the current user, along with the first input argument
echo "x is $x and you are $(whoami) you entered: $1"
# Shift the positional parameters to the left
shift 
# Print the new first input argument
echo "your input is now $1"
# Print the rest of the input arguments starting from the x-th position
echo "rest of $# inputs but after the $x one: ${@:x}"
# $@ or $* in new line {} for custom range

# Increment x by 1 using let or arithmetic expansion
let x=x+1 # or ((x=x+1)) or x=$((x+1))
# Print the new value of x
echo "$x" # output 4
	
# Declare an array and initialize it with values
declare -a arr
arr=(1 2 3)
# Print the array and the second element
echo "arr is $arr el 1 is ${arr[1]}"

# Read input from the user and print it
read a
echo $a

# String comparison examples
str1="111"
str2="111"
str3=""

# Compare strings and check if str3 is empty
# -eq is for strings use == or = for strs
if [ "$str1" != "$str2" ]
then
	echo "str 1 = str2"
elif [ -z "$str3" ]
then
	echo "str 3 is empty"
else
	echo "str1 != str2"
fi

# Integer comparison examples, use -eq or (( int == int )) inside (())
int1=0
int2=99
int3=20

# Check if int1 is 0 and int2 is not 0
# or do (( int1 == 0 && int2 != 0 ))
if [[ "$int1" -eq 0 && "$int2" -ne 0 ]]
then 
	echo "int1 is 0 and int 2 not 0"
fi

# Check if str3 is empty or int3 is less than or equal to int1
if [[ ! "$str3" || "$int3" -le "$int1" ]]
then
	echo "str3 is empty or int 3 <= int 1 "
fi

# Check if the file bash.sh exists
if [ -f bash.sh ]
then
	echo "bash.sh file exists"	
fi

# Loop through a list of names and print each name
names="Jhon Al Green Lennon"
for i in $names
do
	echo $i 
done

# Loop with a sequence from 1 to 10 with a step of 2 and print each value
for i in $(seq 1 2 10)
do
	echo "i = $i"
done

# While loop example
a=1
# Loop while a is less than 5
while [ "$a" -lt 5 ];
do
	echo "a = $a"
	((a=a+1))
done

# Until loop example
b=1
# Loop until b becomes greater than or equal to 5
until [ "$b" -ge 5 ]
do
	((b=b+1))
done
echo "until done 5 is ge 5"

# Loop through all input arguments and print them, shifting each time
while (( $# > 0 ))
do
	echo $*
	shift
done

# While loop with break and continue
int=20
# Loop while int is greater than or equal to 0
while (( int >= 0 )) 
do
	echo " ran int = $int"
	# Check if int is equal to 20
	if [ "$int" -eq  20 ]
	then
		((int=int-1))
		continue
	fi
	echo " int = $int breaking "
	break
done

# Function to print the first argument
function speak() {
	echo $1 # positional parameter
}
speak hiiii

# Function to add two numbers and return the sum
function add() {
	let sum=$1+$2
	return $sum
}
add 3 44
# Print the return value of the last function call
echo $? # return from the last call of add
