j () {
    [ $1. == . ] && {
        0bold "usage: j[ump] dest"
        echo dest may be bh0 or part of repo name
        return    
    }
    [ $1. == bh0. ] && {
        cd $(dirname $BH0)
        return
    }
    for repo in $(bh0 bch locals | grep $1); do
        cd $BH0_BCH/$repo
    done
}

