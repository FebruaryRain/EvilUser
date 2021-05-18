checkPyVer(){
    string="$@"
    if [[ "${string:0:1}" -eq "3" ]]
    then
        if [[ "${string:2:1}" -eq "9" ]]
        then
            return "1"
        fi
    fi
    return "0"
}

getPyVer(){
    pyVer=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
    if [[ "$?" -ne "0" ]]
    then
        pyVer=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
        if [[ "$?" -ne "0" ]]
        then
            echo "python command not found. Quitting"
            exit 1
        else
            checkPyVer $pyVer
        fi
    else
        checkPyVer $pyVer
    fi

    #Check for success
    if [[ "$?" -ne "1" ]]
    then
        echo "Need at least python 3.9"
        exit 1
    else
        echo "Found python version $pyVer!"
        return true
    fi
}

checkPipInstalled() {
    pipVer=$(pip3 --version)
    if [[ "$?" -ne 0 ]]
    then
        pipVer=$(pip --version)   
        if [[ "$?" -ne 0 ]]
        then
            echo "pip not found, exiting"
            exit 1
        fi
    fi
    return true
}

help(){
    printf "This will ensure you have the preinstalled software to run our Hackathon game!\n"
    printf "No required input needed. Skip python checking by flag -p\n"
    printf "Flags:\n"
    printf "\t-p Skip python version check <true/false>\n"
    printf "\t-s Skip pip check <true/false>\n"
    printf "\t-h Print help\n"
}

getPackages(){
    echo '\n<=====================================================================>'
    echo '\n\nChecking pip packages are installed.\n'
    
    #Cheek all needed packages
    pip3 install #<Package-name>

}


while getopts 'p:s:xh' flag; do
  case "${flag}" in
    p) PyCheck="${OPTARG}" ;;
    s) PipCheck="${OPTARG}" ;;
    h) help
	   exit;;
	*) help
       exit 1 ;;
  esac
done

if [ -z $PyCheck ] ; then
    PyCheck=true
fi

if [ -z $PipCheck ] ; then
    PipCheck=true
fi

if [ $PyCheck == false ] ; then
    pyFound=getPyVer
else
    pyFound=true
fi

if [ $PipCheck == false ] ; then
    pipFound=checkPipInstalled
else
    pipFound=true
fi

if [ $pipFound -a $pyFound ]
then
    getPackages
    echo '\n<================================Begin================================>\n'

    #Run app
    python3 ./Engine/main.py
fi



