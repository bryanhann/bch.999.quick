__path_append() {
    [ ${1}. == . ] && return
    [[ ":$PATH:" == *":${1}:"* ]] && return
    echo "  [${FUNCNAME}()] append path [${1}]"
    export PATH=${PATH}:${1}
}

__path_append $(dirname ${BASH_SOURCE[0]})/bin

source $(dirname ${BASH_SOURCE[0]})/functions
source $(dirname ${BASH_SOURCE[0]})/aliases

