echo 'launched refine.sh'
/google-refine-2.5/refine -i 0.0.0.0 > /tmp/server-log.txt &
echo 'called google-refine-2.5'

sleep 1
while ! grep -m1 ' Point your browser to' < /tmp/server-log.txt; do
    sleep 1
done

export OPENREFINE_HOST=23.236.57.67
python load_csv.py ‘/tmp/inputs/refine_input.csv’
echo 'called load_csv.py'