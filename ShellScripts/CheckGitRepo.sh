#!/bin/bash
git fetch origin

#See if there are any incoming changes
git log HEAD..origin/master --oneline
#Pull if changes
if [[ "${reslog}" != "" ]] ; then
  echo "Update Available. Downloading."
  git merge origin/master #completing the pull
else 
  echo "Current Version Already Installed."
fi

