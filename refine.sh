echo 'launched refine.sh'
/google-refine-2.5/refine -i 0.0.0.0 &
echo 'called google-refine-2.5'
export OPENREFINE_HOST=23.236.57.67
python load_csv.py ‘/tmp/inputs/refine_input.csv’
echo 'called load_csv.py'