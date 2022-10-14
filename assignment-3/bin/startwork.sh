#Create system variables and change directory to the project folder
$Env: project = myshow
$Env: asset = $1
$Env: task = $2

echo "Set asset to $project : $asset : $task"
echo "${project}/assets/${asset}/${task}"

cd ${project}/assets/${asset}/${task}

