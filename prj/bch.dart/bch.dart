$BH1
this=$(0resolve ${BASH_SOURCE[0]})
prj=$(dirname $(dirname $this))
uv --project $prj run $(dirname $this)/app/$(basename $this) $*
