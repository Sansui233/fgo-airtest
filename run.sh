# line=$(ps | grep 'iproxy 8100' | grep -v 'grep')
# if test -z "$line" 
# then
#   echo "run 'iproxy 8100 8100'"
#   iproxy 8100 8100 &
#   sleep 1
# fi

# airtest run ~/Developer/airtest/fgotest.air --no-image
if test -f run.log; then
  rm *.log
fi
python3 ./fgotest.py > run.log 2>&1 &

tail -f run.log | grep 'INFO\|Info\|error\|Error'