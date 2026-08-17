echo 66
join4sep4parts () {
    local sep=$1; shift
    local acc=$1; shift
    for x in $*; do acc=$acc$sep$x; done
    echo $acc
}
_map () { local f=$1 ; shift; for x in $*; do $f $x; done; }
parts4path () { echo $1 | tr '/' ' ' ; }
name4part  () { echo ${1#*\.}; }    
suffix4str4prefix () {
    echo ${1:${#2}}
}
fn4path () { 
    real=${BASH_SOURCE[1]}
    path=${real#*init.d}
    parts=$(echo $path | tr '/' ' ' )
    names=$(_map name4part $parts )
    fn=$(join4sep4parts '_' $names)
    echo $fn
}
