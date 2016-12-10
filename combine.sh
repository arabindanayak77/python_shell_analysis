# Add header to chromosome gene data

echo "starting combining script"
for file in "$@"
do

# Cool trick from Michelle -- combine files
echo '$file'
echo "$file"
cat raw/header.txt "$file" > processed/$file
done
#echo "Switching into new directory"
#cd processed

#for input in *.txt
#do

#echo "Analyzing $input ..."
#python ../Script.py $input
#done
#echo "Done!"


