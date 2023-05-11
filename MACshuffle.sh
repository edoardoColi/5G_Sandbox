#!/bin/bash
#Author: Edoardo Coli
#
#Requirements: bash tshark
#Tested with: GNU bash, version 4.4.20(1)-release (x86_64-pc-linux-gnu)
#Tested with: TShark (Wireshark) 3.6.7 (Git v3.6.7 packaged as 3.6.7-1~ubuntu18.04.0+wiresharkdevstable)

#Temporary files to save data
_FILE_TMP=".MACrandom.tmp"
_FILE2_TMP=".MAClistall.tmp"
_FILE3_TMP=".MACprobe.tmp"
#Reverence strings
_FILE_REF=''
_SSID_REF=''
#Flags for optional variables
_ENHANCED_FLAG='false'
_VERBOSE_FLAG='false'
_UNIQ_FLAG='false'
_PROBE_FLAG='false'
#Global parametric variable
_MAX_TO=50000
#Counters to show the results
_PCKS_CNTR=0
_PCKS_WLAN_CNTR=0
_PCKS_SSID_CNTR=0
_SCOPE_ALL_CNTR=0
_SCOPE_RAND_CNTR=0
_SCOPE_FIX_CNTR=0
#Set the error color to red
ERROR="\e[31m"
#Set the warning color to yellow
WARNING="\e[33m"
#Set color to highlight the results
LOOKGOOD="\e[0;38;5;208m"
#Set the default color
DEFAULT="\e[0m"

### error_msg(program_name, msg)
function error_msg()
{
	echo "Error: $2"
	echo "Usage: $1 [OPTIONS]"
	echo "Try '$1 -h' for more information."
}

### verbose_msg(msg)
function verbose_msg()
{
	if [[ $_VERBOSE_FLAG == 'true' ]]; then
		echo -e "${LOOKGOOD}$1${DEFAULT}"
	fi
}

### usage(program_name)
function usage()
{
	echo "Usage: $1 [OPTIONS]"
	echo "Specifies a file to analyze if not passed through redirection."
	echo "Pipe(|) have priority over flag -f."
	echo "Redirection(<) have priority over pipe(|)."
	echo "WARNING: When using pipe redirection for data stream remember to use the -U and -w flags."
	echo "         The "-U" flag instructs tcpdump to write packets to the output file immediately (unbuffered mode)."
	echo "         (this should avoid having \"appears to have been cut short in the middle of a packet\")"
	echo "         The "-w" flag specifies the output file where packets will be saved."
	echo
	echo "Options:"
	echo "    -e,		Option to discriminate and merge different MAC addresses (NOT YET DEVELOPED)"
	echo "    -f,		Set the file to analyze"
	echo "    -i,		Set SSID filter to analyze frames"
	echo "    -n,		Number of packets to analyze, in case of file data input (starting from the beginning)	~~TODO test with data stream"
	echo "    -p,		Option to pipe in data stream, without a pipe is ignored"
	echo "    -u,		Option to not consider duplicates in MAC count"
	echo "    -v,		Option for enable verbose messages"
	echo
	echo "Example:"
	echo "         sudo tcpdump -i <interface> -U -w $_FILE3_TMP | $0 -p"
	echo "         $0 < file.pcap"
	echo "         cat file.pcap | $0"
	echo "         $0 -f file.pcap"
	echo
}

### Behavior when received SIGINT
function handle_sigint()
{
	# verbose_msg "SIGINT received..."
	# verbose_msg "killing main process"
	#Cleanup code
	rm -f "$_FILE_TMP"
	rm -f "$_FILE2_TMP"
	rm -f "$_FILE3_TMP"
	rm -f "$lock_print"
	kill -9 $_PROCESS_ID		#forcefully terminate the process, and any subprocesses or child processes, with the ID using the SIGKILL signal. (sometimes it's not enough, why?)
	exit 0
}

### check_ret(prog_name, val_ret)
function check_ret()
{
	notgood=0
	case $1 in
	"filtering_away")
	if [ $2 -ne 0 ]; then
		notgood=1
	fi
	;;
	"print_results")
	if [ $2 -ne 0 ]; then
		notgood=1
	fi
	;;
	*) echo -e "${WARNING}Setup success value returned for function \"$1\"${DEFAULT}"
	return 1;;
	esac
	if [ $notgood -eq 1 ]; then
		echo -e "${ERROR}Problem with the execution of \"$1\", exited with status $2${DEFAULT}"
	fi
}

###
function filtering_away()
{
	scope='wlan.ta'		#filter for the main scope of divide randomized MAC and fixed ones.
	filterSSID=''
#(PARALLEL EXECUTION)
	if ! [[ $_SSID_REF == '' ]]; then
		filterSSID="&& (wlan.ssid == $_SSID_REF)"		#filter from command line to narrow the scope with a specific SSID.
	fi
	filter="($scope) && (wlan) $filterSSID"		#save the complete filter which wanna use to split the data.
	rm -f $_FILE_TMP $_FILE2_TMP		#just as a precaution.
	_TMP=$(mktemp -d)		#creates a unique temporary directory in /tmp/ folder.
	mkfifo $_TMP/pipe1 $_TMP/pipe2 $_TMP/pipe3 $_TMP/pipe4		#creates named pipes inside a temporary directory created before.
	verbose_msg "Counting packets in $_FILE_REF"
	verbose_msg "Counting packets with field 'wlan' in $_FILE_REF"
	if ! [[ $_SSID_REF == '' ]]; then
		verbose_msg "Counting packets with field 'wlan.ssid == $_SSID_REF' in $_FILE_REF"
	fi
	verbose_msg "Counting packets with filter '$filter' in $_FILE_REF"
	(tshark -r $_FILE_REF -T fields -e frame.number -c $_MAX_TO | wc -l >$_TMP/pipe1) &		#the symbol '&' runs the command in the background, allowing other commands to be run in parallel.
	(tshark -r $_FILE_REF -Y "wlan" -T fields -e frame.number -c $_MAX_TO | wc -l >$_TMP/pipe2) &		#the symbol '&' runs the command in the background, allowing other commands to be run in parallel.
	if ! [[ $_SSID_REF == '' ]]; then
		(tshark -r $_FILE_REF -Y "wlan.ssid == $_SSID_REF" -T fields -e frame.number -c $_MAX_TO | wc -l >$_TMP/pipe3) &		#the symbol '&' runs the command in the background, allowing other commands to be run in parallel.
	else
		(echo "(NaN)" >$_TMP/pipe3) &
	fi
	if [[ $_UNIQ_FLAG == 'true' ]]; then
		(tshark -r $_FILE_REF -Y "$filter" -T fields -e wlan.ta -c $_MAX_TO | tr '[:lower:]' '[:upper:]' | sort | uniq | tee >(wc -l > $_TMP/pipe4) >"$_FILE2_TMP") &		#the symbol '&' runs the command in the background, allowing other commands to be run in parallel.
	else
		(tshark -r $_FILE_REF -Y "$filter" -T fields -e wlan.ta -e wlan.fc.type -c $_MAX_TO | tr '[:lower:]' '[:upper:]' | tee >(wc -l > $_TMP/pipe4) >"$_FILE2_TMP") &		#the symbol '&' runs the command in the background, allowing other commands to be run in parallel.
	fi
	while read line; do
		verbose_msg " '$line'"
		_PCKS_CNTR=$(echo $line | cut -d ' ' -f 1)
		_PCKS_WLAN_CNTR=$(echo $line | cut -d ' ' -f 2)
		_PCKS_SSID_CNTR=$(echo $line | cut -d ' ' -f 3)
		_SCOPE_ALL_CNTR=$(echo $line | cut -d ' ' -f 4)
	done < <(paste -d ' ' $_TMP/pipe1 $_TMP/pipe2 $_TMP/pipe3 $_TMP/pipe4)		#the 'paste' command merges the lines of both named pipes and separates them with a space. the '< <' operator to redirect the merged output as input to the while loop.
	rm -rf $_TMP		#remove the temporary directory and all its contents recursively (-r) and without prompting (-f).
	verbose_msg "=> $_PCKS_CNTR for no filter"
	verbose_msg "=> $_PCKS_WLAN_CNTR for filter 'wlan'"
	if ! [[ $_SSID_REF == '' ]]; then
		verbose_msg "=> $_PCKS_SSID_CNTR for filter 'wlan.ssid == $_SSID_REF'"
	fi
	verbose_msg "=> $_SCOPE_ALL_CNTR for filter '$filter'"
	if [[ $_UNIQ_FLAG == 'true' ]]; then
		if [[ $_VERBOSE_FLAG == 'true' ]]; then
			_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | sort | uniq | tee >(wc -l) >"$_FILE_TMP")		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). sort+uniq remove the duplicates(seems useless but necessary). tee split the data in the pipe.
		else
			_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | sort | uniq | wc -l)		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). sort+uniq remove the duplicates(seems useless but necessary).
		fi
	else
		if [[ $_VERBOSE_FLAG == 'true' ]]; then
			_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | tee >(wc -l) >"$_FILE_TMP")		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). tee split the data in the pipe.
		else
			_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | wc -l)		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx).
		fi
	fi
#(SEQUENTIAL EXECUTION)
	# verbose_msg "Counting packets in $_FILE_REF"
	# _PCKS_CNTR=$(tshark -r $_FILE_REF -T fields -e frame.number -c $_MAX_TO | wc -l)		#for details see 'man tshark'.
	# verbose_msg "=> $_PCKS_CNTR"
	# verbose_msg "Counting packets with field 'wlan' in $_FILE_REF"
	# _PCKS_WLAN_CNTR=$(tshark -r $_FILE_REF -Y "wlan" -T fields -e frame.number -c $_MAX_TO | wc -l)		#for details see 'man tshark'.
	# verbose_msg "=> $_PCKS_WLAN_CNTR"
	# if ! [[ $_SSID_REF == '' ]]; then
	# 	filterSSID="&& (wlan.ssid == $_SSID_REF)"		#filter from command line to narrow the scope with a specific SSID.
	# 	verbose_msg "Counting packets with field 'wlan.ssid == $_SSID_REF' in $_FILE_REF"
	# 	_PCKS_SSID_CNTR=$(tshark -r $_FILE_REF -Y "wlan.ssid == $_SSID_REF" -T fields -e frame.number -c $_MAX_TO | wc -l)		#for details see 'man tshark'.
	# 	verbose_msg "=> $_PCKS_SSID_CNTR"
	# fi
	# filter="($scope) && (wlan) $filterSSID"		#save the complete filter which wanna use to split the data.
	# rm -f $_FILE_TMP $_FILE2_TMP		#just as a precaution.
	# if [[ $_UNIQ_FLAG == 'true' ]]; then
	# 	verbose_msg "Counting packets with filter '$filter' in $_FILE_REF"
	# 	_SCOPE_ALL_CNTR=$(tshark -r $_FILE_REF -Y "$filter" -T fields -e wlan.ta -c $_MAX_TO | tr '[:lower:]' '[:upper:]' | sort | uniq | tee >(wc -l) >"$_FILE2_TMP")		#for details see 'man tshark'. tr swap all upper-case. sort+uniq remove the duplicates. tee split the data in the pipe.
	# 	verbose_msg "=> $_SCOPE_ALL_CNTR"
	# 	if [[ $_VERBOSE_FLAG == 'true' ]]; then
	# 		_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | sort | uniq | tee >(wc -l) >"$_FILE_TMP")		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). sort+uniq remove the duplicates(seems useless but necessary). tee split the data in the pipe.
	# 	else
	# 		_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | sort | uniq | wc -l)		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). sort+uniq remove the duplicates(seems useless but necessary).
	# 	fi
	# else
	# 	verbose_msg "Counting packets with filter '$filter' in $_FILE_REF"
	# 	_SCOPE_ALL_CNTR=$(tshark -r $_FILE_REF -Y "$filter" -T fields -e wlan.ta -e wlan.fc.type -c $_MAX_TO | tr '[:lower:]' '[:upper:]' | tee >(wc -l) >"$_FILE2_TMP")		#for details see 'man tshark'. tr swap all upper-case. tee split the data in the pipe.
	# 	verbose_msg "=> $_SCOPE_ALL_CNTR"
	# 	if [[ $_VERBOSE_FLAG == 'true' ]]; then
	# 		_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | tee >(wc -l) >"$_FILE_TMP")		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx). tee split the data in the pipe.
	# 	else
	# 		_SCOPE_RAND_CNTR=$(cut -c 1-17 $_FILE2_TMP | awk '/^.[AE26]:..:..:..:..:../{print $1}' | wc -l)		#cut print selected parts of line. awk is used to consider only MAC specified(x[A E 2 6]:xx:xx:xx:xx:xx).
	# 	fi
	# fi
	_SCOPE_FIX_CNTR=$(expr $_SCOPE_ALL_CNTR - $_SCOPE_RAND_CNTR)
	return 0;
}

###
function print_results()
{
	if ! [ -t 0 ]; then
		echo "Total Number of Packets captured: $_PCKS_CNTR"
	else
		echo "Total Number of Packets captured in \"$_FILE_REF\": $_PCKS_CNTR"
	fi

	echo
	echo -n "Number of Frame Structure of IEEE 802.11"
	if [[ $_UNIQ_FLAG == 'false' ]]; then
		echo -n " (with field 'wlan.ta' $_SCOPE_ALL_CNTR)"
	fi
	echo -n " : $_PCKS_WLAN_CNTR"
	if [[ $_PCKS_WLAN_CNTR -eq 0 || $_PCKS_CNTR -eq 0 ]]; then
		echo
	else
		echo "(~$(expr  $_PCKS_WLAN_CNTR \* 100 / $_PCKS_CNTR )%)"
	fi
	if ! [[ $_SSID_REF == '' ]]; then
		echo "-->Taking into account only those with \"SSID=$_SSID_REF\": $_PCKS_SSID_CNTR"
	fi
	echo -n "----> with randomized MAC: $_SCOPE_RAND_CNTR"
	if [[ $_SCOPE_RAND_CNTR -eq 0 || $_PCKS_WLAN_CNTR -eq 0 ]]; then
		echo
	else
		echo "(~$(expr  $_SCOPE_RAND_CNTR \* 100 / $_SCOPE_ALL_CNTR )%)"
	fi
	echo "----> with fixed MAC: $_SCOPE_FIX_CNTR"
	if [[ $_VERBOSE_FLAG == 'true' ]]; then
		N=10
		if [ $(wc -l < $_FILE_TMP) -gt $N ]; then
			echo && echo -e "${LOOKGOOD}$_FILE_TMP${DEFAULT}" && head -n $N "$_FILE_TMP" && echo "..."
		elif [ $(wc -l < $_FILE_TMP) -gt 0 ]; then
			echo && echo -e "${LOOKGOOD}$_FILE_TMP${DEFAULT}" && head -n $N "$_FILE_TMP"
		fi
		# rm $_FILE_TMP
		if [ $(wc -l < $_FILE2_TMP) -gt $N ] && [[ $_UNIQ_FLAG == 'false' ]]; then
			echo && echo -e "${LOOKGOOD}$_FILE2_TMP${DEFAULT}" && echo "[MAC Address]           [Frame Control Type:]" && echo "                        [0-Management Frame, 1-Control Frame, 2-Data Frame, 3-Extension Frame, (4+)-PV1 Reserved]" && head -n $N "$_FILE2_TMP" && echo "..."
		elif [ $(wc -l < $_FILE2_TMP) -gt $N ]; then
			echo && echo -e "${LOOKGOOD}$_FILE2_TMP${DEFAULT}" && head -n $N "$_FILE2_TMP" && echo "..."
		elif [ $(wc -l < $_FILE2_TMP) -gt 0 ]; then
			echo && echo -e "${LOOKGOOD}$_FILE2_TMP${DEFAULT}" && head -n $N "$_FILE2_TMP"
		fi
		# rm $_FILE2_TMP
	fi
	echo
	return 0
}

### START EXECUTION

_PROCESS_ID=$$		#save the process ID of the current shell

if [ $# -le 0 ] && [ -t 0 ]; then		#if the number of arguments is less than or equal to 0 and we don't have a redirection.
	error_msg $0 "Nothing has been passed to analyze"
	exit 1
else
	while getopts 'ef:hi:n:puv' flag; do		#colon(:) to indicate that the flag has one argument.
	case "${flag}" in
		e) _ENHANCED_FLAG='true' ;;
		f) _FILE_REF="${OPTARG}" ;;
		h) usage $0 
		exit 0;;
		i) _SSID_REF="${OPTARG}" ;;
		n) _MAX_TO="${OPTARG}" ;;
		p) _PROBE_FLAG='true' ;;
		u) _UNIQ_FLAG='true' ;;
		v) _VERBOSE_FLAG='true' ;;
		*) exit 1;;
	esac
	done
fi

if ! [ -t 0 ]; then		#checks if the descriptor is opened with a redirection, regardless of type of redirection used.
	if [ -p /dev/stdin ]; then		#checks if there is a pipe redirection. Redirection from a command and not from a file.
		if [[ $_PROBE_FLAG == 'true' ]]; then		#checks if we want to process a data stream (from tcpdump).
			trap handle_sigint SIGINT		#set up a trap for SIGINT
			lock_print=$(mktemp)		#creates a unique temporary file in /tmp/ folder.
			_FILE_REF="$_FILE3_TMP"
			sleep 2		#waiting to have something to analyze.
			echo -ne "\033[2J\033[H"		#the "\033[2J" sequence clear the terminal screen, the "\033[H" sequence moves the cursor to the top left corner of the screen.
			while true
			do
				filtering_away > $lock_print
				check_ret filtering_away $?
				print_results >> $lock_print
				check_ret print_results $?
				echo -e "\033[2J\033[H"		#the "\033[2J" sequence clear the terminal screen, the "\033[H" sequence moves the cursor to the top left corner of the screen.
				echo "$(cat $lock_print)"		#The "$()" syntax is used to execute the command inside the parentheses and return the result as a string (used to handle print cases TO REVIEW)
			done
		else
			_FILE_REF=$(mktemp)		#creates a unique temporary file in /tmp/ folder.
			cat /dev/stdin > "$_FILE_REF"
		fi
	else
		if head -c4 | od -t x4 -N4 | grep -q -e "a1b2c3d4" -e "d4c3b2a1" -e "0a0d0d0a"; then		#handled only pcap, pcapng files (not erf ...) using magic number of file.
			_FILE_REF=$(mktemp)		#creates a unique temporary file in /tmp/ folder.
			cat /dev/stdin > "$_FILE_REF"
		else
			error_msg $0 "Not a pcap/pcapng file"
			exit 1;
		fi
	fi
else
	if ! [[ $_FILE_REF == '' ]]; then
		if ! head -c4 $_FILE_REF | od -t x4 -N4 | grep -q -e "a1b2c3d4" -e "d4c3b2a1" -e "0a0d0d0a"; then		#handled only pcap, pcapng files (not erf ...) using magic number of file.
			error_msg $0 "'$_FILE_REF' not a pcap/pcapng file"
			exit 1;
		fi
	else
		error_msg $0 "Insert a file using -f flag"
		exit 1;
	fi
fi
filtering_away
check_ret filtering_away $?
if ! [ -t 0 ]; then
	rm -f "$_FILE_REF"
fi
print_results
check_ret print_results $?
exit 0