# Path to this repository
$project_root = "C:\git\civitai-metadata-sorter\"

# Name of project module
$module_name = "sort"

# Path to target file to be sorted
$target_f = "C:\examplefile.txt"

# Path to venv activation script
& "C:\Users\User\AppData\Local\pypoetry\Cache\virtualenvs\sort-venv\Scripts\Activate.ps1"
Set-Location $project_root

# Add -b flag if backup file before sorting is wanted
python -m $module_name -f $target_f

Write-Host "`r`nPress any key to continue...";
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');
