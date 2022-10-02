# Conda Env Creator Script: 
# © Samm-G
# Github: https://github.com/Samm-G

# TODO: Refactor..

echo [$(date)]: "START - init-setup.bash"
echo [$(date)]: "creating environment"

unset -v _VERSION_

while getopts v: flag; do
    case "${flag}" in
            v) _VERSION_="${OPTARG}" ;;
            *)
                echo 'Error in command line parsing' >&2
                exit 1
    esac
done
shift "$(( OPTIND - 1 ))"
if [ -z "$_VERSION_" ]; then
        echo 'Missing -v python version argument' >&2
        exit 1
fi


if ! [ -e "requirements.txt" ] ; then
    echo [$(date)]: "requirements.txt Missing, for new conda env."
else
    if ! [ -d "conda_env" ] ; then
        
        echo [$(date)]: "Append conda-forge Download Channel"
        conda config --append channels conda-forge

        echo [$(date)]: "Creating Conda Env.."
        conda create --prefix ./conda_env python==$_VERSION_ -y
        
        echo [$(date)]: "Activating Environment"
        source activate ./conda_env

        echo [$(date)]: "Clearing pip cache"
        # pip cache purge

        echo [$(date)]: "Installing Requirements from requirements_dev.txt"
        pip install -r requirements_dev.txt

        #echo [$(date)]: "Exporting newly created conda environment into requirements.txt"
        #pip list --format=freeze > requirements.txt
    else
        echo [$(date)]: "Conda Env Already Exists"
    fi
fi

unset -v _VERSION_

# TODO: For automatically adding and Committing.. 
# echo "# ${PWD}" > README.md
# echo [$(date)]: "first commit"
# git add .
# git commit -m "first commit"
echo [$(date)]: "END"


# To Revert Back everything (Or only seleted files and folders)

# rm -rf env/ 
# rm -rf .gitignore 
# rm -rf conda.yaml 
# rm -rf README.md 
# rm -rf .git/