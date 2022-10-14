#Make directory assets/$asset/maya/scenes if none exist
$filePath = "assets/$asset/maya/scenes"
if(Test-Path assets/$asset/maya/scenes)
{
    Write-Host = "Folder Exists"
}
else
{
    New-Item $filePath -ItemType Directory
    Write-Host = "Folder Created Successfully"
}
